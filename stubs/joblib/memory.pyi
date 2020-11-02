from . import hashing as hashing
from ._store_backends import FileSystemStoreBackend as FileSystemStoreBackend, StoreBackendBase as StoreBackendBase
from .func_inspect import filter_args as filter_args, format_call as format_call, format_signature as format_signature, get_func_code as get_func_code, get_func_name as get_func_name
from .logger import Logger as Logger, format_time as format_time, pformat as pformat
from typing import Any, Optional

FIRST_LINE_TEXT: str

def extract_first_line(func_code: Any): ...

class JobLibCollisionWarning(UserWarning): ...

def register_store_backend(backend_name: Any, backend: Any) -> None: ...

class MemorizedResult(Logger):
    func_id: Any = ...
    func: Any = ...
    args_id: Any = ...
    store_backend: Any = ...
    mmap_mode: Any = ...
    metadata: Any = ...
    duration: Any = ...
    verbose: Any = ...
    timestamp: Any = ...
    def __init__(self, location: Any, func: Any, args_id: Any, backend: str = ..., mmap_mode: Optional[Any] = ..., verbose: int = ..., timestamp: Optional[Any] = ..., metadata: Optional[Any] = ...) -> None: ...
    @property
    def argument_hash(self): ...
    def get(self): ...
    def clear(self) -> None: ...

class NotMemorizedResult:
    value: Any = ...
    valid: bool = ...
    def __init__(self, value: Any) -> None: ...
    def get(self): ...
    def clear(self) -> None: ...

class NotMemorizedFunc:
    func: Any = ...
    def __init__(self, func: Any) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any): ...
    def call_and_shelve(self, *args: Any, **kwargs: Any): ...
    def clear(self, warn: bool = ...) -> None: ...

class MemorizedFunc(Logger):
    mmap_mode: Any = ...
    compress: Any = ...
    func: Any = ...
    ignore: Any = ...
    store_backend: Any = ...
    timestamp: Any = ...
    __doc__: Any = ...
    def __init__(self, func: Any, location: Any, backend: str = ..., ignore: Optional[Any] = ..., mmap_mode: Optional[Any] = ..., compress: bool = ..., verbose: int = ..., timestamp: Optional[Any] = ...) -> None: ...
    @property
    def func_code_info(self): ...
    def call_and_shelve(self, *args: Any, **kwargs: Any): ...
    def __call__(self, *args: Any, **kwargs: Any): ...
    def clear(self, warn: bool = ...) -> None: ...
    def call(self, *args: Any, **kwargs: Any): ...

class Memory(Logger):
    mmap_mode: Any = ...
    timestamp: Any = ...
    bytes_limit: Any = ...
    backend: Any = ...
    compress: Any = ...
    backend_options: Any = ...
    location: Any = ...
    store_backend: Any = ...
    def __init__(self, location: Optional[Any] = ..., backend: str = ..., cachedir: Optional[Any] = ..., mmap_mode: Optional[Any] = ..., compress: bool = ..., verbose: int = ..., bytes_limit: Optional[Any] = ..., backend_options: Optional[Any] = ...) -> None: ...
    @property
    def cachedir(self): ...
    def cache(self, func: Optional[Any] = ..., ignore: Optional[Any] = ..., verbose: Optional[Any] = ..., mmap_mode: bool = ...): ...
    def clear(self, warn: bool = ...) -> None: ...
    def reduce_size(self) -> None: ...
    def eval(self, func: Any, *args: Any, **kwargs: Any): ...
