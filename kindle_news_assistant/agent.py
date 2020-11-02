from typing import List, Optional
from feedparser.util import FeedParserDict
from kindle_news_assistant.word_extractor import extract_words
from sklearn.linear_model import SGDClassifier # type: ignore
import os
import random
import feedparser
from bs4 import BeautifulSoup

dirname = os.path.dirname(__file__)
relative_path = "../userdata/feeds.txt"
absolute_path = os.path.join(dirname, relative_path)


class Agent:
  """ A class for fetching articles from the feeds in `feeds.txt`
  """
  
  BatchSize = 20

  def __init__(self, history):
    self.history = history
    
    f = open(absolute_path, "r")
    content = f.read()
    f.close()
    self.feeds = content.split("\n")

  def fetch(self):
    """Fetch the articles from the feeds

    :return: All of the posts from the articles
    """
    posts: List[FeedParserDict] = []
    for url in self.feeds:
      posts.extend(feedparser.parse(url).entries)

    return posts

  def filter_by_unread(self, posts: List[FeedParserDict]):
    """Filter articles by articles which have not been read

    :param posts: A list of all of the articles
    :return: A list of the articles that have not been read
    """
    filtered: List[FeedParserDict] = []
    for post in posts:
      if not self.history.contains(post.id):
        filtered.append(post)
    return filtered

  def filter_by_model(self, posts: List[FeedParserDict], model):
    filtered = []
    for post in posts:
      soup = BeautifulSoup(post.summary, 'html.parser')
      summary_text = soup.get_text()
      rating = model.predict([extract_words(summary_text)])[0]
      if rating == 1:
        filtered.append(post)
    return filtered

  def batch(self, mark: Optional[bool] = True, model: Optional[SGDClassifier] = None, size: Optional[int] = BatchSize):
    """Fetch a batch of articles that are shuffled and filtered by unread

    :param mark: Whether to mark the batch as read, defaults to True
    :param size: The size of the batch, defaults to BatchSize
    :type size: int, optional
    :return: A list of articles
    """
    posts: List[FeedParserDict] = self.fetch()
    self.history.remove_ids_other_than([post.id for post in posts])
    posts = self.filter_by_unread(posts)
    if model is not None:
      posts = self.filter_by_model(posts , model)
    random.shuffle(posts)
    limited = posts[:size]
    if mark:
      self.history.extend([post.id for post in limited])
    return limited

