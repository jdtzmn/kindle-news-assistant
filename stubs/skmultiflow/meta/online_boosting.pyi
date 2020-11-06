from skmultiflow.utils.utils import *
from skmultiflow.core import BaseSKMObject as BaseSKMObject, ClassifierMixin as ClassifierMixin, MetaEstimatorMixin as MetaEstimatorMixin
from skmultiflow.drift_detection import ADWIN as ADWIN
from skmultiflow.lazy import KNNADWINClassifier as KNNADWINClassifier
from skmultiflow.utils import check_random_state as check_random_state
from typing import Any, Optional

def OnlineBoosting(base_estimator: Any = ..., n_estimators: int = ..., drift_detection: bool = ..., random_state: Optional[Any] = ...): ...

class OnlineBoostingClassifier(BaseSKMObject, ClassifierMixin, MetaEstimatorMixin):
    base_estimator: Any = ...
    random_state: Any = ...
    drift_detection: Any = ...
    ensemble: Any = ...
    actual_n_estimators: Any = ...
    classes: Any = ...
    adwin_ensemble: Any = ...
    lam_sc: Any = ...
    lam_sw: Any = ...
    epsilon: Any = ...
    def __init__(self, base_estimator: Any = ..., n_estimators: int = ..., drift_detection: bool = ..., random_state: Optional[Any] = ...) -> None: ...
    def reset(self) -> None: ...
    def partial_fit(self, X: Any, y: Any, classes: Optional[Any] = ..., sample_weight: Optional[Any] = ...): ...
    def predict(self, X: Any): ...
    def predict_proba(self, X: Any): ...