"""
  by combining all of these guys in a seperate module like this, it is easier
  to avoid circular references
"""

class BaseFields(object):
  COLLECTION_NAME = None
  PK_KEY = '_id'
  SESSION_KEY = 'login'
  LOGIN_PK_KEY = 'loginPk'
  ACCOUNT_PK_KEY = 'accountPk'
  HERO_PK_KEY = 'heroPk'


class AuthenticationFields:
  """
    Just a collection of strings that function as constants
  """
  COLLECTION_NAME = 'logins'
  USER_LOGIN = 'login'
  USER_PASSWORD = 'pw'
  USER_DESC = 'desc'

class AccountDbFields(BaseFields):
  COLLECTION_NAME = 'accounts'
  REMINDER_TIME = 'reminderTime'
  DAY_START = 'dayStart'
  DEATH_GOLD_PENALTY = 'deathGoldPenalty'
  HERO_LVL_PENALTY = 'heroLvlPenalty'
  ZONE_LVL_PENALTY = 'zoneLvlPenalty'
  PERMA_DEATH = 'permaDeath'
  STORY_MODE_IS_ON = 'storyModeIsOn'
  LAST_CHECKIN_TIME = 'lastCheckinTime'
  PUBLIC_ACCOUNT = 'publicAccount'
  PUBLIC_KEY = 'PublicKey'
  CREATE_DATE = 'creationDate'
  PREVENT_POPUPS = 'preventPopups'

class DailyDbFields(BaseFields):
  COLLECTION_NAME = 'dailies'
  NAME = 'name'
  NOTE = 'note'
  URGENCY = 'urgency'
  DIFFICULTY = 'difficulty'
  TRIGGER_PERIOD_LENGTH = 'triggerPeriodLength'
  DAYS_UNTIL_TRIGGER = 'daysUntilTrigger'
  SORT_KEY = 'sortKey'
  ACTIVE_DAYS = 'activeDays'
  PUBLIC_KEY = 'PublicKey'


class HeroDbFields(BaseFields):
  COLLECTION_NAME = 'heros'
  SHIP_NAME = 'shipName'
  LVL = 'lvl'
  GOLD = 'gold'
  MAX_HP = 'maxHp'
  NOW_HP = 'nowHp'
  MAX_XP = 'maxXp'
  NOW_XP = 'nowXp'
  ATTACK_LVL = 'attackLvl'
  DEFENSE_LVL = 'defenseLvl'
  ZONE_VISIT_COUNTS = 'zoneVisitCounts'
  PUBLIC_KEY = 'PublicKey'
  ZONE = 'zone'
  MONSTER = 'monster'


class StoryDbFields(BaseFields):
  NAME = 'name'
  DESCRIPTION = 'description'
  DEFINITION_KEY = 'definitionKey'

class MonsterDbFields(StoryDbFields):
  COLLECTION_NAME = 'monsters'
  OWNER_COLLECTION = 'heros'
  OWNER_PROPERTY = HeroDbFields.MONSTER #key in the Hero dict
  BASE_HP = 'baseHp'
  NOW_HP = 'nowHP'
  MAX_HP = 'maxHp'
  LVL = 'lvl'
  BASE_XP_REWARD = 'baseXpReward'
  TRASURE_DROP_RATE = 'treasureDropRate'
  MAX_GOLD_DROP_PER_LVL = 'maxGoldDrop'
  TRASURE_DROPS = 'treasureDrops'
  ZONE_KEY = 'zoneKey'
  ATTACK_LVL = 'attackLvl'
  DEFENSE_LVL = 'defenseLvl'


class ZoneDBFields(StoryDbFields):
  COLLECTION_NAME = 'zones'
  OWNER_COLLECTION = 'heros'
  OWNER_PROPERTY = HeroDbFields.ZONE #key in the Hero dict
  FULL_NAME = 'fullName'
  ALIASES = 'aliases'
  MONSTERS_KILLED = 'monstersKilled'
  MAX_MONSTERS = 'maxMonsters'
  LVL = 'lvl'
  PREVIOUS_ZONE_REFERENCE_PK = 'previousZoneReferencePK'
  NEXT_ZONE_REFERENCE_LIST = 'nextZoneReferenceList'
  SUFFIX = 'suffix'
  HERO_ID = 'heroId'

class ZoneGroupFields:
  LVL_0 = 'lvl0Zones'
  LVL_1 = 'lvl1Zones'
  LVL_5 = 'lvl5Zones'
  LVL_10 = 'lvl10Zones'
  LVL_15 = 'lvl15Zones'
  LVL_20 = 'lvl20Zones'
  LVL_25 = 'lvl25Zones'
  LVL_30 = 'lvl30Zones'

class ZoneDefinitionFields:
  ALL = 'all'
  HOME = 'home'
  GAS = 'gas'
  EMPTY_SPACE = 'emptySpace'
  NEBULA = 'nebula'
  SAFE_SPACE = 'safeSpace'
  ASTEROID_FIELD = 'asteroidField'
  SOLAR = 'solar'
  UNCHARTED = 'uncharted'
  BACKWATER = 'backwater'
  GARBAGE_BALL = 'garbageBall'
  CAVE = 'cave'
  DEFENSE = 'defense'
  RESORT = 'resort'
  METROPOLIS = 'metropolis'
  TEMPLE = 'spaceTemple'
  INFESTATION = 'infestation'
  GREY = 'grey'
  MALESTERIUM = 'malesterium'
  SKY = 'sky'
  PSYCHEDELIC = 'psychedelic'
  OCEAN = 'ocean'
  WEB = 'web'
  NO_MOON = 'noMoon'
  WARP = 'warp'
  EVENT_HORIZON = 'eventHorizon'
  WORLD_END = 'worldEnd'
  HELL = 'hell'
  BEGINNING = 'beginning'
  INFINITE = 'infinite'

class MonsterDefinitionFields:
  MECH = 'mech'
  PIRATES = 'pirate'
  M_SCOUT = 'mScout'
  SMALL_ASTEROID = 'smallasteroid'
  SPACE_SLIME = 'spaceslime'
  SPACEMAN = 'spaceman'
  CLOUD_FORTRESS = 'cloudfortress'
  POISON_CLOUD = 'poisonCloud'
  DREAD_PIRATES = 'dreadPirates'
  GRAVITY_HOLE = 'gravityHole'
  SPACE_PARASITES = 'spaceParasites'
  ZOMBIE_FREIGHTER = 'zombieFreighter'
  BIG_ASTEROID = 'bigAsteroid'
  MINER = 'miner'
  AMBUSH_PIRATES = 'ambushpirates'
  SPACE_GOLEM = 'spacegolem'
  MOTHS = 'moths'
