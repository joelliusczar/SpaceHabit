class OrphanedModelException(Exception):
    """
      raise this exception when the code trys to save certain kinds of models
      without a heroId
    """
    def __init__(self,value):
      self.value = value

    def __str__(self):
      return repr(self.value)


