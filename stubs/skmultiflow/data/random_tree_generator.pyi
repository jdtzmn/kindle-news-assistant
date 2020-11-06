from skmultiflow.data.base_stream import Stream as Stream
from skmultiflow.utils import check_random_state as check_random_state
from typing import Any, Optional

class RandomTreeGenerator(Stream):
    tree_random_state: Any = ...
    sample_random_state: Any = ...
    n_classes: Any = ...
    n_targets: int = ...
    n_num_features: Any = ...
    n_cat_features: Any = ...
    n_categories_per_cat_feature: Any = ...
    n_features: Any = ...
    max_tree_depth: Any = ...
    min_leaf_depth: Any = ...
    fraction_leaves_per_level: Any = ...
    tree_root: Any = ...
    name: str = ...
    target_names: Any = ...
    feature_names: Any = ...
    target_values: Any = ...
    def __init__(self, tree_random_state: Optional[Any] = ..., sample_random_state: Optional[Any] = ..., n_classes: int = ..., n_cat_features: int = ..., n_num_features: int = ..., n_categories_per_cat_feature: int = ..., max_tree_depth: int = ..., min_leaf_depth: int = ..., fraction_leaves_per_level: float = ...) -> None: ...
    current_sample_x: Any = ...
    current_sample_y: Any = ...
    def next_sample(self, batch_size: int = ...): ...

class Node:
    class_label: Any = ...
    split_att_index: Any = ...
    split_att_value: Any = ...
    children: Any = ...
    def __init__(self, class_label: Optional[Any] = ..., split_att_index: Optional[Any] = ..., split_att_value: Optional[Any] = ...) -> None: ...