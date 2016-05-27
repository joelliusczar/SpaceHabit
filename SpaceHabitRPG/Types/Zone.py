import DatabaseLayer

class Zone(object):
    """description of class"""
    def __init__(self,dict=None,id = None):
        """Priority is given to dictionary object over id """
        self._changes = {}
        if dict:
            self._dict = dict
            return
        if id:
            self._dict = DatabaseLayer.get_thing_by_id(id,"zones")
            return
        raise ValueError("Either a reference to a dictionary or an id is required")


    def save_changes(self):
        DatabaseLayer.update_thing_by_id(self.id,"zones",self._changes)
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
    def voyageLvl(self):
        return self._dict['voyageLvl']

    @voyageLvl.setter
    def voyageLvl(self,value):
        self._dict['voyageLvl'] = value
        self._changes['voyageLvl'] = value

    @property
    def destinationLvl(self):
        return self._dict['destinationLvl']

    @destinationLvl.setter
    def destinationLvl(self,value):
        self._dict['destinationLvl'] = value
        self._changes['destinationLvl'] = value

    @property
    def skillLvl(self):
        return self._dict['skillLvl']

    @skillLvl.setter
    def skillLvl(self,value):
        self._dict['skillLvl'] = value
        self._changes['skillLvl'] = value

    @property
    def description(self):
        return self._dict['description']

    @description.setter
    def description(self,value):
        self._dict['description'] = value
        self._changes['description'] = value

    @property
    def previousZoneReference(self):
        return self._dict['previousZoneReference']

    @previousZoneReference.setter
    def previousZoneReference(self,value):
        self._dict['previousZoneReference'] = value
        self._changes['previousZoneReference'] = value

    @property
    def nextZoneReferenceList(self):
        return self._dict['nextZoneReferenceList']

    @nextZoneReferenceList.setter
    def nextZoneReferenceList(self,value):
        self._dict['nextZoneReferenceList'] = value
        self._changes['nextZoneReferenceList'] = value

    @property
    def zoneType(self):
        return self._dict['zoneType']

    @zoneType.setter
    def zoneType(self,value):
        self._dict['zoneType'] = value
        self._changes['zoneType'] = value