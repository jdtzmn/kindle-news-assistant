from skmultiflow.trees.split_criterion import SplitCriterion as SplitCriterion
from typing import Any

class GiniSplitCriterion(SplitCriterion):
    def get_merit_of_split(self, pre_split_dist: Any, post_split_dist: Any): ...
    @staticmethod
    def compute_gini(dist: Any, dist_sum_of_weights: Any): ...
    @staticmethod
    def get_range_of_merit(pre_split_dist: Any): ...