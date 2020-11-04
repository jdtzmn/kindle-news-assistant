"""A set of conversion methods for extracing information from article headers."""
from typing import List
from kindle_news_assistant.top_words import words as common_words

FEATURE_LENGTH = 30


def extract_words(article: str) -> List[int]:
    """Extract the most unique words from an article and pad to `feature_length` if necessary.

    :param article: The article or article description
    :return: The most unique words in descending order
    """
    numbered_article = article_to_numbers(article)
    numbered_article.sort(reverse=True)
    padded = numbered_article + [0] * max(0, FEATURE_LENGTH - len(numbered_article))
    return padded[:FEATURE_LENGTH]


def article_to_numbers(article: str) -> List[int]:
    """Convert an article or article description to a list of numbers.

    :param article: The article or article description
    :return: A list of numbers corresponding to the words
    """
    numbers: List[int] = []
    article_words = article.strip(",:.-()'\"?!").lower().split(" ")

    while len(article_words) > 0:
        current_word = article_words.pop(0)

        try:
            word_index = common_words.index(current_word)
            if not word_index in numbers:
                numbers.append(word_index)
        except ValueError:
            continue

    return numbers


def numbers_to_words(numbers: List[int]) -> List[str]:
    """Convert the numbers array back to words.

    :param numbers: A list of numbers
    :return: A list of words
    """
    remaining = numbers[:]
    words: List[str] = []

    while len(remaining) > 0:
        current = remaining.pop(0)
        words.append(common_words[current])

    return words
