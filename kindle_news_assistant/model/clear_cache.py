"""The main method for clearing the article cache."""
import shutil
import click
from newspaper.settings import TOP_DIRECTORY


def clear_cache_dir():
    """Delete the article cache directory and all its memoized articles."""
    print("Cache directory is located at:")
    print(TOP_DIRECTORY + "\n")

    if click.confirm("Are you sure you want to delete the cache folder?"):
        shutil.rmtree(TOP_DIRECTORY)
        print("Cache directory successfully deleted.")
