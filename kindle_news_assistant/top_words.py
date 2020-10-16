import os
dirname = os.path.dirname(__file__)
relative_path = "../google-10000-english/20k.txt"
absolute_path = os.path.join(dirname, relative_path)
f = open(absolute_path, "r")
content = f.read()
f.close()

"""The top words from the google-10000-english list
"""
words = content.split("\n")