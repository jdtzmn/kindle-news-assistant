"""Fetch articles from the feeds in `feeds.txt`."""
from typing import List, Optional, Union, Tuple, overload
import os
import random
import feedparser
from feedparser.util import FeedParserDict
from sklearn.neural_network import MLPRegressor  # type: ignore
from bs4 import BeautifulSoup
from tqdm import tqdm
from kindle_news_assistant.safe_open import safe_open
from kindle_news_assistant.history import History
from kindle_news_assistant.word_extractor import article_to_frequency

dirname = os.path.dirname(__file__)
RELATIVE_PATH = "../userdata/feeds.txt"
absolute_path = os.path.join(dirname, RELATIVE_PATH)


class Agent:
    """A class for fetching articles from the feeds in `feeds.txt`."""

    BatchSize = 20

    def __init__(self, history: History):
        """Initialize the Agent class.

        :param history: An instance of the History class
        """
        self.history = history

        feeds_file = safe_open(absolute_path, "r")
        content = feeds_file.read()
        feeds_file.close()
        self.feeds = content.split("\n")

    def fetch(self):
        """Fetch the articles from the feeds.

        :return: All of the posts from the articles
        """
        print("Fetching articles...")
        posts: List[FeedParserDict] = []

        for url in tqdm(self.feeds):
            posts.extend(feedparser.parse(url).entries)

        return posts

    def filter_by_unread(self, posts: List[FeedParserDict]):
        """Filter articles by articles which have not been read.

        :param posts: A list of all of the articles
        :return: A list of the articles that have not been read
        """
        filtered: List[FeedParserDict] = []
        for post in posts:
            if not self.history.contains(post.id):
                filtered.append(post)
        return filtered

    @staticmethod
    def get_summary_text(post: FeedParserDict):
        """Extract summary text from an article.

        :param post: The article to extract summary data from
        :return: The article's summary
        """
        soup = BeautifulSoup(post.summary, "html.parser")
        summary_text = soup.get_text()
        return summary_text

    @staticmethod
    @overload
    def filter_by_model(
        posts: List[FeedParserDict], model: MLPRegressor
    ) -> List[FeedParserDict]:  # noqa: D102
        ...

    @staticmethod
    @overload
    def filter_by_model(
        posts: List[FeedParserDict], model: MLPRegressor, include_complement: bool
    ) -> Union[
        List[FeedParserDict], Tuple[List[FeedParserDict], List[FeedParserDict]]
    ]:  # noqa: D102
        ...

    @staticmethod
    def filter_by_model(
        posts: List[FeedParserDict],
        model: MLPRegressor,
        include_complement: Optional[bool] = False,
    ) -> Union[List[FeedParserDict], Tuple[List[FeedParserDict], List[FeedParserDict]]]:
        """Filter articles by using the learned classification model.

        :param posts: The articles
        :param model: The learned classification model
        :param include_complement: Whether to include articles that would not be
            recommended, defaults to False
        :return: Articles that were approved by the classification model, in recommended order.
            Will return a tuple with filtered and complement articles if `include_complement`
            flag is set to True.
        """
        frequencies = [
            article_to_frequency(Agent.get_summary_text(post)) for post in posts
        ]
        ratings = model.predict(frequencies)

        filtered = []
        complement = []
        for (rating, post) in sorted(
            zip(ratings, posts), reverse=True, key=lambda pair: pair[0]
        ):
            print(rating)
            if rating >= 0:
                filtered.append(post)
            else:
                complement.append(post)

        return (filtered, complement) if include_complement else filtered

    def batch(
        self,
        mark: Optional[bool] = True,
        model: Optional[MLPRegressor] = None,
        size: Optional[int] = BatchSize,
    ):
        """Fetch a batch of articles that are shuffled and filtered by unread.

        :param mark: Whether to mark the batch as read, defaults to True
        :param model: The learned article classification model
        :param size: The size of the batch, defaults to BatchSize
        :return: A list of articles
        """
        posts: List[FeedParserDict] = self.fetch()
        self.history.remove_ids_other_than([post.id for post in posts])
        posts = self.filter_by_unread(posts)
        if model is not None:
            posts = Agent.filter_by_model(posts, model)
        random.shuffle(posts)
        limited = posts[:size]
        if mark:
            self.history.extend([post.id for post in limited])
        return limited
