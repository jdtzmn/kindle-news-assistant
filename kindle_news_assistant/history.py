import os
from typing import List

dirname = os.path.dirname(__file__)
relative_path = "../userdata/history.txt"
absolute_path = os.path.join(dirname, relative_path)


class History:
  """ A class for fetching articles from the feeds in `feeds.txt`
  """

  def __init__(self):
    self.f = open(absolute_path, "a+")
    content = self.f.read()
    self.feeds = content.split("\n")

  def __del__(self):
    self.f.close()

  def contains(self, id: str) -> bool:
    """Determine whether the history log contains a given article id

    :param id: The identifier associated with a given article
    :return: Whether or not the article id is in the history log
    """
    self.f.seek(0)
    ids = self.f.readlines()
    return (id + "\n") in ids

  def append(self, id: str):
    """Append an article id to the end of the history log

    :param id: The identifier associated with a given article
    """
    self.f.seek(0, 2)
    self.f.write(id + "\n")

  def extend(self, ids: List[str]):
    """Append a list of article ids to the end of the history log

    :param ids: A list of identifiers associated with a given list of articles
    """
    self.f.seek(0, 2)
    for id in ids:
      self.f.write(id + "\n")

  def remove_ids_other_than(self, ids: List[str]):
    """Remove all the ids that are not in a given list of ids.
      This is useful for removing unnecessary records of ids that are no longer
      relevant for a given RSS feed (ones that have disappeared).

    :param ids: A list of article ids
    """
    self.f.seek(0)
    lines = self.f.readlines()
    self.f.truncate(0)
    self.f.seek(0)
    for id in lines:
      if id.rstrip() in ids:
        self.f.write(id)
    self.f.truncate()