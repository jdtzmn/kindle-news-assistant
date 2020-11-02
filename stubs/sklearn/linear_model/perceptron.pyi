from ..externals._pep562 import Pep562 as Pep562
from typing import Any

deprecated_path: str
correct_import_path: str

def __getattr__(name: Any): ...
