"""The main method for the kindle news assistant application."""

from typing import Optional
import click
from newspaper.utils import get_available_languages
from kindle_news_assistant.model.train import start_training
from kindle_news_assistant.model.test import start_test
from kindle_news_assistant.model.send import send_articles
from kindle_news_assistant.delivery.index import GeneralDeliveryMethod


@click.command()
@click.option("--train", is_flag=True, help="Train the assistant model.")
@click.option(
    "--test", is_flag=True, help="Preview a list compiled by the assistant model."
)
@click.option(
    "--lang",
    type=click.Choice(get_available_languages(), case_sensitive=False),
    help="Ensure retrieved articles are in a given language.",
)
@click.option(
    "--delivery",
    type=click.Choice(GeneralDeliveryMethod.methods, case_sensitive=False),
    help="Set the method for delivering articles.",
)
def run(train: bool, test: bool, lang: Optional[str], delivery: Optional[str]):
    """Start the application.

    :param train: A flag that indicates whether to train the model
    :param test: A flag that indicates whether to test the model
    :param lang: A language argument that is used for article filtration. Will filter articles
        by a given language, if specified
    :param delivery: An argument to set the method for delivering articles
    """
    if train:
        start_training(lang)
    elif test:
        start_test(lang)
    else:
        send_articles(lang, delivery)


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    run()
