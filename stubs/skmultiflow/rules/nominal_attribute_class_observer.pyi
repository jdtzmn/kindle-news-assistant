from skmultiflow.rules.attribute_expand_suggestion import AttributeExpandSuggestion as AttributeExpandSuggestion
from skmultiflow.trees.attribute_observer import AttributeClassObserver as AttributeClassObserver
from typing import Any, Optional

class NominalAttributeClassObserver(AttributeClassObserver):
    def __init__(self) -> None: ...
    def observe_attribute_class(self, att_val: Any, class_val: Any, weight: Any) -> None: ...
    def probability_of_attribute_value_given_class(self, att_val: Any, class_val: Any): ...
    def get_best_evaluated_split_suggestion(self, criterion: Any, pre_split_dist: Any, att_idx: Any, class_idx: Optional[Any] = ...): ...
    def get_class_dist_from_multiway_split(self): ...
    def get_class_dist_from_binary_split(self, val_idx: Any): ...
