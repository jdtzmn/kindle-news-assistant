"""File opener helper that creates subdirectories as needed."""
import os
import errno


def mkdirs(path: str):
    """Make directories as needed – used in the safe_open method."""
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def safe_open(path: str, mode: str):
    """Open "path" for writing, creating any parent directories as needed."""
    mkdirs(os.path.dirname(path))
    return open(path, mode)
