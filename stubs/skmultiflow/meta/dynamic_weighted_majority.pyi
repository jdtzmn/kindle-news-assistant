from skmultiflow.bayes import NaiveBayes as NaiveBayes
from skmultiflow.core import BaseSKMObject as BaseSKMObject, ClassifierMixin as ClassifierMixin, MetaEstimatorMixin as MetaEstimatorMixin
from typing import Any, Optional

def DynamicWeightedMajority(n_estimators: int = ..., base_estimator: Any = ..., period: int = ..., beta: float = ..., theta: float = ...): ...

class DynamicWeightedMajorityClassifier(BaseSKMObject, ClassifierMixin, MetaEstimatorMixin):
    class WeightedExpert:
        estimator: Any = ...
        weight: Any = ...
        def __init__(self, estimator: Any, weight: Any) -> None: ...
    n_estimators: Any = ...
    base_estimator: Any = ...
    beta: Any = ...
    theta: Any = ...
    period: Any = ...
    epochs: Any = ...
    num_classes: Any = ...
    experts: Any = ...
    def __init__(self, n_estimators: int = ..., base_estimator: Any = ..., period: int = ..., beta: float = ..., theta: float = ...) -> None: ...
    def partial_fit(self, X: Any, y: Any, classes: Optional[Any] = ..., sample_weight: Optional[Any] = ...): ...
    def predict(self, X: Any): ...
    def predict_proba(self, X: Any) -> None: ...
    def fit_single_sample(self, X: Any, y: Any, classes: Optional[Any] = ..., sample_weight: Optional[Any] = ...) -> None: ...
    def get_expert_predictions(self, X: Any): ...
    def reset(self) -> None: ...
