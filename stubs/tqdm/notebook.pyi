from .std import tqdm as std_tqdm
from typing import Any, Optional

class tqdm_notebook(std_tqdm):
    @staticmethod
    def status_printer(_: Any, total: Optional[Any] = ..., desc: Optional[Any] = ..., ncols: Optional[Any] = ...): ...
    @staticmethod
    def format_meter(n: Any, total: Any, *args: Any, **kwargs: Any): ...
    def display(self, msg: Optional[Any] = ..., pos: Optional[Any] = ..., close: bool = ..., bar_style: Optional[Any] = ...) -> None: ...
    @property
    def colour(self): ...
    @colour.setter
    def colour(self, bar_color: Any) -> None: ...
    sp: Any = ...
    ncols: Any = ...
    container: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __iter__(self, *args: Any, **kwargs: Any) -> Any: ...
    def update(self, *args: Any, **kwargs: Any): ...
    def close(self, *args: Any, **kwargs: Any) -> None: ...
    def moveto(self, *_: Any, **__: Any) -> None: ...
    def reset(self, total: Optional[Any] = ...): ...

def tnrange(*args: Any, **kwargs: Any): ...
tqdm = tqdm_notebook
trange = tnrange
