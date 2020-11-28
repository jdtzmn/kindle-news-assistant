"""The main method for filtering and delivering articles."""
from typing import Optional
from sklearn.neural_network import MLPRegressor  # type:ignore
from kindle_news_assistant.agent import Agent
from kindle_news_assistant.model_storage import load_model
from kindle_news_assistant.publisher.construct_book import construct_book_from
from kindle_news_assistant.delivery.index import GeneralDeliveryMethod


def send_articles(language: Optional[str], method: Optional[str]):
    """Retrieve, filter, and send articles to the user.

    :param language: The language to filter articles by
    :param method: The method flag set through a command line interface argument
    """
    agent = Agent()

    perceptron: MLPRegressor = load_model()
    filtered = agent.batch(perceptron, None, language)
    agent.download(filtered)

    print("The following articles were selected for delivery:")
    print([article.title for article in filtered])

    print("Constructing epub issue...")
    book_path = construct_book_from(filtered)

    print("Delivering news issue...")
    delivery_method = GeneralDeliveryMethod(method)
    delivery_method.deliver_issue(book_path)

    print("Issue has been successfully delivered.")
