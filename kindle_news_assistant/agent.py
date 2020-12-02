"""Fetch articles from the feeds in `feeds.txt`."""
import math
import random
from copy import deepcopy
from itertools import zip_longest
from urllib.parse import urlparse
from typing import (
    Callable,
    Dict,
    List,
    Optional,
    Iterable,
    Union,
    Tuple,
    overload,
    cast,
)
import os
from multiprocessing.dummy import Pool as ThreadPool
import newspaper
from newspaper.article import Article
from newspaper.utils import get_available_languages
from sklearn.neural_network import MLPRegressor  # type: ignore
from tqdm import tqdm
from kindle_news_assistant.safe_open import safe_open
from kindle_news_assistant.word_extractor import article_to_frequency

DELIVERY_SIZE = 10  # Number of articles to deliver
DEFAULT_FETCH_LIMIT = (
    20 * DELIVERY_SIZE
)  # Default limit on the number of articles to fetch.
# In other words, each article that is delivered is the best of 20 articles

BATCH_SIZE = 100  # Size of a batch of articles in each efficient download cycle

dirname = os.path.dirname(__file__)
RELATIVE_PATH = "../userdata/feeds.txt"
absolute_path = os.path.join(dirname, RELATIVE_PATH)

# --------------------------------------------------
# > Helper Functions
# --------------------------------------------------


def grouplen(sequence, chunk_size):
    """Group a sequence by a given chunk_size.

    :param sequence: The sequence to be chunked.
    :param chunk_size: The size of the chunks.
    :return: A sequence of grouped tuples.
    """
    return zip_longest(*(iter(sequence),) * chunk_size)


def create_language_filter(language: str):
    """Use to create a higher order component for filtering articles by a language.

    :param language: The language to filter by
    :return: Whether or not the article is
    """
    assert (
        language in get_available_languages()
    ), f'"{language}" is not a supported language.'

    def language_filter(article: Article):
        return article.meta_lang == "" or article.meta_lang == language

    return language_filter


class Agent:
    """A class for fetching articles from the feeds in `feeds.txt`."""

    def __init__(
        self, include_old: Optional[bool] = False, thread_count: Optional[int] = None
    ):
        """Initialize the Agent class.

        :param include_old: Whether to include cached articles, defaults to False
        :param thread_count: An argument that enforces a certain thread count for this instance
        """
        self.include_old = bool(include_old)
        assert thread_count is None or thread_count >= 1
        self.thread_count = thread_count

        feeds_file = safe_open(absolute_path, "r")
        content = feeds_file.read()
        feeds_file.close()
        self.feeds = content.split("\n")

    def efficient_map_unordered(
        self,
        func: Callable,
        items: List,
        show_bar: Optional[bool] = None,
        thread_count: Optional[int] = None,
        **kwargs,
    ):
        """Run a function over a list of items with optional loading bars and multithreading.

        :param func: The function to be called over the list.
        :param items: The items to map the function over.
        :param show_bar: Whether to show a progress bar
        :param thread_count: The number of threads, as specified by the function call.
            Note: This value is overridden by the instance's thread_count value, if set.
        :param kwargs: A number of keyword arguments to be passed to the tqdm progress bar instance
        :return: A mapped version of the items.
        """
        if self.thread_count == 1:
            iterable = tqdm(items) if show_bar else items
            return list(map(func, cast(Iterable, iterable)))

        if self.thread_count is not None:
            thread_count = self.thread_count

        pool = ThreadPool(thread_count)
        return_value = (
            list(tqdm(pool.imap_unordered(func, items), **kwargs))
            if show_bar
            else list(pool.imap_unordered(func, items))
        )
        pool.close()
        pool.join()

        return return_value

    def fetch(self, limit: int = DEFAULT_FETCH_LIMIT):
        """Fetch the articles from the feeds.

        :param limit: Limit the number of returned article by some number, \
            defaults to `DEFAULT_FETCH_LIMIT`.
        :return: All of articles from the configured sources, without parsing or downloading.
        """
        print("Fetching article sources...")
        articles: List[Article] = []

        # Multi-thread article source construction
        number_of_feeds = len(self.feeds)

        def build_source(feed: str):
            source = newspaper.build(
                feed, memoize_articles=not self.include_old, keep_article_html=True
            )
            if len(source.articles) == 0 and self.include_old:
                tqdm.write(
                    "Warning: The source `" + feed + "` appears to have no articles."
                )
            articles.extend(source.articles)

        self.efficient_map_unordered(
            build_source, self.feeds, True, number_of_feeds, total=number_of_feeds
        )

        # Shuffle articles before limiting to make it more fair
        if len(articles) > limit:
            print(f"Found {len(articles)} articles, but only including {limit}.")
        else:
            print(f"Found {len(articles)} articles.")
        random.shuffle(articles)
        trimmed = articles[:limit]
        return trimmed

    def download(self, articles: List[Article]):
        """Download (and parse) articles in-place efficiently using multithreading.

        :param articles: The articles to be downloaded and parsed.
        """
        # Multi-thread article downloads and parsing
        print("Downloading and parsing articles...")

        number_of_articles = len(articles)

        def download_and_parse(article: Article):
            try:
                article.download()
                article.parse()
            except newspaper.article.ArticleException:
                pass

        self.efficient_map_unordered(
            download_and_parse,
            articles,
            True,
            number_of_articles,
            total=number_of_articles,
        )

    def download_and_validate(self, articles: List[Article], language: Optional[str]):
        """Download and validate articles across multiple threads, \
            and not in-place like the `Agent.download` method.

        This method is mainly used during the `Agent.score_by_model` method.
        It is recommended to use the download method instead when not filtering
        using the model.

        :param articles: The articles to download.
        :param language: The language to filter articles by
        :return: A tuple of original articles that are valid and their downloaded counterparts
        """
        # Articles that have not been downloaded but are marked as valid:
        # - These are used when zipping the ratings and articles below
        valid_articles: List[Article] = []
        # Articles that have been downloaded:
        downloaded_copies: List[Article] = []

        language_filter = None
        if language is not None:
            language_filter = create_language_filter(language)

        def download_and_parse_batch(article: Article):
            # Download and parse article copies (so that downloads can be purged later)
            if article is None:
                return

            copy = deepcopy(article)
            # Skip if it has already been downloaded and parsed
            if article.is_parsed:
                valid_articles.append(article)
                downloaded_copies.append(copy)
                return

            try:
                copy.download()
                copy.parse()

                # Filter invalid articles and articles that aren't the right language
                if copy.is_valid_body() and (
                    language_filter is None or language_filter(copy)
                ):
                    valid_articles.append(article)
                    downloaded_copies.append(copy)
            except newspaper.article.ArticleException:
                pass

        self.efficient_map_unordered(
            download_and_parse_batch, articles, False, len(articles)
        )

        return valid_articles, downloaded_copies

    def score_by_model(
        self, articles: List[Article], model: MLPRegressor, language: Optional[str]
    ):
        """Score articles by using the learned regression model.

        It scores articles across multiple threads and in batches for efficiency.
        In addition, invalid articles and articles in the wrong languages
        are filtered out automatically.

        Process:
        1. Use a for loop every `BATCH_SIZE` that starts fetching articles across multiple threads
        2. Chunk each batch of articles into a smaller sizes, spread those across threads, and
            use a for loop to fetch each of those.
        3. Then, once all of the `BATCH_SIZE` number of articles are fetched, score the articles
            using the regression model.

        :param articles: The articles
        :param model: The learned regression model
        :param language: The language to filter by
        :return: A tuple of scores and articles.
        """
        batched_articles = grouplen(articles, BATCH_SIZE)
        number_of_batches = math.ceil(len(articles) / BATCH_SIZE)

        scored: List[Tuple[float, Article]] = []

        print("Downloading, parsing, and scoring articles in batches...")
        for batch in tqdm(
            batched_articles, unit_scale=BATCH_SIZE, total=number_of_batches
        ):
            valid_articles, downloaded_copies = self.download_and_validate(
                batch, language
            )

            # Guard against an empty batch
            if len(valid_articles) == 0:
                return []

            # Score the batch using the regression model
            frequencies = [
                article_to_frequency(article.text) for article in downloaded_copies
            ]
            ratings = model.predict(frequencies)
            scored.extend(zip(ratings, valid_articles))

        return scored

    @overload
    def filter_by_model(
        self,
        articles: List[Article],
        model: MLPRegressor,
        language: Optional[str] = None,
    ) -> List[Article]:  # noqa: D102
        ...

    @overload
    def filter_by_model(
        self,
        articles: List[Article],
        model: MLPRegressor,
        language: Optional[str] = None,
        include_complement: bool = False,
    ) -> Union[List[Article], Tuple[List[Article], List[Article]]]:  # noqa: D102
        ...

    def filter_by_model(
        self,
        articles: List[Article],
        model: MLPRegressor,
        language: Optional[str] = None,
        include_complement: Optional[bool] = False,
    ) -> Union[List[Article], Tuple[List[Article], List[Article]]]:
        """Filter articles by using the learned regression model. \
            It filters articles in batches to minimize memory consumption.

        :param articles: The articles
        :param model: The learned regression model
        :param include_complement: Whether to include articles that would not be
            recommended, defaults to False
        :param language: A language filter for the articles
        :return: Articles that were approved by the regression model, in recommended order.
            Will return a tuple with filtered and complement articles if `include_complement`
            flag is set to True.
            Articles will not be parsed on return.
        """
        scored = self.score_by_model(articles, model, language)
        sorted_by_rating = sorted(scored, reverse=True, key=lambda pair: pair[0])

        if include_complement:
            filtered = []
            complement = []

            for (rating, article) in sorted_by_rating:
                if rating >= 0.5:
                    filtered.append(article)
                else:
                    complement.append(article)

            return filtered, complement

        return [zipped[1] for zipped in sorted_by_rating]

    @staticmethod
    def filter_duplicates(articles: List[Article]) -> List[Article]:
        """Filter duplicate articles by their urls.

        :param articles: The article list
        :return: A filtered list of articles that excludes duplicates
        """
        seen_dict: Dict[str, List[str]] = {}  # Track seen article urls by source url
        filtered: List[Article] = []

        for article in articles:
            source_url = article.source_url
            path = urlparse(article.url).path

            if source_url not in seen_dict:
                seen_dict[source_url] = []

            has_been_seen = False
            for seen_path in seen_dict[source_url]:
                if path == seen_path:
                    has_been_seen = True
                    break

            if has_been_seen:
                continue

            seen_dict[source_url].append(path)
            filtered.append(article)

        return filtered

    @staticmethod
    def filter_by_language(articles: List[Article], language: str) -> List[Article]:
        """Filter articles by a specified language.

        :param articles: The list of articles
        :param language: The language to filter by
        :return: A filtered list where all the articles are the right language
        """
        language_filter = create_language_filter(language)
        return [article for article in articles if language_filter(article)]

    def batch(
        self,
        model: Optional[MLPRegressor] = None,
        size: Optional[int] = DELIVERY_SIZE,
        language: Optional[str] = None,
    ):
        """Fetch a batch of articles.

        Will filter duplicates and filter by the model if one is given.

        :param model: The learned article classification model
        :param size: The size of the batch, defaults to DELIVERY_SIZE
        :param language: The language to filter by
        :return: A list of articles
        """
        articles = self.fetch()
        articles = Agent.filter_duplicates(articles)
        if model is not None:
            articles = self.filter_by_model(articles, model, language)
        limited = articles[:size]
        return limited
