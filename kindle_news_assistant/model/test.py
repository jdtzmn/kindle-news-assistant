"""The main method for testing the article classification model."""
from sklearn.neural_network import MLPRegressor  # type:ignore
from kindle_news_assistant.agent import Agent
from kindle_news_assistant.history import History
from kindle_news_assistant.model_storage import load_model


def start_test():
    """Start the assistant model's test."""
    history = History()
    agent = Agent(history)

    perceptron: MLPRegressor = load_model()
    posts = agent.fetch()

    filtered = agent.filter_by_model(posts, perceptron)
    complement = [
        article
        for article in posts
        if not article.title in [post.title for post in filtered]
    ]

    print("Model would not suggest:")
    print([article.title for article in complement])
    print("")
    print("Model would suggest:")
    print([article.title for article in filtered])
