from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..utils import check_array as check_array
from ..utils.extmath import row_norms as row_norms
from ._base import make_dataset as make_dataset
from ._sag_fast import sag32 as sag32, sag64 as sag64
from typing import Any, Optional

def get_auto_step_size(max_squared_sum: Any, alpha_scaled: Any, loss: Any, fit_intercept: Any, n_samples: Optional[Any] = ..., is_saga: bool = ...): ...
def sag_solver(X: Any, y: Any, sample_weight: Optional[Any] = ..., loss: str = ..., alpha: float = ..., beta: float = ..., max_iter: int = ..., tol: float = ..., verbose: int = ..., random_state: Optional[Any] = ..., check_input: bool = ..., max_squared_sum: Optional[Any] = ..., warm_start_mem: Optional[Any] = ..., is_saga: bool = ...): ...
