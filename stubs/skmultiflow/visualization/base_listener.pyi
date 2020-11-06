from abc import ABCMeta, abstractmethod
from skmultiflow.core.base import BaseEstimator as BaseEstimator
from typing import Any

class BaseListener(BaseEstimator, metaclass=ABCMeta):
    def __init__(self) -> None: ...
    @abstractmethod
    def on_new_train_step(self, sample_id: Any, data_buffer: Any) -> Any: ...
