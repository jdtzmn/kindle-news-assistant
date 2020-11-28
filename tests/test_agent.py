import pytest
from typing import List
from newspaper.article import Article
from kindle_news_assistant.agent import Agent


@pytest.fixture
def agent():
    return Agent()


@pytest.mark.parametrize(
    "articles,expected_len",
    [
        (
            [
                Article("https://cnn.com/0/16/article-title.html", "https://cnn.com"),
                Article(
                    "https://cnn.com/0/16/article-title.html?query=yes",
                    "https://cnn.com",
                ),
                Article("https://cnn.com/1/16/different-title.html", "https://cnn.com"),
            ],
            2,
        ),
    ],
)
def test_filter_duplicates(agent: Agent, articles: List[Article], expected_len: int):
    filtered = agent.filter_duplicates(articles)
    assert len(filtered) == expected_len


def test_assertion_error_if_invalid_language(agent: Agent):
    articles: List[Article] = []
    language = "zy"
    with pytest.raises(AssertionError):
        agent.filter_by_language(articles, language)
