from abc import ABCMeta, abstractmethod
from typing import Any, Optional

def clone(estimator: Any, safe: bool = ...): ...

class BaseEstimator:
    def get_params(self, deep: bool = ...): ...
    def set_params(self, **params: Any): ...

class BaseSKMObject(BaseEstimator):
    def reset(self) -> None: ...
    def get_info(self): ...

class ClassifierMixin(metaclass=ABCMeta):
    def fit(self, X: Any, y: Any, classes: Optional[Any] = ..., sample_weight: Optional[Any] = ...): ...
    @abstractmethod
    def partial_fit(self, X: Any, y: Any, classes: Optional[Any] = ..., sample_weight: Optional[Any] = ...) -> Any: ...
    @abstractmethod
    def predict(self, X: Any) -> Any: ...
    @abstractmethod
    def predict_proba(self, X: Any) -> Any: ...
    def score(self, X: Any, y: Any, sample_weight: Optional[Any] = ...): ...

class RegressorMixin(metaclass=ABCMeta):
    def fit(self, X: Any, y: Any, sample_weight: Optional[Any] = ...): ...
    @abstractmethod
    def partial_fit(self, X: Any, y: Any, sample_weight: Optional[Any] = ...) -> Any: ...
    @abstractmethod
    def predict(self, X: Any) -> Any: ...
    @abstractmethod
    def predict_proba(self, X: Any) -> Any: ...
    def score(self, X: Any, y: Any, sample_weight: Optional[Any] = ...): ...

class MetaEstimatorMixin: ...
class MultiOutputMixin: ...

def is_classifier(estimator: Any): ...
def is_regressor(estimator: Any): ...
