import os
from typing import List
import click
from bs4 import BeautifulSoup
from feedparser.util import FeedParserDict
from kindle_news_assistant.word_extractor import extract_words
from kindle_news_assistant.agent import Agent
from kindle_news_assistant.history import History
from kindle_news_assistant.word_extractor import extract_words
from sklearn.linear_model import SGDClassifier # type: ignore
from joblib import dump, load

dirname = os.path.dirname(__file__)
relative_path = "../../userdata/model.joblib"
absolute_path = os.path.join(dirname, relative_path)

def start_training() -> None:
  """Start the assistant model's training
  """
  history = History()
  agent = Agent(history)
  entries = agent.batch(False)

  (yes, no) = classify_articles(entries, history)
  (X, y) = format_for_training(yes, no)
  
  if os.path.isfile(absolute_path): # model exists
    clf: SGDClassifier = load(absolute_path)
    clf.partial_fit(X, y)
    dump(clf, absolute_path)
  else:
    clf = SGDClassifier()
    clf.fit(X, y)
    dump(clf, absolute_path)

def classify_articles(entries: List[FeedParserDict], history: History):
  """Run the user through a number of yes/no choices to determine which articles they would read

  :param entries: The articles being classified
  :param history: The history class instance
  :return: A yes, no tuple of entries that were labelled yes and entries that were labelled no
  """
  yes: List[FeedParserDict] = []
  no: List[FeedParserDict] = []

  for (index, entry) in enumerate(entries):
    click.clear()
    position_text = str(index + 1) + " of " + str(Agent.BatchSize)
    click.echo(click.style(entry.title, bold=True) + " (" + position_text + ")\n")
    soup = BeautifulSoup(entry.summary, 'html.parser')
    summary_text = soup.get_text()
    print(summary_text + "\n")

    would_read = click.confirm(click.style("Would you read this article?", fg='green'))
    if would_read:
      yes.append(entry)
    else:
      no.append(entry)

    history.append(entry.id)

  return (yes, no)

def format_for_training(yes, no):
  """Format the yes/no articles in preparation for training

  :param yes: The list of articles that the user would read
  :param no: The list of the articles that the user would not read
  """
  X: List[int] = []
  y: List[int] = [] # 0 or 1

  format_helper(yes, 1, X, y)
  format_helper(no, 0, X, y)

  return (X, y)

def format_helper(list, output: int, X, y):
  """A helper for the `format_for_training` method

  :param list: The yes/no list
  :param output: The class for this list to be associated with (0 or 1)
  :param X: A list of the input features
  :param y: A list of the output classes
  """
  for article in list:
    soup = BeautifulSoup(article.summary, 'html.parser')
    text_value = soup.get_text()
    spaced = text_value.replace("\n", " ")
    article_X = extract_words(spaced)
    article_y = output
    X.append(article_X)
    y.append(article_y)