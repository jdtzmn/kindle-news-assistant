from ._memmapping_reducer import TemporaryResourcesManager as TemporaryResourcesManager, get_memmapping_reducers as get_memmapping_reducers
from .externals.loky.reusable_executor import _ReusablePoolExecutor
from typing import Any, Optional

def get_memmapping_executor(n_jobs: Any, **kwargs: Any): ...

class MemmappingExecutor(_ReusablePoolExecutor):
    @classmethod
    def get_memmapping_executor(cls, n_jobs: Any, timeout: int = ..., initializer: Optional[Any] = ..., initargs: Any = ..., env: Optional[Any] = ..., temp_folder: Optional[Any] = ..., context_id: Optional[Any] = ..., **backend_args: Any): ...
    def terminate(self, kill_workers: bool = ...) -> None: ...

class _TestingMemmappingExecutor(MemmappingExecutor):
    def apply_async(self, func: Any, args: Any): ...
    def map(self, f: Any, *args: Any): ... # type: ignore # type: ignore
