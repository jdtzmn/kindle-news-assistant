"""The main method for testing the article classification model."""
from typing import Optional, cast, Tuple, List
from sklearn.neural_network import MLPRegressor  # type:ignore
from newspaper.article import Article
from kindle_news_assistant.agent import Agent
from kindle_news_assistant.model_storage import load_model


def start_test(language: Optional[str], thread_count: Optional[int]):
    """Start the assistant model's test.

    :param language: The language to filter articles by
    :param thread_count: The number of threads to use during article retrieval.
    """
    agent = Agent(True, thread_count)

    articles = agent.fetch()

    # Filter and download articles
    perceptron: MLPRegressor = load_model()
    (filtered, complement) = cast(
        Tuple[List[Article], List[Article]],
        agent.filter_by_model(articles, perceptron, language, True),
    )
    agent.download(filtered)
    agent.download(complement)

    print("Model would not suggest: " + str(len(complement)))
    print([article.title for article in complement])
    print("")
    print("Model would suggest: " + str(len(filtered)))
    print([article.title for article in filtered])
