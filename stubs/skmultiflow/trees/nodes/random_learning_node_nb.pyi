from skmultiflow.bayes import do_naive_bayes_prediction as do_naive_bayes_prediction
from skmultiflow.trees.nodes import RandomLearningNodeClassification as RandomLearningNodeClassification
from typing import Any

class RandomLearningNodeNB(RandomLearningNodeClassification):
    def __init__(self, initial_class_observations: Any, max_features: Any, random_state: Any) -> None: ...
    def get_class_votes(self, X: Any, ht: Any): ...
