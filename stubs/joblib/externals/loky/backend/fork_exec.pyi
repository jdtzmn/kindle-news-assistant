from typing import Any, Optional

def close_fds(keep_fds: Any) -> None: ...
def fork_exec(cmd: Any, keep_fds: Any, env: Optional[Any] = ...): ...
