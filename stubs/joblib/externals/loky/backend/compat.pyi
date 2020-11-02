import queue as queue
from .compat_posix import wait as wait
from multiprocessing.process import BaseProcess as BaseProcess
from typing import Any

def set_cause(exc: Any, cause: Any): ...
