from ebooklib.plugins.base import BasePlugin as BasePlugin
from ebooklib.utils import parse_html_string as parse_html_string
from typing import Any

ATTRIBUTES_GLOBAL: Any
DEPRECATED_TAGS: Any

def leave_only(item: Any, tag_list: Any) -> None: ...

class SyntaxPlugin(BasePlugin):
    NAME: str = ...
    def html_before_write(self, book: Any, chapter: Any): ...
