from kindle_news_assistant.top_words import words as common_words

feature_length = 30

def extract_words(article):
  """Extract the most unique words from an article and pad to `feature_length` if necessary

  :param article: The article or article description
  :type article: string
  :return: The most unique words in descending order
  :rtype: int[]
  """
  numbered_article = article_to_numbers(article)
  numbered_article.sort(reverse = True)
  padded = numbered_article + [0] * max(0, feature_length - len(numbered_article))
  return padded[:feature_length]

def article_to_numbers(article):
  """Convert an article or article description to a list of numbers

  :param article: The article or article description
  :type article: string
  :return: A list of numbers corresponding to the words
  :rtype: int[]
  """

  numbers = []
  article_words = article.strip(',:.-()\'"?!').lower().split(" ")

  while len(article_words) > 0:
    current_word = article_words.pop(0)

    try:
      word_index = common_words.index(current_word)
      if not word_index in numbers:
        numbers.append(word_index)
    except ValueError:
      continue

  return numbers

def numbers_to_words(numbers):
  """Convert the numbers array back to words

  :param numbers: A list of numbers
  :type numbers: int[]
  :return: A list of words
  :rtype: string[]
  """
  remaining = numbers[:]
  words = []
  
  while len(remaining) > 0:
    current = remaining.pop(0)
    words.append(common_words[current])

  return words