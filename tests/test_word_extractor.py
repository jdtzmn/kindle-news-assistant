import pytest
from kindle_news_assistant.word_extractor import article_to_frequency, numbers_to_words


@pytest.fixture
def example_article():
    return """post solve option moral growth
    cousin moral disappoint mole payment moral harmony 
    exile permission nomination driver experience 
    genuine broadcast parachute temple relative nomination"""


@pytest.fixture
def expected_frequency():
    return [
        136,
        538,
        565,
        1312,
        1697,
        2023,
        2926,
        3855,
        4337,
        4903,
        4952,
        5017,
        7423,
        9153,
        11132,
        14378,
        16327,
    ]


@pytest.fixture
def expected_words():
    return [
        "post",
        "payment",
        "experience",
        "option",
        "driver",
        "permission",
        "relative",
        "broadcast",
        "temple",
        "moral",
        "solve",
        "genuine",
        "harmony",
        "nomination",
        "cousin",
        "exile",
        "mole",
    ]


def test_article_to_frequency(example_article, expected_frequency):
    word_frequency = article_to_frequency(example_article)
    filtered = [index for (index, value) in enumerate(word_frequency) if not value == 0]

    assert filtered == expected_frequency


def test_numbers_to_words(example_article, expected_words):
    word_frequency = article_to_frequency(example_article)
    words = numbers_to_words(word_frequency)
    assert words == expected_words
