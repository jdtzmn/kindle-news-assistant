from skmultiflow.core import BaseSKMObject as BaseSKMObject, ClassifierMixin as ClassifierMixin, MetaEstimatorMixin as MetaEstimatorMixin
from typing import Any, Optional

def LearnNSE(base_estimator: Any = ..., window_size: int = ..., slope: float = ..., crossing_point: int = ..., n_estimators: int = ..., pruning: Optional[Any] = ...): ...

class LearnPPNSEClassifier(BaseSKMObject, ClassifierMixin, MetaEstimatorMixin):
    ensemble: Any = ...
    ensemble_weights: Any = ...
    bkts: Any = ...
    wkts: Any = ...
    buffer: Any = ...
    window_size: Any = ...
    slope: Any = ...
    crossing_point: Any = ...
    n_estimators: Any = ...
    pruning: Any = ...
    X_batch: Any = ...
    y_batch: Any = ...
    instance_weights: Any = ...
    base_estimator: Any = ...
    classes: Any = ...
    def __init__(self, base_estimator: Any = ..., window_size: int = ..., slope: float = ..., crossing_point: int = ..., n_estimators: int = ..., pruning: Optional[Any] = ...) -> None: ...
    def partial_fit(self, X: Any, y: Optional[Any] = ..., classes: Optional[Any] = ..., sample_weight: Optional[Any] = ...): ...
    def predict_proba(self, X: Any): ...
    def predict(self, X: Any): ...
    def reset(self) -> None: ...