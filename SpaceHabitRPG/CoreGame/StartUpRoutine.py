from datetime import datetime, timedelta
from StoryEvents import storyEvents
from Zone import Zone
from Monster import Monster
import random

def build_first_time_checkin_messages(hero):
  """
    We want to build a dict that can be sent back to the client when they
    create a hero

    args:
      hero: 
        an object of the hero model. We want to iterate through the
        zone options for where to go next and we need the shipname from 
        the hero.

    return:
      a dict with two keys: 
        key1: storyNotice: 
        value1: a story element to display at the user
        key2: zoneNotice: 
        value2: the new zone description
        key3: zonePrompt:
        value3: a small list of dicts that the zone info that the user can
        choose
  """
  result = {}
  result['storyNotice'] = get_intro_with_shipName_included(hero.shipName)
  result['zoneNotice'] = hero.zone.get_description()
  result['zonePrompt'] = hero.zone.nextZoneReferenceList
  return result

def get_intro_with_shipName_included(shipName):
  """
    we want to check if the user gave their ship a name and then add it to the
    story. And if they didn't, then we'll modify accordingly.
    
    args:
      shipName:
        string, name of the ship, duh!

    return:
      modified story element
  """
  storyElement = storyEvents['newUser']['description']
  if shipName:
    return storyElement.format(shipName)
  else:
    return storyElement.format(storyEvents['noShipNameIntro']['description'])



def check_in_and_get_notices(heroPk,accountPk,checkinTimeUtc,utcOffset):
  """
    this should be called on page load and should be used to get any notices
    for the use

    args:
      heroPk:
        we want a  pymongo objectId for the hero table
      accountPk:
        we want a  pymongo objectId for the hero table
      checkinTimeUtc:
        this needs to be that the user check in and it needs to be utc
      utcOffset:
         the time-zone offset from UTC, in minutes, for the current locale.

    returns:
      we return a dict with two elements: 'story' which will be a list of 
      huge things of text and 'zoneChoice' which is a list of dicts each
      of which contain 'zoneId','description'
      but zoneChoice may be none.

  """
  from Hero import Hero
  from Account import Account
  hero = Hero.create_model_from_pk(heroPk)
  account = Account.create_model_from_pk(accountPk)

  lastCheckinTime = account.lastCheckInTime
  account.lastCheckInTime = checkinTimeUtc
  account.save_changes()

  if not lastCheckinTime:
    messages = build_first_time_checkin_messages(hero)
    hero.isInZoneLimbo = True
    hero.save_changes()
    return messages

  if hero.isInZoneLimbo:
    autoPickedZoneDict = random.choice(hero.zone.nextZoneReferenceList)
    hero.zone = Zone.construct_model_from_dict(autoPickedZoneDict)
    hero.monster = Monster.construct_new_monster(hero.zone.definitionKey,hero.zone.lvl)
    

  timeDiffInDays = (checkinTimeUtc - lastCheckinTime)/(60*60*24)
  if timeDiffInDays >= 1:
    pass

  






