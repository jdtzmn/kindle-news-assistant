from skmultiflow.core import BaseSKMObject as BaseSKMObject, ClassifierMixin as ClassifierMixin, MetaEstimatorMixin as MetaEstimatorMixin
from skmultiflow.drift_detection import ADWIN as ADWIN
from skmultiflow.drift_detection.base_drift_detector import BaseDriftDetector as BaseDriftDetector
from skmultiflow.metrics import ClassificationPerformanceEvaluator as ClassificationPerformanceEvaluator
from skmultiflow.trees.arf_hoeffding_tree import ARFHoeffdingTreeClassifier as ARFHoeffdingTreeClassifier
from skmultiflow.utils import check_random_state as check_random_state, check_weights as check_weights, get_dimensions as get_dimensions, normalize_values_in_dict as normalize_values_in_dict
from typing import Any, Optional

def AdaptiveRandomForest(n_estimators: Any=..., max_features: Any=..., disable_weighted_vote: Any=..., lambda_value: Any=..., performance_metric: Any=..., drift_detection_method: BaseDriftDetector=..., warning_detection_method: BaseDriftDetector=..., max_byte_size: Any=..., memory_estimate_period: Any=..., grace_period: Any=..., split_criterion: Any=..., split_confidence: Any=..., tie_threshold: Any=..., binary_split: Any=..., stop_mem_management: Any=..., remove_poor_atts: Any=..., no_preprune: Any=..., leaf_prediction: Any=..., nb_threshold: Any=..., nominal_attributes: Any=..., random_state: Any=...) -> Any: ...

class AdaptiveRandomForestClassifier(BaseSKMObject, ClassifierMixin, MetaEstimatorMixin):
    n_estimators: Any = ...
    max_features: Any = ...
    disable_weighted_vote: Any = ...
    lambda_value: Any = ...
    drift_detection_method: Any = ...
    warning_detection_method: Any = ...
    instances_seen: int = ...
    classes: Any = ...
    ensemble: Any = ...
    random_state: Any = ...
    performance_metric: Any = ...
    max_byte_size: Any = ...
    memory_estimate_period: Any = ...
    grace_period: Any = ...
    split_criterion: Any = ...
    split_confidence: Any = ...
    tie_threshold: Any = ...
    binary_split: Any = ...
    stop_mem_management: Any = ...
    remove_poor_atts: Any = ...
    no_preprune: Any = ...
    leaf_prediction: Any = ...
    nb_threshold: Any = ...
    nominal_attributes: Any = ...
    def __init__(self, n_estimators: Any=..., max_features: Any=..., disable_weighted_vote: Any=..., lambda_value: Any=..., performance_metric: Any=..., drift_detection_method: BaseDriftDetector=..., warning_detection_method: BaseDriftDetector=..., max_byte_size: Any=..., memory_estimate_period: Any=..., grace_period: Any=..., split_criterion: Any=..., split_confidence: Any=..., tie_threshold: Any=..., binary_split: Any=..., stop_mem_management: Any=..., remove_poor_atts: Any=..., no_preprune: Any=..., leaf_prediction: Any=..., nb_threshold: Any=..., nominal_attributes: Any=..., random_state: Any=...) -> None: ...
    def partial_fit(self, X: Any, y: Any, classes: Optional[Any] = ..., sample_weight: Optional[Any] = ...): ...
    def predict(self, X: Any): ...
    def predict_proba(self, X: Any): ...
    def reset(self) -> None: ...
    def get_votes_for_instance(self, X: Any): ...

class ARFBaseLearner(BaseSKMObject):
    index_original: Any = ...
    classifier: Any = ...
    created_on: Any = ...
    is_background_learner: Any = ...
    evaluator_method: Any = ...
    drift_detection_method: Any = ...
    warning_detection_method: Any = ...
    last_drift_on: int = ...
    last_warning_on: int = ...
    nb_drifts_detected: int = ...
    nb_warnings_detected: int = ...
    drift_detection: Any = ...
    warning_detection: Any = ...
    background_learner: Any = ...
    evaluator: Any = ...
    def __init__(self, index_original: Any, classifier: ARFHoeffdingTreeClassifier, instances_seen: Any, drift_detection_method: BaseDriftDetector, warning_detection_method: BaseDriftDetector, is_background_learner: Any) -> None: ...
    def reset(self, instances_seen: Any) -> None: ... # type: ignore
    def partial_fit(self, X: Any, y: Any, classes: Any, sample_weight: Any, instances_seen: Any) -> None: ...
    def predict(self, X: Any): ...
    def get_votes_for_instance(self, X: Any): ...
