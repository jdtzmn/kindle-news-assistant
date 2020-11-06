"""File opener helper that creates subdirectories as needed."""
import os
import errno


def mkdirs(path: str):
    """Make directories as needed – used in the safe_open method.

    :param path: The path of a file or directories to create
    """
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def safe_open(path: str, mode: str):
    """Open "path" for writing, creating any parent directories as needed.

    :param path: The path of a file to open
    :param mode: The mode, as described by the python built-in `open` function
    :return: The opened file, using python's built-in `open` function
    """
    mkdirs(os.path.dirname(path))
    return open(path, mode)
