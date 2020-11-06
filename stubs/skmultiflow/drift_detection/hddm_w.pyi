from math import *
from skmultiflow.drift_detection.base_drift_detector import BaseDriftDetector as BaseDriftDetector
from typing import Any

class HDDM_W(BaseDriftDetector):
    class SampleInfo:
        EWMA_estimator: Any = ...
        independent_bounded_condition_sum: Any = ...
        def __init__(self) -> None: ...
    total: Any = ...
    sample1_decr_monitor: Any = ...
    sample1_incr_monitor: Any = ...
    sample2_decr_monitor: Any = ...
    sample2_incr_monitor: Any = ...
    incr_cutpoint: Any = ...
    decr_cutpoint: Any = ...
    width: int = ...
    delay: int = ...
    drift_confidence: Any = ...
    warning_confidence: Any = ...
    lambda_option: Any = ...
    two_side_option: Any = ...
    def __init__(self, drift_confidence: float = ..., warning_confidence: float = ..., lambda_option: float = ..., two_side_option: bool = ...) -> None: ...
    in_concept_change: bool = ...
    in_warning_zone: bool = ...
    estimation: Any = ...
    def add_element(self, prediction: Any) -> None: ...
    def reset(self) -> None: ...