from typing import Any, Optional

def configuration(parent_package: str = ..., top_path: Optional[Any] = ...): ...

DEFAULT_ROOT: str
CYTHON_MIN_VERSION: str

def build_from_c_and_cpp_files(extensions: Any) -> None: ...
def maybe_cythonize_extensions(top_path: Any, config: Any) -> None: ...