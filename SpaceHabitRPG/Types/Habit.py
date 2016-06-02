import DatabaseLayer

COLLECTION_NAME = 'dailies'
ID_KEY = '_id'
NAME = 'name'
NOTE = 'note'
URGENCY = 'urgency'
DIFFICULTY = 'difficulty'
POLARITY = 'polarity'
TRIGGER_FREQUENCY = 'triggerFrequency'
ALLOWANCE = 'allowance'
PUNISH_ON_NEGLECT = 'punishOnNeglect'
PUBLIC_KEY = 'PublicKey'

def get_habits_by_account(id):
    import pymongo
    return DatabaseLayer.get_sorted_stuff_by_key({ID_KEY:id},COLLECTION_NAME,[(TRIGGER_FREQUENCY,pymongo.DESCENDING),
        (URGENCY,pymongo.DESCENDING),
        (DIFFICULTY,pymongo.ASCENDING)])


class Habit(object):
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
    def polarity(self):
        return self._dict[POLARITY]

    @polarity.setter
    def polarity(self,value):
        self._dict[POLARITY] = value
        self._changes[POLARITY] = value

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
    def trigger_frequency(self):
        return self._dict[TRIGGER_FREQUENCY]

    @trigger_frequency.setter
    def trigger_frequency(self,value):
        self._dict[TRIGGER_FREQUENCY] = value
        self._changes[TRIGGER_FREQUENCY] = value

    @property
    def allowance(self):
        return self._dict[ALLOWANCE]

    @allowance.setter
    def allowance(self,value):
        self._dict[ALLOWANCE] = value
        self._changes[ALLOWANCE] = value

    @property
    def punishOnNeglect(self):
        return self._dict[PUNISH_ON_NEGLECT]

    @punishOnNeglect.setter
    def punishOnNeglect(self,value):
        self._dict[PUNISH_ON_NEGLECT] = value
        self._changes[PUNISH_ON_NEGLECT] = value