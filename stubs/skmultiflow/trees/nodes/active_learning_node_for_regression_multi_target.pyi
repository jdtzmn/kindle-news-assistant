from skmultiflow.trees.attribute_observer import NominalAttributeRegressionObserver as NominalAttributeRegressionObserver, NumericAttributeRegressionObserver as NumericAttributeRegressionObserver
from skmultiflow.trees.nodes import ActiveLearningNodeForRegression as ActiveLearningNodeForRegression
from typing import Any

class ActiveLearningNodeForRegressionMultiTarget(ActiveLearningNodeForRegression):
    def __init__(self, initial_class_observations: Any) -> None: ...
    def learn_from_instance(self, X: Any, y: Any, weight: Any, ht: Any) -> None: ...
