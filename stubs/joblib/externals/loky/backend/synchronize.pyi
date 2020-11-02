from typing import Any, Optional

class SemLock:
    def __init__(self, kind: Any, value: Any, maxvalue: Any) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args: Any): ...

class Semaphore(SemLock):
    def __init__(self, value: int = ...) -> None: ...
    def get_value(self): ...

class BoundedSemaphore(Semaphore):
    def __init__(self, value: int = ...) -> None: ...

class Lock(SemLock):
    def __init__(self) -> None: ...

class RLock(SemLock):
    def __init__(self) -> None: ...

class Condition:
    def __init__(self, lock: Optional[Any] = ...) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args: Any): ...
    def wait(self, timeout: Optional[Any] = ...): ...
    def notify(self) -> None: ...
    def notify_all(self) -> None: ...
    def wait_for(self, predicate: Any, timeout: Optional[Any] = ...): ...

class Event:
    def __init__(self) -> None: ...
    def is_set(self): ...
    def set(self) -> None: ...
    def clear(self) -> None: ...
    def wait(self, timeout: Optional[Any] = ...): ...
