"""Keep track of articles that have been read previously."""
import os
from typing import List

dirname = os.path.dirname(__file__)
RELATIVE_PATH = "../userdata/history.txt"
absolute_path = os.path.join(dirname, RELATIVE_PATH)


class History:
    """A class for keeping track of articles that have already been read."""

    def __init__(self):
        """Initialize the History class."""
        self.history_file = open(absolute_path, "a+")
        content = self.history_file.read()
        self.history_fileeeds = content.split("\n")

    def __del__(self):
        """Delete the History class."""
        self.history_file.close()

    def contains(self, article_id: str) -> bool:
        """Determine whether the history log contains a given article id.

        :param article_id: The identifier associated with a given article
        :return: Whether or not the article id is in the history log
        """
        self.history_file.seek(0)
        ids = self.history_file.readlines()
        return article_id + "\n" in ids

    def append(self, article_id: str):
        """Append an article id to the end of the history log.

        :param article_id: The identifier associated with a given article
        """
        self.history_file.seek(0, 2)
        self.history_file.write(article_id + "\n")

    def extend(self, ids: List[str]):
        """Append a list of article ids to the end of the history log.

        :param ids: A list of identifiers associated with a given list of articles
        """
        self.history_file.seek(0, 2)
        for article_id in ids:
            self.history_file.write(article_id + "\n")

    def remove_ids_other_than(self, ids: List[str]):
        """Remove all the ids that are not in a given list of ids.

        This is useful for removing unnecessary records of ids that are no longer
        relevant for a given RSS feed (ones that have disappeared).

        :param ids: A list of article ids
        """
        self.history_file.seek(0)
        lines = self.history_file.readlines()
        self.history_file.truncate(0)
        self.history_file.seek(0)
        for article_id in lines:
            if article_id.rstrip() in ids:
                self.history_file.write(article_id)
        self.history_file.truncate()
