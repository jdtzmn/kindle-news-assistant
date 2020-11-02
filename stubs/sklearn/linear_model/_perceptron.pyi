from ._stochastic_gradient import BaseSGDClassifier as BaseSGDClassifier
from typing import Any, Optional

class Perceptron(BaseSGDClassifier):
    def __init__(self, *, penalty: Optional[Any] = ..., alpha: float = ..., fit_intercept: bool = ..., max_iter: int = ..., tol: float = ..., shuffle: bool = ..., verbose: int = ..., eta0: float = ..., n_jobs: Optional[Any] = ..., random_state: int = ..., early_stopping: bool = ..., validation_fraction: float = ..., n_iter_no_change: int = ..., class_weight: Optional[Any] = ..., warm_start: bool = ...) -> None: ...
