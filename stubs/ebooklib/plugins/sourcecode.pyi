from ebooklib.plugins.base import BasePlugin as BasePlugin
from ebooklib.utils import parse_html_string as parse_html_string
from typing import Any

class SourceHighlighter(BasePlugin):
    def __init__(self) -> None: ...
    def html_before_write(self, book: Any, chapter: Any) -> None: ...
