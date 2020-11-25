"""The main method for filtering and delivering articles."""
from typing import Optional
from sklearn.neural_network import MLPRegressor  # type:ignore
from kindle_news_assistant.agent import Agent
from kindle_news_assistant.model_storage import load_model
from kindle_news_assistant.publisher.construct_book import construct_book_from
from kindle_news_assistant.delivery.index import GeneralDeliveryMethod

DELIVERY_SIZE = 10  # Number of articles to deliver


def send_articles(method: Optional[str]):
    """Retrieve, filter, and send articles to the user.

    :param method: The method flag set through a command line interface argument
    """
    agent = Agent()

    perceptron: MLPRegressor = load_model()
    articles = agent.fetch()

    print("Filtering articles...")
    filtered = Agent.filter_by_model(articles, perceptron)
    limited = filtered[:DELIVERY_SIZE]

    print("The following articles were selected for delivery:")
    print([article.title for article in limited])

    print("Constructing epub issue...")
    book_path = construct_book_from(limited)

    print("Delivering news issue...")
    delivery_method = GeneralDeliveryMethod(method)
    delivery_method.deliver_issue(book_path)

    print("Issue has been successfully delivered.")
