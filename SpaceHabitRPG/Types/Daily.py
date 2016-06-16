import DatabaseLayer

COLLECTION_NAME = 'dailies'
ID_KEY = '_id'
NAME = 'name'
NOTE = 'note'
URGENCY = 'urgency'
DIFFICULTY = 'difficulty'
TRIGGER_PERIOD_LENGTH = 'triggerPeriodLength'
DAYS_UNTIL_TRIGGER = 'daysUntilTrigger'
ACTIVE_DAYS = 'activeDays'
PUBLIC_KEY = 'PublicKey'

def get_dailies_by_account(id,isCompleted=False):
    import pymongo
    return DatabaseLayer.get_sorted_stuff_by_search({ID_KEY:id,'isCompleted':isCompleted},
        COLLECTION_NAME,[(DAYS_UNTIL_TRIGGER,pymongo.ASCENDING),
        (URGENCY,pymongo.DESCENDING),
        (DIFFICULTY,pymongo.ASCENDING)])

class Daily(object):
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
    def triggerPeriodLength(self):
        return self._dict[TRIGGER_PERIOD_LENGTH]

    @triggerPeriodLength.setter
    def triggerPeriodLength(self,value):
        self._dict[TRIGGER_PERIOD_LENGTH] = value
        self._changes[TRIGGER_PERIOD_LENGTH] = value

    @property
    def daysUntilTrigger(self):
        return self._dict[DAYS_UNTIL_TRIGGER]

    @daysUntilTrigger.setter
    def daysUntilTrigger(self,value):
        self._dict[DAYS_UNTIL_TRIGGER] = value
        self._changes[DAYS_UNTIL_TRIGGER] = value

    @property
    def activeDays(self):
        return self._dict[ACTIVE_DAYS]

    @activeDays.setter
    def activeDays(self,value):
        self._dict[ACTIVE_DAYS] = value
        self._changes[ACTIVE_DAYS] = value