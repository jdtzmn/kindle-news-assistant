from typing import Any

class JoblibException(Exception):
    def __init__(self, *args: Any) -> None: ...

class TransportableException(JoblibException):
    message: Any = ...
    etype: Any = ...
    def __init__(self, message: Any, etype: Any) -> None: ...
    def unwrap(self, context_message: str = ...): ...
