from typing import Any

class ResourceTracker:
    def __init__(self) -> None: ...
    def getfd(self): ...
    def ensure_running(self) -> None: ...
    def register(self, name: Any, rtype: Any) -> None: ...
    def unregister(self, name: Any, rtype: Any) -> None: ...
    def maybe_unlink(self, name: Any, rtype: Any) -> None: ...

ensure_running: Any
register: Any
unregister: Any
