from skmultiflow.trees.nodes import InactiveLearningNodePerceptronMultiTarget as InactiveLearningNodePerceptronMultiTarget
from typing import Any, Optional

class InactiveLearningNodeAdaptiveMultiTarget(InactiveLearningNodePerceptronMultiTarget):
    fMAE_M: float = ...
    fMAE_P: float = ...
    def __init__(self, initial_class_observations: Any, parent_node: Optional[Any] = ..., random_state: Optional[Any] = ...) -> None: ...
    def update_weights(self, X: Any, y: Any, learning_ratio: Any, rht: Any) -> None: ...