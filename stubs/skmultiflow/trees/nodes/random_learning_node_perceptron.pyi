from skmultiflow.trees.attribute_observer import NominalAttributeRegressionObserver as NominalAttributeRegressionObserver, NumericAttributeRegressionObserver as NumericAttributeRegressionObserver
from skmultiflow.trees.nodes import ActiveLearningNodePerceptron as ActiveLearningNodePerceptron
from skmultiflow.utils import get_dimensions as get_dimensions
from typing import Any, Optional

class RandomLearningNodePerceptron(ActiveLearningNodePerceptron):
    max_features: Any = ...
    list_attributes: Any = ...
    def __init__(self, initial_class_observations: Any, max_features: Any, parent_node: Optional[Any] = ..., random_state: Optional[Any] = ...) -> None: ...
    perceptron_weight: Any = ...
    samples_seen: Any = ...
    def learn_from_instance(self, X: Any, y: Any, weight: Any, rht: Any) -> None: ...