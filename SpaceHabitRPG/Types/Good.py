import DatabaseLayer

COLLECTION_NAME = 'goods'
ID_KEY = '_id'
NAME = 'name'
NOTE = 'note'
COST = 'cost'
TYPE = 'type'
SPECIAL = 'special'
PUBLIC_KEY = 'PublicKey'


class Good(object):
    """description of class"""
    def __init__(self,dict=None,id = None):
        """Priority is given to dictionary object over id """
        self._changes = {}
        if dict:
            self._dict = dict
            return
        if id:
            self._dict = DatabaseLayer.get_thing_by_id(id,COLLECTION_NAME)
            return
        raise ValueError("Either a reference to a dictionary or an id is required")


    def save_changes(self):
        DatabaseLayer.update_thing_by_id(self.id,COLLECTION_NAME,self._changes)
        self._changes = {}

    @property
    def id(self):
        return self._dict[ID_KEY]

    @property
    def name(self):
        return self._dict[NAME]

    @name.setter
    def name(self,value):
        self._dict[NAME] = value
        self._changes[NAME] = value

    @property
    def note(self):
        return self._dict[NOTE]

    @note.setter
    def note(self,value):
        self._dict[NOTE] = value
        self._changes[NOTE] = value

    @property
    def cost(self):
        return self._dict[COST]

    @cost.setter
    def cost(self,value):
        self._dict[COST] = value
        self._changes[COST] = value

    @property
    def type(self):
        return self._dict[TYPE]

    @type.setter
    def type(self,value):
        self._dict[TYPE] = value
        self._changes[TYPE] = value

    @property
    def special(self):
        return self._dict[SPECIAL]

    @special.setter
    def special(self,value):
        self._dict[SPECIAL] = value
        self._changes[SPECIAL] = value