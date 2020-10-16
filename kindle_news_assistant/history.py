import os

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

  def contains(self, id):
    """Determine whether the history log contains a given article id

    :param id: The identifier associated with a given article
    :type id: string
    :return: Whether or not the article id is in the history log
    :rtype: boolean
    """
    self.f.seek(0)
    ids = self.f.readlines()
    return (id + "\n") in ids

  def append(self, id):
    """Append an article id to the end of the history log

    :param id: The identifier associated with a given article
    :type id: string
    """
    self.f.seek(0, 2)
    self.f.write(id + "\n")

  def extend(self, ids):
    """Append a list of article ids to the end of the history log

    :param ids: A list of identifiers associated with a given list of articles
    :type ids: string[]
    """
    self.f.seek(0, 2)
    for id in ids:
      self.f.write(id + "\n")

  def remove_ids_other_than(self, ids):
    """Remove all the ids that are not in a given list of ids.
      This is useful for removing unnecessary records of ids that are no longer
      relevant for a given RSS feed (ones that have disappeared).

    :param ids: A list of article ids
    :type ids: string[]
    """
    self.f.seek(0)
    lines = self.f.readlines()
    self.f.truncate(0)
    self.f.seek(0)
    for id in lines:
      if id.rstrip() in ids:
        self.f.write(id)
    self.f.truncate()