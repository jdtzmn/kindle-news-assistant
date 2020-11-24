import logging
from .api import build as build, build_article as build_article, fulltext as fulltext, hot as hot, languages as languages, popular_urls as popular_urls
from .article import Article as Article, ArticleException as ArticleException
from .source import Source as Source
from typing import Any

news_pool: Any

class NullHandler(logging.Handler):
    def emit(self, record: Any) -> None: ...
