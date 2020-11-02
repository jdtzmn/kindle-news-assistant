from .compat import pickle as pickle # type: ignore
from typing import Any # type: ignore

def f(): ...

CellType: Any
DEFAULT_PROTOCOL: Any
PYPY: Any
builtin_code_type: Any

def cell_set(cell: Any, value: Any) -> None: ...

STORE_GLOBAL: Any
DELETE_GLOBAL: Any
LOAD_GLOBAL: Any
GLOBAL_OPS: Any
HAVE_ARGUMENT: Any
EXTENDED_ARG: Any

def parametrized_type_hint_getinitargs(obj: Any): ...
def is_tornado_coroutine(func: Any): ...

load: Any
loads: Any

def subimport(name: Any): ...
def dynamic_subimport(name: Any, vars: Any): ...
def instance(cls): ...

class _empty_cell_value:
    @classmethod
    def __reduce__(cls): ...
