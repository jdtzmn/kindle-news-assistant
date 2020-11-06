from skmultiflow.bayes import do_naive_bayes_prediction as do_naive_bayes_prediction
from skmultiflow.trees.nodes import AnyTimeActiveLearningNode as AnyTimeActiveLearningNode
from typing import Any

class AnyTimeLearningNodeNB(AnyTimeActiveLearningNode):
    def __init__(self, initial_class_observations: Any) -> None: ...
    def get_class_votes(self, X: Any, ht: Any): ...
    def disable_attribute(self, att_index: Any) -> None: ...