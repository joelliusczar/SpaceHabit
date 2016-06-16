import DatabaseLayer

COLLECTION_NAME = 'todos'
ID_KEY = '_id'
NAME = 'name'
NOTE = 'note'
URGENCY = 'urgency'
DIFFICULTY = 'difficulty'
EFFECTIVE_DATE = 'effectiveDate'
DUE_DATE = 'dueDate'
PUBLIC_KEY = 'PublicKey'

def get_todos_by_account(id):
    import pymongo
    return DatabaseLayer.get_sorted_stuff_by_search({ID_KEY:id},COLLECTION_NAME,[
        (DUE_DATE,pymongo.ASCENDING),
        (URGENCY,pymongo.DESCENDING),
        (DIFFICULTY,pymongo.ASCENDING)
        (EFFECTIVE_DATE,pymongo.ASCENDING)])

class Todo(object):
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
    def urgency(self):
        return self._dict[URGENCY]

    @urgency.setter
    def urgency(self,value):
        self._dict[URGENCY] = value
        self._changes[URGENCY] = value

    @property
    def difficulty(self):
        return self._dict[DIFFICULTY]

    @difficulty.setter
    def difficulty(self,value):
        self._dict[DIFFICULTY] = value
        self._changes[DIFFICULTY] = value

    @property
    def effectiveDate(self):
        return self._dict[EFFECTIVE_DATE]

    @effectiveDate.setter
    def effectiveDate(self,value):
        self._dict[EFFECTIVE_DATE] = value
        self._changes[EFFECTIVE_DATE] = value

    @property
    def dueDate(self):
        return self._dict[DUE_DATE]

    @dueDate.setter
    def dueDate(self,value):
        self._dict[DUE_DATE] = value
        self._changes[DUE_DATE] = value
