from ._memmapping_reducer import TemporaryResourcesManager as TemporaryResourcesManager, get_memmapping_reducers as get_memmapping_reducers
from ._multiprocessing_helpers import assert_spawning as assert_spawning, mp as mp # type: ignore
from multiprocessing.pool import Pool
from pickle import Pickler
from typing import Any, Optional

WindowsError: Any

class CustomizablePickler(Pickler):
    dispatch: Any = ...
    dispatch_table: Any = ...
    def __init__(self, writer: Any, reducers: Optional[Any] = ..., protocol: Any = ...) -> None: ...
    def register(self, type: Any, reduce_func: Any) -> None: ...

class CustomizablePicklingQueue:
    def __init__(self, context: Any, reducers: Optional[Any] = ...) -> None: ...
    def empty(self): ...

class PicklingPool(Pool):
    def __init__(self, processes: Optional[Any] = ..., forward_reducers: Optional[Any] = ..., backward_reducers: Optional[Any] = ..., **kwargs: Any) -> None: ...

class MemmappingPool(PicklingPool):
    def __init__(self, processes: Optional[Any] = ..., temp_folder: Optional[Any] = ..., max_nbytes: float = ..., mmap_mode: str = ..., forward_reducers: Optional[Any] = ..., backward_reducers: Optional[Any] = ..., verbose: int = ..., context_id: Optional[Any] = ..., prewarm: bool = ..., **kwargs: Any) -> None: ...
    def terminate(self) -> None: ...
