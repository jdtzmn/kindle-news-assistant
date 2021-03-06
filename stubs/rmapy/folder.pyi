from .const import RFC3339Nano as RFC3339Nano
from .meta import Meta as Meta
from io import BytesIO
from typing import Any, Optional, Tuple

class ZipFolder:
    ID: Any = ...
    file: Any = ...
    Version: int = ...
    def __init__(self, _id: str) -> None: ...

class Folder(Meta):
    Type: str = ...
    VissibleName: Any = ...
    ID: Any = ...
    def __init__(self, name: Optional[str]=..., **kwargs: Any) -> None: ...
    def create_request(self) -> Tuple[BytesIO, dict]: ...
    def update_request(self) -> dict: ...
