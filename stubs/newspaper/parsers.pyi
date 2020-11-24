from . import text as text
from typing import Any, Optional

log: Any

class Parser:
    @classmethod
    def xpath_re(cls, node: Any, expression: Any): ...
    @classmethod
    def drop_tag(cls, nodes: Any) -> None: ...
    @classmethod
    def css_select(cls, node: Any, selector: Any): ...
    @classmethod
    def get_unicode_html(cls, html: Any): ...
    @classmethod
    def fromstring(cls, html: Any): ...
    @classmethod
    def clean_article_html(cls, node: Any): ...
    @classmethod
    def nodeToString(cls, node: Any): ...
    @classmethod
    def replaceTag(cls, node: Any, tag: Any) -> None: ...
    @classmethod
    def stripTags(cls, node: Any, *tags: Any) -> None: ...
    @classmethod
    def getElementById(cls, node: Any, idd: Any): ...
    @classmethod
    def getElementsByTag(cls: Any, node: Any, tag: Any=..., attr: Any=..., value: Any=..., childs: Any=..., use_regex: Any=...) -> list: ...
    @classmethod
    def appendChild(cls, node: Any, child: Any) -> None: ...
    @classmethod
    def childNodes(cls, node: Any): ...
    @classmethod
    def childNodesWithText(cls, node: Any): ...
    @classmethod
    def textToPara(cls, text: Any): ...
    @classmethod
    def getChildren(cls, node: Any): ...
    @classmethod
    def getElementsByTags(cls, node: Any, tags: Any): ...
    @classmethod
    def createElement(cls, tag: str = ..., text: Optional[Any] = ..., tail: Optional[Any] = ...): ...
    @classmethod
    def getComments(cls, node: Any): ...
    @classmethod
    def getParent(cls, node: Any): ...
    @classmethod
    def remove(cls, node: Any) -> None: ...
    @classmethod
    def getTag(cls, node: Any): ...
    @classmethod
    def getText(cls, node: Any): ...
    @classmethod
    def previousSiblings(cls, node: Any): ...
    @classmethod
    def previousSibling(cls, node: Any): ...
    @classmethod
    def nextSibling(cls, node: Any): ...
    @classmethod
    def isTextNode(cls, node: Any): ...
    @classmethod
    def getAttribute(cls, node: Any, attr: Optional[Any] = ...): ...
    @classmethod
    def delAttribute(cls, node: Any, attr: Optional[Any] = ...) -> None: ...
    @classmethod
    def setAttribute(cls, node: Any, attr: Optional[Any] = ..., value: Optional[Any] = ...) -> None: ...
    @classmethod
    def outerHtml(cls, node: Any): ...
