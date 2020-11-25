from ebooklib.plugins.base import BasePlugin as BasePlugin
from ebooklib.utils import parse_html_string as parse_html_string
from typing import Any

class BooktypeLinks(BasePlugin):
    NAME: str = ...
    booktype_book: Any = ...
    def __init__(self, booktype_book: Any) -> None: ...
    def html_before_write(self, book: Any, chapter: Any) -> None: ...

class BooktypeFootnotes(BasePlugin):
    NAME: str = ...
    booktype_book: Any = ...
    def __init__(self, booktype_book: Any) -> None: ...
    def html_before_write(self, book: Any, chapter: Any) -> None: ...