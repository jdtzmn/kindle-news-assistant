from .configuration import Configuration as Configuration
from threading import Thread
from typing import Any, Optional

log: Any

class ConcurrencyException(Exception): ...

class Worker(Thread):
    tasks: Any = ...
    timeout: Any = ...
    daemon: bool = ...
    def __init__(self, tasks: Any, timeout_seconds: Any) -> None: ...
    def run(self) -> None: ...

class ThreadPool:
    tasks: Any = ...
    def __init__(self, num_threads: Any, timeout_seconds: Any) -> None: ...
    def add_task(self, func: Any, *args: Any, **kargs: Any) -> None: ...
    def wait_completion(self) -> None: ...

class NewsPool:
    pool: Any = ...
    config: Any = ...
    def __init__(self, config: Optional[Any] = ...) -> None: ...
    def join(self) -> None: ...
    def set(self, news_list: Any, threads_per_source: int = ..., override_threads: Optional[Any] = ...) -> None: ...