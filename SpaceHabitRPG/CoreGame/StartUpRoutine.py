from datetime import datetime, timedelta
from StoryEvents import storyEvents
from Zone import Zone
from Monster import Monster
import random

def build_first_time_checkin_messages(zone):
  """
    We want to build a dict that can be sent back to the client when they
    create a hero

    args:
      zone: an object of the zone model. We want to iterate through the
      zone options for where to go next

    return:
      a dict with two keys: 
        key1: messages: 
        value1: a list of messages to display at the user
        key2: zonePrompt:
        value2: a small list of dicts that the zone info that the user can
        choose
  """
  result = {}
  result['notices'] = []
  result['notices'].append(storyEvents['newUser'])
  result['notices'].append(zone.get_description())
  result['zonePrompt'] = zone.nextZoneReferenceList
  return result




def check_in_and_get_notices(heroId,accountId,checkinTimeUtc,utcOffset):
  """
    this should be called on page load and should be used to get any notices
    for the use

    args:
      heroId:
        we want a  pymongo objectId for the hero table
      accountId:
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
  hero = Hero.create_model_from_pk(heroId)
  account = Account.create_model_from_pk(accountId)

  lastCheckinTime = account.lastCheckInTime
  account.lastCheckInTime = checkinTimeUtc
  account.save_changes()

  if not lastCheckinTime:
    messages = build_first_time_checkin_messages(hero.zone)
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

  






