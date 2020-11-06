from skmultiflow.drift_detection.adwin import ADWIN as ADWIN
from skmultiflow.trees.attribute_test import NominalAttributeMultiwayTest as NominalAttributeMultiwayTest
from skmultiflow.trees.nodes import ActiveLearningNode as ActiveLearningNode, AdaNode as AdaNode, FoundNode as FoundNode, InactiveLearningNode as InactiveLearningNode, SplitNode as SplitNode
from skmultiflow.utils import check_random_state as check_random_state
from typing import Any, Optional

class AdaSplitNodeForRegression(SplitNode, AdaNode):
    error_change: bool = ...
    random_state: Any = ...
    def __init__(self, split_test: Any, class_observations: Any, random_state: Optional[Any] = ...) -> None: ...
    def number_leaves(self): ...
    def get_error_estimation(self): ...
    def get_error_width(self): ...
    def is_null_error(self): ...
    def learn_from_instance(self, X: Any, y: Any, weight: Any, rhat: Any, parent: Any, parent_branch: Any) -> None: ...
    def kill_tree_children(self, rhat: Any) -> None: ...
    def filter_instance_to_leaves(self, X: Any, y: Any, weight: Any, parent: Any, parent_branch: Any, update_splitter_counts: bool = ..., found_nodes: Optional[Any] = ...) -> None: ...
    def get_normalized_error(self, y: Any, y_pred: Any): ...
