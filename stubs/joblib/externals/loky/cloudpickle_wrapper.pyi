from joblib.externals.cloudpickle import dumps as dumps, loads as loads
from typing import Any

cloudpickle: bool
WRAP_CACHE: Any

class CloudpickledObjectWrapper:
    def __init__(self, obj: Any, keep_wrapper: bool = ...) -> None: ...
    def __reduce__(self): ...
    def __getattr__(self, attr: Any): ...

class CallableObjectWrapper(CloudpickledObjectWrapper):
    def __call__(self, *args: Any, **kwargs: Any): ...

def wrap_non_picklable_objects(obj: Any, keep_wrapper: bool = ...): ...
