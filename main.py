"""The main method for the kindle news assistant application."""

import click
from kindle_news_assistant.model.train import start_training
from kindle_news_assistant.model.test import start_test
from kindle_news_assistant.model.send import send_articles


@click.command()
@click.option("--train", is_flag=True, help="Train the assistant model.")
@click.option(
    "--test", is_flag=True, help="Preview a list compiled by the assistant model."
)
def run(train: bool, test: bool):
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
        send_articles()


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    run()
