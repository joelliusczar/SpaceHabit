class Defintions(object):
  """
    base class for easy reference to static content such as descriptions and 
    names and such.
  """

  _indexes = None

  def __init__(self,key):
    """
      args:
        key:
          this should be the string key for any of the allZones sub-dicts
    """
    self._key = key

  def get_name(self):
    return self._indexes[self._key]['name']

  def get_description(self):
    return self._indexes[self._key]['description']


