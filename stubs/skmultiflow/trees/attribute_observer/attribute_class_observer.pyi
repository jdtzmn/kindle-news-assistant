from abc import ABCMeta, abstractmethod
from typing import Any

class AttributeClassObserver(metaclass=ABCMeta):
    def __init__(self) -> None: ...
    @abstractmethod
    def observe_attribute_class(self, att_val: Any, class_val: Any, weight: Any) -> Any: ...
    @abstractmethod
    def probability_of_attribute_value_given_class(self, att_val: Any, class_val: Any) -> Any: ...
    @abstractmethod
    def get_best_evaluated_split_suggestion(self, criterion: Any, pre_split_dist: Any, att_idx: Any, binary_only: Any) -> Any: ...
