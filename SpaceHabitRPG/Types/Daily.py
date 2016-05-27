import DatabaseLayer

class Daily(object):
    """description of class"""
    def __init__(self,dict=None,id = None):
        """Priority is given to dictionary object over id """
        self._changes = {}
        if dict:
            self._dict = dict
            return
        if id:
            self._dict = DatabaseLayer.get_thing_by_id(id,"dailies")
            return
        raise ValueError("Either a reference to a dictionary or an id is required")


    def save_changes(self):
        DatabaseLayer.update_thing_by_id(self.id,"dailies",self._changes)
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
    def urgency(self):
        return self._dict['urgency']

    @urgency.setter
    def urgency(self,value):
        self._dict['urgency'] = value
        self._changes['urgency'] = value

    @property
    def difficulty(self):
        return self._dict['difficulty']

    @difficulty.setter
    def difficulty(self,value):
        self._dict['difficulty'] = value
        self._changes['difficulty'] = value

    @property
    def triggerFrequency(self):
        return self._dict['triggerFrequency']

    @triggerFrequency.setter
    def triggerFrequency(self,value):
        self._dict['triggerFrequency'] = value
        self._changes['triggerFrequency'] = value

    @property
    def daysUntilTrigger(self):
        return self._dict['daysUntilTrigger']

    @daysUntilTrigger.setter
    def daysUntilTrigger(self,value):
        self._dict['daysUntilTrigger'] = value
        self._changes['daysUntilTrigger'] = value

    @property
    def activeDays(self):
        return self._dict['activeDays']

    @activeDays.setter
    def activeDays(self,value):
        self._dict['activeDays'] = value
        self._changes['activeDays'] = value