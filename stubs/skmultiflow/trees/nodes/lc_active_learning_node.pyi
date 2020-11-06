from skmultiflow.trees.attribute_observer import NominalAttributeClassObserver as NominalAttributeClassObserver, NumericAttributeClassObserverGaussian as NumericAttributeClassObserverGaussian
from skmultiflow.trees.nodes import ActiveLearningNode as ActiveLearningNode
from typing import Any

class LCActiveLearningNode(ActiveLearningNode):
    def __init__(self, initial_class_observations: Any) -> None: ...
    def learn_from_instance(self, X: Any, y: Any, weight: Any, ht: Any) -> None: ...
