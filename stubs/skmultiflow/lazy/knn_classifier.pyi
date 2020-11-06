from skmultiflow.utils.utils import *
from skmultiflow.core import ClassifierMixin as ClassifierMixin
from skmultiflow.lazy.base_neighbors import BaseNeighbors as BaseNeighbors
from typing import Any, Optional

def KNN(n_neighbors: int = ..., max_window_size: int = ..., leaf_size: int = ...): ...

class KNNClassifier(BaseNeighbors, ClassifierMixin):
    classes: Any = ...
    def __init__(self, n_neighbors: int = ..., max_window_size: int = ..., leaf_size: int = ..., metric: str = ...) -> None: ...
    def partial_fit(self, X: Any, y: Any, classes: Optional[Any] = ..., sample_weight: Optional[Any] = ...): ...
    def predict(self, X: Any): ...
    def predict_proba(self, X: Any): ...
