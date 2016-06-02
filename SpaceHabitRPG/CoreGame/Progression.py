import ZoneLookup
from datetime import datetime
import random
from Zone import Zone
from Account import *
from Hero import *


def start_account(accountId,heroName,shipName):
    account = Account(id = create_new_account(heroName))
    hero = Hero(id = create_new_hero(shipName))
    account.assign_heroId(hero.id)
    account.save_changes()





def define_zone(heroLvl,vistiedZones,firstZone = False):
    zones = get_unlocked_zones(heroLvl)
    selectedZone = random.choice(zones)
    zoneName = selectedZone['zoneType']
    if selectedZone['key'] in vistiedZones:
        zoneName += (" " + generate_zone_name_suffix(vistiedZones[selectedZone['key']]))
        vistiedZones[selectedZone['key']] += 1
    zonelvl = heroLvl
    if not firstZone:
        lvlOffset = 10
        heroLvl = 0 if heroLvl - lvlOffset < 1 else heroLvl
        lvlAdjustment = random.randint(heroLvl -lvlOffset,heroLvl +lvlOffset)
        zoneLvl + lvlAdjustment
        

def generate_zone_name_suffix(visitCount):
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
    adjustedVisitCount = convert_number_to_naming_number_base(visitCount,len(symbols))
    while adjustedVisitCount > 0:
        r = adjustedVisitCount % len(symbols)
        adjustedVisitCount //= len(symbols)
        s = (symbols[r] + " " + s)

    if superSuffix > 0:
        s += str(superSuffix)
    return s.strip()

def convert_number_to_naming_number_base(num,base):
    """Numbers naturally want to follow this pattern:
    0,A,B,C,...,Y,Z,A0,AA,AB,AC,...,AY,AZ,B0,BA,BB,BC
    But I want zone suffix naming system to follow this pattern:
    0,A,B,C,...,Y,Z,AA,AB,AC,...,AY,AZ,BA,BB,BC,... 
    This function adjust numbers to fit the wanted pattern, 
    i.e. without the proverbial mulitples of 10
    The accuracy of this function becomes unreliable after base^2
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
    if heroLvl < 1:
        return []
    availableZones = []
    availableZones.extend(ZoneLookup.zones["lvl1Zones"])
    if heroLvl >= 5:
        availableZones.extend(ZoneLookup.zones["lvl5Zones"])
    if heroLvl >= 10:
        availableZones.extend(ZoneLookup.zones["lvl10Zones"])
    if heroLvl >= 15:
        availableZones.extend(ZoneLookup.zones["lvl15Zones"])
    if heroLvl >= 20:
        availableZones.extend(ZoneLookup.zones["lvl20Zones"])
    if heroLvl >= 25:
        availableZones.extend(ZoneLookup.zones["lvl25Zones"])
    if heroLvl >= 30:
        availableZones.extend(ZoneLookup.zones["lvl30Zones"])
    return availableZones


    

