from skmultiflow.trees.attribute_observer import NominalAttributeRegressionObserver as NominalAttributeRegressionObserver, NumericAttributeRegressionObserver as NumericAttributeRegressionObserver
from skmultiflow.trees.nodes import ActiveLearningNodeForRegression as ActiveLearningNodeForRegression
from skmultiflow.utils import check_random_state as check_random_state
from typing import Any, Optional

class ActiveLearningNodePerceptron(ActiveLearningNodeForRegression):
    random_state: Any = ...
    samples_seen: int = ...
    perceptron_weight: Any = ...
    def __init__(self, initial_class_observations: Any, parent_node: Optional[Any] = ..., random_state: Optional[Any] = ...) -> None: ...
    def learn_from_instance(self, X: Any, y: Any, weight: Any, rht: Any) -> None: ...
    def update_weights(self, X: Any, y: Any, learning_ratio: Any, rht: Any) -> None: ...

def compute_sd(square_val: float, val: float, size: float) -> Any: ...
