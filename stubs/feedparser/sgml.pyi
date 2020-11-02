import sgmllib as sgmllib
from typing import Any

charref: Any
tagfind: Any
attrfind: Any
entityref: Any
incomplete: Any
interesting: Any
shorttag: Any
shorttagopen: Any
starttagopen: Any

class _EndBracketRegEx:
    endbracket: Any = ...
    def __init__(self) -> None: ...
    def search(self, target: Any, index: int = ...): ...

class EndBracketMatch:
    match: Any = ...
    def __init__(self, match: Any) -> None: ...
    def start(self, n: Any): ...

endbracket: Any
