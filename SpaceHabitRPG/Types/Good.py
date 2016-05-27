import DatabaseLayer

class Good(object):
    """description of class"""
    def __init__(self,dict=None,id = None):
        """Priority is given to dictionary object over id """
        self._changes = {}
        if dict:
            self._dict = dict
            return
        if id:
            self._dict = DatabaseLayer.get_thing_by_id(id,"goods")
            return
        raise ValueError("Either a reference to a dictionary or an id is required")


    def save_changes(self):
        DatabaseLayer.update_thing_by_id(self.id,"goods",self._changes)
        self._changes = {}

    @property
    def id(self):
        return self._dict['_id']

    @property
    def name(self):
        return self._dict['name']

    @name.setter
    def name(self,value):
        self._dict['name'] = value
        self._changes['name'] = value

    @property
    def note(self):
        return self._dict['note']

    @note.setter
    def note(self,value):
        self._dict['note'] = value
        self._changes['note'] = value

    @property
    def cost(self):
        return self._dict['cost']

    @cost.setter
    def cost(self,value):
        self._dict['cost'] = value
        self._changes['cost'] = value

    @property
    def type(self):
        return self._dict['type']

    @type.setter
    def daysUntilTrigger(self,value):
        self._dict['type'] = value
        self._changes['type'] = value

    @property
    def special(self):
        return self._dict['special']

    @special.setter
    def special(self,value):
        self._dict['special'] = value
        self._changes['special'] = value