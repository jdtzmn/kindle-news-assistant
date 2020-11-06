from skmultiflow.data import AGRAWALGenerator as AGRAWALGenerator
from skmultiflow.data.base_stream import Stream as Stream
from skmultiflow.utils import check_random_state as check_random_state
from typing import Any, Optional

class ConceptDriftStream(Stream):
    n_samples: Any = ...
    n_targets: Any = ...
    n_features: Any = ...
    n_num_features: Any = ...
    n_cat_features: Any = ...
    n_classes: Any = ...
    cat_features_idx: Any = ...
    feature_names: Any = ...
    target_names: Any = ...
    target_values: Any = ...
    name: Any = ...
    random_state: Any = ...
    alpha: Any = ...
    width: Any = ...
    position: Any = ...
    stream: Any = ...
    drift_stream: Any = ...
    def __init__(self, stream: Any = ..., drift_stream: Any = ..., position: int = ..., width: int = ..., random_state: Optional[Any] = ..., alpha: float = ...) -> None: ...
    def n_remaining_samples(self): ...
    def has_more_samples(self): ...
    def is_restartable(self): ...
    current_sample_x: Any = ...
    current_sample_y: Any = ...
    def next_sample(self, batch_size: int = ...): ...
    sample_idx: int = ...
    def restart(self) -> None: ...