"""The main method for training the article classification model."""
from typing import List
import click
from feedparser.util import FeedParserDict
from sklearn.neural_network import MLPRegressor  # type:ignore
from kindle_news_assistant.word_extractor import article_to_frequency
from kindle_news_assistant.agent import Agent
from kindle_news_assistant.history import History
from kindle_news_assistant.model_storage import model_exists, load_model, store_model

SUMMARY_TEXT_LIMIT = 450  # characters


def start_training() -> None:
    """Start the assistant model's training."""
    history = History()
    agent = Agent(history)
    entries = agent.batch(False)

    (yes, no) = classify_articles(entries, history)  # pylint: disable=invalid-name
    (X, y) = format_for_training(yes, no)  # pylint: disable=invalid-name

    print("Training model...")

    if model_exists():
        perceptron: MLPRegressor = load_model()

        # Log accuracy
        accuracy = calculate_accuracy(yes, no, perceptron)
        print("Accuracy:")
        percentage_str = str(int(accuracy * 100))
        print(percentage_str + "%")

        # Update model
        perceptron.partial_fit(X, y)
    else:
        perceptron = MLPRegressor(
            hidden_layer_sizes=(11, 5),
            solver="sgd",
            max_iter=1000,
        )

        # Fit model
        perceptron.fit(X, y)

    print("Saving model...")
    store_model(perceptron)


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
        position_text = str(index + 1) + " of " + str(len(entries))
        click.echo(click.style(entry.title, bold=True) + " (" + position_text + ")\n")
        summary_text = Agent.get_summary_text(entry)
        truncated_summary = (
            (summary_text[: SUMMARY_TEXT_LIMIT - 3] + "...")
            if len(summary_text) > SUMMARY_TEXT_LIMIT
            else summary_text
        )
        print(truncated_summary)

        would_read = click.confirm(
            click.style("Would you read this article?", fg="green")
        )
        if would_read:
            yes.append(entry)
        else:
            no.append(entry)

        history.append(entry.id)

    return (yes, no)


def format_for_training(
    yes: List[FeedParserDict], no: List[FeedParserDict]
):  # pylint: disable=invalid-name
    """Format the yes/no articles in preparation for training.

    :param yes: The list of articles that the user would read
    :param no: The list of the articles that the user would not read
    :return: A formatted tuple for training the model, formatted as (X, y)
    """
    X: List[List[int]] = []  # pylint: disable=invalid-name
    y: List[int] = []  # 0 or 1 # pylint: disable=invalid-name

    format_helper(yes, 1, X, y)
    format_helper(no, -1, X, y)

    return (X, y)


def format_helper(
    article_list: List[FeedParserDict], output: int, X: List[List[int]], y: List[int]
):  # pylint: disable=invalid-name
    """Help the `format_for_training` method group articles for training.

    :param article_list: A list of feedparser articles
    :param output: The class for this list to be associated with (0 or 1)
        1 is would read and 0 is would not read
    :param X: A list of the input features
    :param y: A list of the output classes
    """
    for article in article_list:
        text_value = article.title + " " + Agent.get_summary_text(article)
        spaced = text_value.replace("\n", " ")
        article_x = article_to_frequency(spaced)
        article_y = output
        X.append(article_x)
        y.append(article_y)


def calculate_accuracy(  # pylint: disable=invalid-name
    yes: List[FeedParserDict],
    no: List[FeedParserDict],
    perceptron: MLPRegressor,
) -> float:
    """Calculate the accuracy of the inputted perceptron model.

    :param yes: The articles which the user liked
    :param no: The articles which the user disliked
    :param perceptron: The perceptron model used for classification
    :return: The accuracy of the current model
    """
    # Predict the "yes" articles using the model
    entries = yes + no
    predicted_correct = Agent.filter_by_model(entries, perceptron)

    # We'll add correct yes articles and subtract incorrect no articles
    correct = len(no)

    for true_yes in yes:
        for predicted_yes in predicted_correct:
            if true_yes.title == predicted_yes.title:
                correct += 1
                continue

    for true_no in no:
        for predicted_yes in predicted_correct:
            if true_no.title == predicted_yes.title:  # Incorrect classification
                correct -= 1
                continue

    return correct / len(entries)
