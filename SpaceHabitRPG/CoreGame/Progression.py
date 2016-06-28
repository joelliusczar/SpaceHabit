"""
  this module handles all all of the tracking for progress in the story mode
"""

from datetime import datetime
from Zone import Zone
from Account import *
from Hero import *
import ZoneDefinitions
import random


def start_account(accountId,heroName,shipName):
  account = Account(id = create_new_account(heroName))
  hero = Hero(id = create_new_hero(shipName))
  account.assign_heroId(hero.id)
  account.save_changes()


def get_intro_if_new_hero(heroId):
  """
    this checks the database for a particular character and determines if this 
    is a new character and if we need to go through the new game schtick

    args:
      heroId:
        we want a  pymongo objectId for the hero table

    returns:
      if it is a new hero we return a dict with two elements: 'story' which 
      is a huge thing of text and 'zoneChoice' which is a list of dicts each
      of which contain 'zoneId','description'
      but if it's a returning user, we just return None

  """
  collection = DatabaseLayer.get_table(HeroFields.COLLECTION_NAME)
  hero = Hero(None,heroId)
  if Hero.hasLeftPort:
    return None
  zones = []
  zones[0] = define_zone(hero.lvl,hero.zoneVisitCounts,True)
  zones[1] = define_zone(hero.lvl,hero.zoneVisitCounts)
  zones[2] = define_zone(hero.lvl,hero.zoneVisitCounts)



def define_zone(heroLvl,vistiedZones,matchHeroLvl = False):

  """
    generates a zone with unique name and randomlvl

    args:
      heroLvl:
        this should be a positive integer greater than 1
      visitedZones:
        this should be a dict. the dict is used to keep tract of which
        name suffix combinations have popped up already.
      matchHeroLvl: 
        Set this to true if first level.if this is true than the zone 
        difficulty level will perfectly match the hero's level rather than
        approximate it.
        
    returns:
      a model of type zone
      also adds to the value for a key in the visitedZones dict
  """
  zone = select_random_zone_from_definitions(heroLvl)
  if zone.definitionKey in vistiedZones: #if we've visited it before
    zone.zoneName += (" " + generate_zone_name_suffix(vistiedZones[zone.definitionKey]))
    vistiedZones[zone.definitionKey] += 1
  else:
    vistiedZones[zone.definitionKey] = 1
  if not matchHeroLvl:
    zone.skillLvl = calculate_zone_lvl(heroLvl)
  return zone

def get_port_zone():
  """
    this probably only needs to be called when a new hero is being created for
    a user

    returns:
      a model of type zone with starting details
  """
  zone = Zone()
  zone.definitionKey = "port"
  zone.zoneName = "Space Port"

def select_random_zone_from_definitions(heroLvl):
  """
    creates a model of zone from a randomly selected definition

    args:
      heroLvl:
        this should be a positive integer greater than 1
      returns:
        a model of type zone
  """
  zones = get_unlocked_zones(heroLvl)
  selectedZone = random.choice(zones)
  zone = Zone()
  zone.zoneName = selectedZone['name']
  zone.definitionKey = selectedZone['key']
  zone.description = selectedZone['description']
  zone.skillLvl = heroLvl
  zone.maxMonsters = random.randint(5,15) 
  return zone

def calculate_zone_lvl(heroLvl):
  """
    calculates the lvl for the zone based on the hero level

    args:
      heroLvl:
        this is a positive integer. Not much to say here.

      returns:
        this is an integer. The return value should be at least 10 less than 
        heroLvl and at most 10 greater than heroLvl. It should also be at least 1.
  """
  zonelvl = heroLvl
  lvlOffset = 10
  lvlAdjLowBound = 0
  if heroLvl <= lvlOffset:
    lvlAdjLowBound = -heroLvl +1
  else:
    lvlAdjLowBound = - lvlOffset
  lvlAdjustment = random.randint(lvlAdjLowBound,lvlOffset)
  zonelvl += lvlAdjustment
  return zonelvl

    

def generate_zone_name_suffix(visitCount):
  """
    each time we visit a particular zone type, we don't want it to have
    the same exact name as last time. To do this, we will add a suffix to
    the name. This generates a suffic based on the number of times
    that zone has been hit.

    args:
      visitCount:
        the number of times the hero character has visited a zone
        s
    returns:
      a suffix which will be a string. We will take this string and append
      it to stuff.
  """

  if visitCount < 1:
    return ""
  """if you add any items to symbols, please adjust the unit test
   to account for that"""
  symbols =["","Alpha", "Beta","Cain","Delta", #4
      "Epsilon","Foxtrot","September","October", #8
      "November","Kilo","Juliett","Romeo","Silver","Deckard", #14
      "Sierra","Tango","Zeta","Theta","July","Ludwig","Tyrell", #21
      "Lambda","Mu","London","Victor","Quintin","Gold", #27 
      "Whiskey","Xray","Zulu","Pi","Rho","Antilles","Blanca", #34
      "Sigma","Tau","India","Hector","Quebec","Waltz","Sapphire", #41
      "Tokyo","Ramesses","Washington","Darius","Emerald","Midgard", #47
      "Futura","Charlotte","Flanders","Berlin","Onion","Ruby", #53
      "David","Pizza","Lazlo","Kong","Jerico","Diamond", #59
      "Black","White","Olaf","Biggs","Wedge","Tyrannus", #65
      "Richter","Medusa","Swan","Gemini","Noir","Xerxes",#71
      "TNT","Plutonia","Cerberus","Tiberius", #75
      "Arcturus","Prime","Tarsonis","Babylon","Sparta",#80
      "Atlanta","Yutani","Python","Ridley","Midway", #85
      "Bismark","Dextera","Dominus","Jejunum", #89
      "Superior","Distal","Eurebus","Indigo", #93
      "Xs","Rex","Titan","Zen","Apex","Omega","Zed"] #100
  s = ""
  superSuffix = 0
  if visitCount > (len(symbols)-1) * len(symbols):
    symbols[0] = "?4815162342"
    #the -1 on the first array length is to account for the single symbol range of items
    superSuffix = visitCount // ((len(symbols)-1) * len(symbols)) + 1 #+1 because the 1 suffix would be redundant
    visitCount = visitCount % ((len(symbols)-1) * len(symbols)) 
  adjustedVisitCount = offset_number_for_base(visitCount,len(symbols))
  while adjustedVisitCount > 0:
    r = adjustedVisitCount % len(symbols)
    adjustedVisitCount //= len(symbols)
    s = (symbols[r] + " " + s)

  if superSuffix > 0:
    s += str(superSuffix)
  return s.strip()

def offset_number_for_base(num,base):
  """
    Numbers naturally want to follow this pattern:
    0,A,B,C,...,Y,Z,A0,AA,AB,AC,...,AY,AZ,B0,BA,BB,BC
    But I want zone suffix naming system to follow this pattern:
    0,A,B,C,...,Y,Z,AA,AB,AC,...,AY,AZ,BA,BB,BC,... 
    This function adjust numbers to fit the wanted pattern, 
    i.e. without the proverbial mulitples of 10
    The accuracy of this function becomes unreliable after base^2

    args:
      num:
        this is the number that we're offsetting.
      base:
        an integer. multiples of this number will be skipped

    returns:
      a number that's been offset for the base occurances skipped over

  """
  if base < 1 or not float.is_integer(float(base)):
    raise ValueError("Base needs to be a positive non-zero integer")
  if not float.is_integer(float(num)):
    raise ValueError("num needs to be an integer and not a floating number")
  isNegative = False
  if num < 0:
    num *= -1
    isNegative = True
  adjusterNum = num + (num // base)
  return num + (adjusterNum // base)


def get_unlocked_zones(heroLvl):
  """"
    gets the list of availible zones that can be selected depeding on the 
    hero's level

    args:
      heroLvl:
        this should be an interger 
    returns:
      a list of dicts that contain zone info.
  """
  if heroLvl < 1:
    return []
  availableZones = []
  availableZones.extend(ZoneDefinitions.zones["lvl1Zones"])
  if heroLvl >= 5:
    availableZones.extend(ZoneDefinitions.zones["lvl5Zones"])
  if heroLvl >= 10:
    availableZones.extend(ZoneDefinitions.zones["lvl10Zones"])
  if heroLvl >= 15:
    availableZones.extend(ZoneDefinitions.zones["lvl15Zones"])
  if heroLvl >= 20:
    availableZones.extend(ZoneDefinitions.zones["lvl20Zones"])
  if heroLvl >= 25:
    availableZones.extend(ZoneDefinitions.zones["lvl25Zones"])
  if heroLvl >= 30:
    availableZones.extend(ZoneDefinitions.zones["lvl30Zones"])
  return availableZones


  

