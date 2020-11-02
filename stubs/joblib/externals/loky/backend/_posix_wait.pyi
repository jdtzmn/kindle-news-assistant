import ctypes
from typing import Any, Optional

SYSTEM: Any
libSystem: Any
CoreServices: Any
mach_absolute_time: Any
absolute_to_nanoseconds: Any

def monotonic(): ...

CLOCK_MONOTONIC: int

class timespec(ctypes.Structure): ...

librt: Any
clock_gettime: Any

def wait(object_list: Any, timeout: Optional[Any] = ...): ...
