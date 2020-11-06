from skmultiflow.core import BaseSKMObject as BaseSKMObject
from skmultiflow.utils import SlidingWindow as SlidingWindow
from typing import Any

class BaseNeighbors(BaseSKMObject):
    n_neighbors: Any = ...
    max_window_size: Any = ...
    leaf_size: Any = ...
    metric: Any = ...
    data_window: Any = ...
    def __init__(self, n_neighbors: int = ..., max_window_size: int = ..., leaf_size: int = ..., metric: str = ...) -> None: ...
    def reset(self): ...
    @staticmethod
    def valid_metrics(): ...