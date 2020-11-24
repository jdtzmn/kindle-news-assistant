from .configuration import Configuration as Configuration
from .mthreading import ThreadPool as ThreadPool
from .settings import cj as cj  # type: ignore
from typing import Any, Optional

log: Any
FAIL_ENCODING: str


def get_request_kwargs(timeout: Any, useragent: Any, proxies: Any, headers: Any):
    ...


def get_html(url: Any, config: Optional[Any] = ..., response: Optional[Any] = ...):
    ...


def get_html_2XX_only(
    url: Any, config: Optional[Any] = ..., response: Optional[Any] = ...
):
    ...


class MRequest:
    url: Any = ...
    config: Any = ...
    useragent: Any = ...
    timeout: Any = ...
    proxies: Any = ...
    headers: Any = ...
    resp: Any = ...

    def __init__(self, url: Any, config: Optional[Any] = ...) -> None:
        ...

    def send(self) -> None:
        ...


def multithread_request(urls: Any, config: Optional[Any] = ...):
    ...
