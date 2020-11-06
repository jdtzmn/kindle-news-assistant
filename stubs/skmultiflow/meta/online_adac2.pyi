from skmultiflow.utils.utils import *
from skmultiflow.core import BaseSKMObject as BaseSKMObject, ClassifierMixin as ClassifierMixin, MetaEstimatorMixin as MetaEstimatorMixin
from skmultiflow.drift_detection import ADWIN as ADWIN
from skmultiflow.lazy import KNNADWINClassifier as KNNADWINClassifier
from skmultiflow.utils import check_random_state as check_random_state
from typing import Any, Optional

def OnlineAdaC2(base_estimator: Any = ..., n_estimators: int = ..., cost_positive: int = ..., cost_negative: float = ..., drift_detection: bool = ..., random_state: Optional[Any] = ...): ...

class OnlineAdaC2Classifier(BaseSKMObject, ClassifierMixin, MetaEstimatorMixin):
    n_estimators: Any = ...
    random_state: Any = ...
    cost_positive: Any = ...
    cost_negative: Any = ...
    drift_detection: Any = ...
    base_estimator: Any = ...
    ensemble: Any = ...
    actual_n_estimators: Any = ...
    classes: Any = ...
    adwin_ensemble: Any = ...
    lam_tp: Any = ...
    lam_fn: Any = ...
    lam_tn: Any = ...
    lam_fp: Any = ...
    lam_sum: Any = ...
    wacc: Any = ...
    werr: Any = ...
    def __init__(self, base_estimator: Any = ..., n_estimators: int = ..., cost_positive: int = ..., cost_negative: float = ..., drift_detection: bool = ..., random_state: Optional[Any] = ...) -> None: ...
    def reset(self) -> None: ...
    def partial_fit(self, X: Any, y: Any, classes: Optional[Any] = ..., sample_weight: Optional[Any] = ...): ...
    def predict(self, X: Any): ...
    def predict_proba(self, X: Any): ...
