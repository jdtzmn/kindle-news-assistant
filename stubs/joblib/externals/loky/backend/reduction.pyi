from typing import Any, Optional

class _ReducerRegistry:
    dispatch_table: Any = ...
    @classmethod
    def register(cls, type: Any, reduce_func: Any) -> None: ...

register: Any

class _C:
    def f(self) -> None: ...
    @classmethod
    def h(cls) -> None: ...

def set_loky_pickler(loky_pickler: Optional[Any] = ...) -> None: ...
def loads(buf: Any): ...
def dump(obj: Any, file: Any, reducers: Optional[Any] = ..., protocol: Optional[Any] = ...) -> None: ...
def dumps(obj: Any, reducers: Optional[Any] = ..., protocol: Optional[Any] = ...): ...
