from skmultiflow.transform.base_transform import StreamTransform as StreamTransform
from skmultiflow.utils.utils import get_dimensions as get_dimensions
from typing import Any, Optional

class OneHotToCategorical(StreamTransform):
    categorical_list: Any = ...
    def __init__(self, categorical_list: Any) -> None: ...
    def transform(self, X: Any): ...
    def fit(self, X: Any, y: Any): ...
    def partial_fit_transform(self, X: Any, y: Optional[Any] = ..., classes: Optional[Any] = ...): ...
    def partial_fit(self, X: Any, y: Optional[Any] = ..., classes: Optional[Any] = ...): ...
