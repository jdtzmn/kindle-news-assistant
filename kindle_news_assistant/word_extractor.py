"""A set of conversion methods for extracing information from article headers."""
from typing import List
from kindle_news_assistant.top_words import words as common_words


def article_to_frequency(article: str) -> List[int]:
    """Convert an article or article description to a list of numbers.

    :param article: The article or article description
    :return: A list of numbers corresponding to the words
    """
    numbers: List[int] = [0] * len(common_words)
    article_words = article.strip(",:.-()'\"?!").lower().split(" ")

    while len(article_words) > 0:
        current_word = article_words.pop(0)

        try:
            word_index = common_words.index(current_word)
            numbers[word_index] += 1
        except ValueError:
            continue

    return numbers


def numbers_to_words(frequency: List[int]) -> List[str]:
    """Convert the numbers array back to words.

    This is intended to only be used for testing/debugging.

    :param frequency: A list of frequencies of words.
        An index in the array is the index of the word in the google top words list
    :return: A list of words
    """
    filtered = [index for (index, value) in enumerate(frequency) if not value == 0]
    words: List[str] = []

    while len(filtered) > 0:
        current = filtered.pop(0)
        words.append(common_words[current])

    return words
