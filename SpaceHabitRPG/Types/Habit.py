import DatabaseLayer

class Habit(object):
    """description of class"""
    def __init__(self,dict=None,id = None):
        """Priority is given to dictionary object over id """
        self._changes = {}
        if dict:
            self._dict = dict
            return
        if id:
            self._dict = DatabaseLayer.get_thing_by_id(id,"habits")
            return
        raise ValueError("Either a reference to a dictionary or an id is required")


    def save_changes(self):
        DatabaseLayer.update_thing_by_id(self.id,"habits",self._changes)
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
    def polarity(self):
        return self._dict['polarity']

    @polarity.setter
    def polarity(self,value):
        self._dict['polarity'] = value
        self._changes['polarity'] = value

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
    def frequency(self):
        return self._dict['frequency']

    @frequency.setter
    def frequency(self,value):
        self._dict['frequency'] = value
        self._changes['frequency'] = value

    @property
    def allowance(self):
        return self._dict['allowance']

    @allowance.setter
    def allowance(self,value):
        self._dict['allowance'] = value
        self._changes['allowance'] = value

    @property
    def punishOnNeglect(self):
        return self._dict['punishOnNeglect']

    @punishOnNeglect.setter
    def punishOnNeglect(self,value):
        self._dict['punishOnNeglect'] = value
        self._changes['punishOnNeglect'] = value