from concurrent.futures import ALL_COMPLETED as ALL_COMPLETED, CancelledError as CancelledError, Executor as Executor, FIRST_COMPLETED as FIRST_COMPLETED, FIRST_EXCEPTION as FIRST_EXCEPTION, Future as _BaseFuture, TimeoutError as TimeoutError, as_completed as as_completed, wait as wait
from concurrent.futures._base import CANCELLED as CANCELLED, CANCELLED_AND_NOTIFIED as CANCELLED_AND_NOTIFIED, FINISHED as FINISHED, PENDING as PENDING, RUNNING as RUNNING

class Future(_BaseFuture): ...
