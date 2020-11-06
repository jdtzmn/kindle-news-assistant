from abc import ABCMeta, abstractmethod
from typing import Any

class InstanceConditionalTest(metaclass=ABCMeta):
    def __init__(self) -> None: ...
    @abstractmethod
    def branch_for_instance(self, X: Any) -> Any: ...
    @staticmethod
    @abstractmethod
    def max_branches() -> Any: ...
    @abstractmethod
    def describe_condition_for_branch(self, branch: Any) -> Any: ...
    @abstractmethod
    def get_atts_test_depends_on(self) -> Any: ...
