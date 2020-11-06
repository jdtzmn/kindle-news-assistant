from skmultiflow.data.base_stream import Stream as Stream
from skmultiflow.utils import check_random_state as check_random_state
from typing import Any, Optional

class RegressionGenerator(Stream):
    X: Any = ...
    y: Any = ...
    n_samples: Any = ...
    n_features: Any = ...
    n_targets: Any = ...
    n_informative: Any = ...
    n_num_features: Any = ...
    random_state: Any = ...
    name: str = ...
    def __init__(self, n_samples: int = ..., n_features: int = ..., n_informative: int = ..., n_targets: int = ..., random_state: Optional[Any] = ...) -> None: ...
    def n_remaining_samples(self): ...
    def has_more_samples(self): ...
    current_sample_x: Any = ...
    current_sample_y: Any = ...
    def next_sample(self, batch_size: int = ...): ...
    sample_idx: int = ...
    def restart(self) -> None: ...
    def get_data_info(self): ...