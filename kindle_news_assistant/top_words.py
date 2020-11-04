"""Export the top words from the google top 10000 words list."""
import os

dirname = os.path.dirname(__file__)
RELATIVE_PATH = "../google-10000-english/20k.txt"
absolute_path = os.path.join(dirname, RELATIVE_PATH)
top_words_file = open(absolute_path, "r")
content = top_words_file.read()
top_words_file.close()

words = content.split("\n")  # The top words from the google-10000-english list
