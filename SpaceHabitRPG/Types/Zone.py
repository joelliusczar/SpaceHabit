import DatabaseLayer

COLLECTION_NAME = 'zones'
ID_KEY = '_id'
NAME = 'name'
Progress_LVL = 'progressLvl'
END_POINT_LVL = 'endPointLvl'
SKILL_LVL = 'skillLvl'
DESCRIPTION = 'description'
PREVIOUS_ZONE_REFERENCE = 'previousZoneReference'
NEXT_ZONE_REFERENCE_LIST = 'nextZoneReferenceList'
ZONE_TYPE = 'zoneType'



class Zone(object):
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
    def progressLvl(self):
        return self._dict[Progress_LVL]

    @progressLvl.setter
    def progressLvl(self,value):
        self._dict[Progress_LVL] = value
        self._changes[Progress_LVL] = value

    @property
    def endPointLvl(self):
        return self._dict[END_POINT_LVL]

    @endPointLvl.setter
    def endPointLvl(self,value):
        self._dict[END_POINT_LVL] = value
        self._changes[END_POINT_LVL] = value

    @property
    def skillLvl(self):
        return self._dict[SKILL_LVL]

    @skillLvl.setter
    def skillLvl(self,value):
        self._dict[SKILL_LVL] = value
        self._changes[SKILL_LVL] = value

    @property
    def description(self):
        return self._dict[DESCRIPTION]

    @description.setter
    def description(self,value):
        self._dict[DESCRIPTION] = value
        self._changes[DESCRIPTION] = value

    @property
    def previousZoneReference(self):
        return self._dict[PREVIOUS_ZONE_REFERENCE]

    @previousZoneReference.setter
    def previousZoneReference(self,value):
        self._dict[PREVIOUS_ZONE_REFERENCE] = value
        self._changes[PREVIOUS_ZONE_REFERENCE] = value

    @property
    def nextZoneReferenceList(self):
        return self._dict[NEXT_ZONE_REFERENCE_LIST]

    @nextZoneReferenceList.setter
    def nextZoneReferenceList(self,value):
        self._dict[NEXT_ZONE_REFERENCE_LIST] = value
        self._changes[NEXT_ZONE_REFERENCE_LIST] = value

    @property
    def zoneType(self):
        return self._dict[ZONE_TYPE]

    @zoneType.setter
    def zoneType(self,value):
        self._dict[ZONE_TYPE] = value
        self._changes[ZONE_TYPE] = value