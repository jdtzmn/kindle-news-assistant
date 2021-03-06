from ebooklib.plugins.base import BasePlugin as BasePlugin
from ebooklib.utils import parse_html_string as parse_html_string
from typing import Any

def tidy_cleanup(content: Any, **extra: Any): ...

class TidyPlugin(BasePlugin):
    NAME: str = ...
    OPTIONS: Any = ...
    options: Any = ...
    def __init__(self, extra: Any = ...) -> None: ...
    def html_before_write(self, book: Any, chapter: Any): ...
    def html_after_read(self, book: Any, chapter: Any): ...
