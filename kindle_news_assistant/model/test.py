"""The main method for testing the article classification model."""
from typing import Optional, cast, Tuple, List
from sklearn.neural_network import MLPRegressor  # type:ignore
from newspaper.article import Article
from kindle_news_assistant.agent import Agent
from kindle_news_assistant.model_storage import load_model


def start_test(language: Optional[str]):
    """Start the assistant model's test.

    :param language: The language to filter articles by
    """
    agent = Agent(True)

    perceptron: MLPRegressor = load_model()
    articles = agent.fetch()

    # Filter and download articles
    (filtered, complement) = cast(
        Tuple[List[Article], List[Article]],
        Agent.filter_by_model(articles, perceptron, language, True),
    )
    agent.download(filtered)
    agent.download(complement)

    print("Model would not suggest: " + str(len(complement)))
    print([article.title for article in complement])
    print("")
    print("Model would suggest: " + str(len(filtered)))
    print([article.title for article in filtered])
