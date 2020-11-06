from skmultiflow.data.base_stream import Stream as Stream
from skmultiflow.utils import check_random_state as check_random_state
from typing import Any, Optional

class AGRAWALGenerator(Stream):
    random_state: Any = ...
    n_num_features: int = ...
    n_cat_features: int = ...
    n_features: Any = ...
    n_classes: int = ...
    n_targets: int = ...
    name: str = ...
    target_names: Any = ...
    feature_names: Any = ...
    target_values: Any = ...
    def __init__(self, classification_function: int = ..., random_state: Optional[Any] = ..., balance_classes: bool = ..., perturbation: float = ...) -> None: ...
    @property
    def classification_function(self): ...
    @classification_function.setter
    def classification_function(self, classification_function_idx: Any) -> None: ...
    @property
    def balance_classes(self): ...
    @balance_classes.setter
    def balance_classes(self, balance_classes: Any) -> None: ...
    @property
    def perturbation(self): ...
    @perturbation.setter
    def perturbation(self, perturbation: Any) -> None: ...
    current_sample_x: Any = ...
    current_sample_y: Any = ...
    def next_sample(self, batch_size: int = ...): ...
    def generate_drift(self) -> None: ...
