from . import settings as settings
from typing import Any

ideal: float
stopwords: Any

def load_stopwords(language: Any) -> None: ...
def summarize(url: str = ..., title: str = ..., text: str = ..., max_sents: int = ...): ...
def score(sentences: Any, titleWords: Any, keywords: Any): ...
def sbs(words: Any, keywords: Any): ...
def dbs(words: Any, keywords: Any): ...
def split_words(text: Any): ...
def keywords(text: Any): ...
def split_sentences(text: Any): ...
def length_score(sentence_len: Any): ...
def title_score(title: Any, sentence: Any): ...
def sentence_position(i: Any, size: Any): ...
