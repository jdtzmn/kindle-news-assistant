from abc import ABCMeta, abstractmethod
from typing import Any

class SplitCriterion(metaclass=ABCMeta):
    def __init__(self) -> None: ...
    @abstractmethod
    def get_merit_of_split(self, pre_split_dist: Any, post_split_dist: Any) -> Any: ...
    @staticmethod
    @abstractmethod
    def get_range_of_merit(pre_split_dist: Any) -> Any: ...
