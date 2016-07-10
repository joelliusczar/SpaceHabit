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

class AccountFields(BaseFields):
  COLLECTION_NAME = 'accounts'
  REMINDER_TIME = 'reminderTime'
  DAY_START = 'dayStart'
  DEATH_GOLD_PENALTY = 'deathGoldPenalty'
  HERO_LVL_PENALTY = 'heroLvlPenalty'
  ZONE_LVL_PENALTY = 'zoneLvlPenalty'
  ENEMY_HEALED_ON_ATTACK = 'enemyHealedOnAttack'
  SELF_HEALED_ON_ATTACK = 'selfHealedOnAttack'
  PERMA_DEATH = 'permaDeath'
  STORY_MODE_IS_ON = 'storyModeIsOn'
  LAST_CHECKIN_TIME = 'lastCheckinTime'
  PUBLIC_ACCOUNT = 'publicAccount'
  PUBLIC_KEY = 'PublicKey'
  CREATE_DATE = 'creationDate'

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
  IS_IN_ZONE_LIMBO = 'isInZoneLimbo'
  ZONE = 'zone'
  MONSTER = 'monster'


class MonsterFields(BaseFields):
  COLLECTION_NAME = 'monsters'
  OWNER_COLLECTION = 'heros'
  NAME = 'name'
  BASE_HP = 'baseHp'
  NOW_HP = 'nowHP'
  MAX_HP = 'maxHp'
  LVL = 'lvl'
  DESCRIPTION = 'description'
  BASE_XP_REWARD = 'baseXpReward'
  TRASURE_DROP_RATE = 'treasureDropRate'
  TRASURE_DROPS = 'treasureDrops'
  DEFINITION_KEY = 'definitionKey'
  ZONE_KEY = 'zoneKey'
  ATTACK_LVL = 'attackLvl'
  DEFENSE_LVL = 'defenseLvl'


class ZoneDBFields(BaseFields):
  COLLECTION_NAME = 'zones'
  OWNER_COLLECTION = 'heros'
  NAME = 'name'
  FULL_NAME = 'fullName'
  DESCRIPTION = 'description'
  ALIASES = 'aliases'
  MONSTERS_KILLED = 'monstersKilled'
  MAX_MONSTERS = 'maxMonsters'
  LVL = 'lvl'
  PREVIOUS_ZONE_REFERENCE = 'previousZoneReference'
  NEXT_ZONE_REFERENCE_LIST = 'nextZoneReferenceList'
  SUFFIX = 'suffix'
  DEFINITION_KEY = 'definitionKey'
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
