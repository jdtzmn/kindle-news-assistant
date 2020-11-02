from ..base import MultiOutputMixin as MultiOutputMixin, RegressorMixin as RegressorMixin
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..model_selection import check_cv as check_cv
from ..utils import arrayfuncs as arrayfuncs, as_float_array as as_float_array, check_random_state as check_random_state
from ._base import LinearModel as LinearModel
from typing import Any, Optional

SOLVE_TRIANGULAR_ARGS: Any

def lars_path(X: Any, y: Any, Xy: Optional[Any] = ..., *, Gram: Optional[Any] = ..., max_iter: int = ..., alpha_min: int = ..., method: str = ..., copy_X: bool = ..., eps: Any = ..., copy_Gram: bool = ..., verbose: int = ..., return_path: bool = ..., return_n_iter: bool = ..., positive: bool = ...): ...
def lars_path_gram(Xy: Any, Gram: Any, n_samples: Any, *, max_iter: int = ..., alpha_min: int = ..., method: str = ..., copy_X: bool = ..., eps: Any = ..., copy_Gram: bool = ..., verbose: int = ..., return_path: bool = ..., return_n_iter: bool = ..., positive: bool = ...): ...

class Lars(MultiOutputMixin, RegressorMixin, LinearModel):
    method: str = ...
    positive: bool = ...
    fit_intercept: Any = ...
    verbose: Any = ...
    normalize: Any = ...
    precompute: Any = ...
    n_nonzero_coefs: Any = ...
    eps: Any = ...
    copy_X: Any = ...
    fit_path: Any = ...
    jitter: Any = ...
    random_state: Any = ...
    def __init__(self, *, fit_intercept: bool = ..., verbose: bool = ..., normalize: bool = ..., precompute: str = ..., n_nonzero_coefs: int = ..., eps: Any = ..., copy_X: bool = ..., fit_path: bool = ..., jitter: Optional[Any] = ..., random_state: Optional[Any] = ...) -> None: ...
    def fit(self, X: Any, y: Any, Xy: Optional[Any] = ...): ...

class LassoLars(Lars):
    method: str = ...
    alpha: Any = ...
    fit_intercept: Any = ...
    max_iter: Any = ...
    verbose: Any = ...
    normalize: Any = ...
    positive: Any = ...
    precompute: Any = ...
    copy_X: Any = ...
    eps: Any = ...
    fit_path: Any = ...
    jitter: Any = ...
    random_state: Any = ...
    def __init__(self, alpha: float = ..., *, fit_intercept: bool = ..., verbose: bool = ..., normalize: bool = ..., precompute: str = ..., max_iter: int = ..., eps: Any = ..., copy_X: bool = ..., fit_path: bool = ..., positive: bool = ..., jitter: Optional[Any] = ..., random_state: Optional[Any] = ...) -> None: ...

class LarsCV(Lars):
    method: str = ...
    max_iter: Any = ...
    cv: Any = ...
    max_n_alphas: Any = ...
    n_jobs: Any = ...
    def __init__(self, *, fit_intercept: bool = ..., verbose: bool = ..., max_iter: int = ..., normalize: bool = ..., precompute: str = ..., cv: Optional[Any] = ..., max_n_alphas: int = ..., n_jobs: Optional[Any] = ..., eps: Any = ..., copy_X: bool = ...) -> None: ...
    alpha_: Any = ...
    cv_alphas_: Any = ...
    mse_path_: Any = ...
    def fit(self, X: Any, y: Any): ...

class LassoLarsCV(LarsCV):
    method: str = ...
    fit_intercept: Any = ...
    verbose: Any = ...
    max_iter: Any = ...
    normalize: Any = ...
    precompute: Any = ...
    cv: Any = ...
    max_n_alphas: Any = ...
    n_jobs: Any = ...
    eps: Any = ...
    copy_X: Any = ...
    positive: Any = ...
    def __init__(self, *, fit_intercept: bool = ..., verbose: bool = ..., max_iter: int = ..., normalize: bool = ..., precompute: str = ..., cv: Optional[Any] = ..., max_n_alphas: int = ..., n_jobs: Optional[Any] = ..., eps: Any = ..., copy_X: bool = ..., positive: bool = ...) -> None: ...

class LassoLarsIC(LassoLars):
    criterion: Any = ...
    fit_intercept: Any = ...
    positive: Any = ...
    max_iter: Any = ...
    verbose: Any = ...
    normalize: Any = ...
    copy_X: Any = ...
    precompute: Any = ...
    eps: Any = ...
    fit_path: bool = ...
    def __init__(self, criterion: str = ..., *, fit_intercept: bool = ..., verbose: bool = ..., normalize: bool = ..., precompute: str = ..., max_iter: int = ..., eps: Any = ..., copy_X: bool = ..., positive: bool = ...) -> None: ...
    alphas_: Any = ...
    criterion_: Any = ...
    alpha_: Any = ...
    coef_: Any = ...
    def fit(self, X: Any, y: Any, copy_X: Optional[Any] = ...): ...
