"""The main method for testing the article classification model."""
from sklearn.linear_model import SGDClassifier  # type: ignore
from kindle_news_assistant.agent import Agent
from kindle_news_assistant.history import History
from kindle_news_assistant.model_storage import load_model


def start_test():
    """Start the assistant model's test."""
    history = History()
    agent = Agent(history)

    clf: SGDClassifier = load_model()
    entries = agent.batch(False, clf)

    for entry in entries:
        print(entry.title)
