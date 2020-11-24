"""Fetch articles from the feeds in `feeds.txt`."""
from typing import List, Optional, Union, Tuple, overload
import os
from multiprocessing.dummy import Pool as ThreadPool
import newspaper
from newspaper.article import Article
from sklearn.neural_network import MLPRegressor  # type: ignore
from tqdm import tqdm
from kindle_news_assistant.safe_open import safe_open
from kindle_news_assistant.word_extractor import article_to_frequency

THREAD_COUNT = 10  # When downloading and parsing articles

dirname = os.path.dirname(__file__)
RELATIVE_PATH = "../userdata/feeds.txt"
absolute_path = os.path.join(dirname, RELATIVE_PATH)


class Agent:
    """A class for fetching articles from the feeds in `feeds.txt`."""

    BatchSize = 20

    def __init__(self, include_old: Optional[bool] = False):
        """Initialize the Agent class.

        :param include_old: Whether to include cached articles, defaults to False
        """
        self.include_old = bool(include_old)

        feeds_file = safe_open(absolute_path, "r")
        content = feeds_file.read()
        feeds_file.close()
        self.feeds = content.split("\n")

    def fetch(self):
        """Fetch the articles from the feeds.

        :return: All of the posts from the articles
        """
        print("Fetching article sources...")
        articles: List[Article] = []
        for feed in tqdm(self.feeds):
            source = newspaper.build(
                feed, memoize_articles=not self.include_old, keep_article_html=True
            )
            if len(source.articles) == 0 and self.include_old:
                tqdm.write(
                    "Warning: The source `" + feed + "` appears to have no articles."
                )
            articles.extend(source.articles)

        # Multi-thread article downloads and parsing
        print("Downloading and parsing articles...")

        def download_and_parse(article: Article):
            try:
                article.download()
                article.parse()
                article.nlp()
            except newspaper.article.ArticleException:
                pass

        pool = ThreadPool(THREAD_COUNT)
        list(tqdm(pool.imap(download_and_parse, articles), total=len(articles)))
        pool.close()
        pool.join()

        print("Removing invalid articles...")
        articles = [
            article
            for article in tqdm(articles)
            if article.is_parsed and article.is_valid_body()
        ]
        return articles

    @staticmethod
    def get_summary_text(article: Article):
        """Extract summary text from an article.

        :param article: The article to extract summary data from
        :return: The article's summary
        """
        return article.summary

    @staticmethod
    @overload
    def filter_by_model(
        articles: List[Article], model: MLPRegressor
    ) -> List[Article]:  # noqa: D102
        ...

    @staticmethod
    @overload
    def filter_by_model(
        articles: List[Article], model: MLPRegressor, include_complement: bool
    ) -> Union[List[Article], Tuple[List[Article], List[Article]]]:  # noqa: D102
        ...

    @staticmethod
    def filter_by_model(
        articles: List[Article],
        model: MLPRegressor,
        include_complement: Optional[bool] = False,
    ) -> Union[List[Article], Tuple[List[Article], List[Article]]]:
        """Filter articles by using the learned classification model.

        :param articles: The articles
        :param model: The learned classification model
        :param include_complement: Whether to include articles that would not be
            recommended, defaults to False
        :return: Articles that were approved by the classification model, in recommended order.
            Will return a tuple with filtered and complement articles if `include_complement`
            flag is set to True.
        """
        frequencies = [
            article_to_frequency(Agent.get_summary_text(article))
            for article in articles
        ]
        ratings = model.predict(frequencies)

        grouped_ratings_and_articles = sorted(
            zip(ratings, articles), reverse=True, key=lambda pair: pair[0]
        )

        if include_complement:
            filtered = []
            complement = []

            for (rating, article) in grouped_ratings_and_articles:
                if rating >= 0.5:
                    filtered.append(article)
                else:
                    complement.append(article)

            return (filtered, complement)

        return [zipped[1] for zipped in grouped_ratings_and_articles]

    def batch(
        self,
        model: Optional[MLPRegressor] = None,
        size: Optional[int] = BatchSize,
    ):
        """Fetch a batch of articles.

        :param model: The learned article classification model
        :param size: The size of the batch, defaults to BatchSize
        :return: A list of articles
        """
        articles = self.fetch()
        if model is not None:
            articles = Agent.filter_by_model(articles, model)
        limited = articles[:size]
        return limited
