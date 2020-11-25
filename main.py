"""The main method for the kindle news assistant application."""

from typing import Optional
import click
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
    "--delivery", type=click.Choice(GeneralDeliveryMethod.methods, case_sensitive=False)
)
def run(train: bool, test: bool, delivery: Optional[str]):
    """Start the application.

    :param train: A flag that indicates whether to train the model
    :param test: A flag that indicates whether to test the model
    :type test: bool
    """
    if train:
        start_training()
    elif test:
        start_test()
    else:
        send_articles(delivery)


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    run()
