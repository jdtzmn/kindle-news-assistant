from skmultiflow.metrics import *
from skmultiflow.core import BaseSKMObject as BaseSKMObject, ClassifierMixin as ClassifierMixin, MetaEstimatorMixin as MetaEstimatorMixin, MultiOutputMixin as MultiOutputMixin
from typing import Any, Optional

class MultiOutputLearner(BaseSKMObject, ClassifierMixin, MetaEstimatorMixin, MultiOutputMixin):
    base_estimator: Any = ...
    ensemble: Any = ...
    n_targets: Any = ...
    def __init__(self, base_estimator: Any = ...) -> None: ...
    def fit(self, X: Any, y: Any, classes: Optional[Any] = ..., sample_weight: Optional[Any] = ...): ...
    def partial_fit(self, X: Any, y: Any, classes: Optional[Any] = ..., sample_weight: Optional[Any] = ...): ...
    def predict(self, X: Any): ...
    def predict_proba(self, X: Any): ...
    def reset(self) -> None: ...