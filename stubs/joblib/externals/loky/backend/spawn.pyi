from typing import Any

WINEXE: bool
WINSERVICE: bool

def get_executable(): ...
def get_preparation_data(name: Any, init_main_module: bool = ...): ...

old_main_modules: Any

def prepare(data: Any) -> None: ...
def import_main_path(main_path: Any) -> None: ...
