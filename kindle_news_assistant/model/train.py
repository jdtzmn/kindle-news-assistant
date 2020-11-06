"""The main method for training the article classification model."""
from typing import List
import click
from bs4 import BeautifulSoup
from feedparser.util import FeedParserDict
from sklearn.linear_model import SGDClassifier  # type: ignore
from kindle_news_assistant.word_extractor import article_to_frequency
from kindle_news_assistant.agent import Agent
from kindle_news_assistant.history import History
from kindle_news_assistant.model_storage import model_exists, load_model, store_model


def start_training() -> None:
    """Start the assistant model's training."""
    history = History()
    agent = Agent(history)
    entries = agent.batch(False)

    (yes, no) = classify_articles(entries, history)  # pylint: disable=invalid-name
    (X, y) = format_for_training(yes, no)  # pylint: disable=invalid-name

    if model_exists():  # model exists
        clf: SGDClassifier = load_model()
        clf.partial_fit(X, y)
        store_model(clf)
    else:
        clf = SGDClassifier()
        clf.fit(X, y)
        store_model(clf)


def classify_articles(entries: List[FeedParserDict], history: History):
    """Run the user through a number of yes/no choices to determine which articles they would read.

    :param entries: The articles being classified
    :param history: The history class instance
    :return: A yes, no tuple of entries that were labelled yes and entries that were labelled no
    """
    yes: List[FeedParserDict] = []
    no: List[FeedParserDict] = []  # pylint: disable=invalid-name

    for (index, entry) in enumerate(entries):
        click.clear()
        position_text = str(index + 1) + " of " + str(Agent.BatchSize)
        click.echo(click.style(entry.title, bold=True) + " (" + position_text + ")\n")
        soup = BeautifulSoup(entry.summary, "html.parser")
        summary_text = soup.get_text()
        print(summary_text + "\n")

        would_read = click.confirm(
            click.style("Would you read this article?", fg="green")
        )
        if would_read:
            yes.append(entry)
        else:
            no.append(entry)

        history.append(entry.id)

    return (yes, no)


def format_for_training(yes, no):  # pylint: disable=invalid-name
    """Format the yes/no articles in preparation for training.

    :param yes: The list of articles that the user would read
    :param no: The list of the articles that the user would not read
    """
    X: List[int] = []  # pylint: disable=invalid-name
    y: List[int] = []  # 0 or 1 # pylint: disable=invalid-name

    format_helper(yes, 1, X, y)
    format_helper(no, 0, X, y)

    return (X, y)


def format_helper(article_list, output: int, X, y):  # pylint: disable=invalid-name
    """Help the `format_for_training` method group articles for training.

    :param list: The yes/no list
    :param output: The class for this list to be associated with (0 or 1)
    :param X: A list of the input features
    :param y: A list of the output classes
    """
    for article in article_list:
        soup = BeautifulSoup(article.summary, "html.parser")
        text_value = soup.get_text()
        spaced = text_value.replace("\n", " ")
        article_x = article_to_frequency(spaced)
        article_y = output
        X.append(article_x)
        y.append(article_y)
