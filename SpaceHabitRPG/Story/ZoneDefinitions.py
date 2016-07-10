from Defintions import Defintions
from  AllDBFields import ZoneDBFields
from AllDBFields import ZoneGroupFields
from AllDBFields import ZoneDefinitionFields




AllZones = {
  ZoneGroupFields.LVL_0:{
    ZoneDefinitionFields.HOME:{
      ZoneDBFields.ALIASES: [],
      ZoneDBFields.NAME: "Home Port",
      ZoneDBFields.DESCRIPTION: "Everyone's gotta start somewhere. For you it's the "
        "earth first space port. You may not be so good at the whole space "
        "frontiering yet but just remember, sucking at something is the first "
        "step to being sorta good at something."
    },
    },
  ZoneGroupFields.LVL_1: {
    ZoneDefinitionFields.GAS:{
      ZoneDBFields.ALIASES: ["Ao","Acidia","Cloropha","Harliqua"],
      ZoneDBFields.NAME: "Gas Planet Orbit",
      ZoneDBFields.DESCRIPTION: "This is a gas planet, that is, it's made of floating gas"
          " stuff. It's not liquid; otherwise, it would be a liquid planet. "
          "It's elements don't change state between liquid and gas like that "
          "whore of an element, water. It's all gas, 100% of the time. "
          "No compromising with liquids or solids! Compromise is how you fail "
          "at your good habits."
    },
    ZoneDefinitionFields.EMPTY_SPACE:{
      ZoneDBFields.ALIASES:["Free Space","Wild Space","Empty Space"],
      ZoneDBFields.NAME: "Empty Space",
      ZoneDBFields.DESCRIPTION: "Out here there is nothing but the vacuum of space"
        " -- it kinda sucks. Speaking of vacuums, have you cleaned "
        "your room recently?"
    },
    ZoneDefinitionFields.NEBULA:{
      ZoneDBFields.ALIASES: ["The Crab Nebula","The Mushroom Nebula",
                "The Batman Nebula","The Eifel Tower Nebula"],
      ZoneDBFields.NAME: "Nebula",
      ZoneDBFields.DESCRIPTION: "These are like giant space clouds. Scientists "
        "speculate that they were created by the angels and their nicotine "
        "addiction. This explains both the existence of nebulas and why we "
        "don't see angels anymore. They were killed off by lung cancer which "
        "is what's gonna happen to you if you don't put out that spacedamned "
        "cigarette!"
    },
    ZoneDefinitionFields.SAFE_SPACE:{
      ZoneDBFields.ALIASES: ["Galactic Trade Zone","Commercial Space Trade Rout"],
      ZoneDBFields.NAME: "Safe Space",
      ZoneDBFields.DESCRIPTION: "Here in safe space, they enforce even the small "
        "rules like spacejaywalking. Afterall, if you can't enforce the simple "
        "laws, how do you expect to enforce the more complicated laws. In the "
        "same way, if you aren't doing your small tasks, how do you expect to "
        "ever accomplish the more complicated tasks in your life."
    }
  },
  ZoneGroupFields.LVL_5: {
    ZoneDefinitionFields.ASTEROID_FIELD:{
      ZoneDBFields.ALIASES: ["Asteroid Field"],
      ZoneDBFields.NAME: "Asteroid Field",
      ZoneDBFields.DESCRIPTION: "Supposedly, odds are 725 to 1 that the asteroid belt "
        "is going to spank you. Switch those odds around and you have the "
        "probability that your spouse is gonna spank you if you don't loose "
        "that extra fifteen pounds."
    },
    ZoneDefinitionFields.SOLAR:{
      ZoneDBFields.ALIASES: ["capricorn"],
      ZoneDBFields.NAME: "Solar Orbit",
      ZoneDBFields.DESCRIPTION: ""
    },
    ZoneDefinitionFields.UNCHARTED:{
      ZoneDBFields.NAME: "Uncharted Planet Orbit",
      ZoneDBFields.DESCRIPTION: ""
    },
    ZoneDefinitionFields.BACKWATER:{
      ZoneDBFields.NAME: "Backwater Planet Orbit",
      ZoneDBFields.DESCRIPTION: ""
    }
  },
  ZoneGroupFields.LVL_10: {
    ZoneDefinitionFields.GARBAGE_BALL:{
      ZoneDBFields.ALIASES: ["The Calcutta Space Heap","The Floridian Shit Glob","The Myanis Refuse Dump"],
      ZoneDBFields.NAME: "Giant Space Garbage Ball Orbit",
      ZoneDBFields.DESCRIPTION: "The giant space garbage ball didn't start off as a giant "
        "garbage ball. It was once a tiny space garbage ball but through the "
        "bad habits of man, it kept growing and growing. Let this be a lesson "
        "to you: bad habits turn tiny space garbage balls into giant space "
        "garbage balls."
    },
    ZoneDefinitionFields.CAVE:{
      ZoneDBFields.NAME: "Space Cave",
      ZoneDBFields.DESCRIPTION: ""
    },
    ZoneDefinitionFields.DEFENSE:{
      ZoneDBFields.NAME: "Defense Territory",
      ZoneDBFields.DESCRIPTION: ""
    },
    ZoneDefinitionFields.RESORT:{
      ZoneDBFields.NAME: "Resort Planet Orbit",
      ZoneDBFields.DESCRIPTION: "Look at all those spacedamned kids not working, not "
        "being productive. That's what you're probably thinking. But you're "
        "wrong. Sometimes we need to take a break from our labors so that we "
        "don't burn ourselves out. Use some of those goods you've been "
        "saving up for."
    }
  },
  ZoneGroupFields.LVL_15: {
    ZoneDefinitionFields.METROPOLIS:{
      ZoneDBFields.NAME: "Space Metropolis",
      ZoneDBFields.DESCRIPTION: ""
    },
    ZoneDefinitionFields.TEMPLE:{
      ZoneDBFields.NAME: "Space Temple",
      ZoneDBFields.DESCRIPTION: ""
    },
    ZoneDefinitionFields.INFESTATION:{
      ZoneDBFields.NAME: "Infestation Space",
      ZoneDBFields.DESCRIPTION: ""
    },
    ZoneDefinitionFields.GREY:{
      ZoneDBFields.NAME: "Grey World Orbit",
      ZoneDBFields.DESCRIPTION: ""
    }
  },
  ZoneGroupFields.LVL_20: {
    ZoneDefinitionFields.MALESTERIUM:{
      ZoneDBFields.NAME: "Malesterium Fortress World",
      ZoneDBFields.DESCRIPTION: ""
    },
    ZoneDefinitionFields.SKY:{
      ZoneDBFields.NAME: "Sky Planet Orbit",
      ZoneDBFields.DESCRIPTION: ""
    },
    ZoneDefinitionFields.PSYCHEDELIC:{
      ZoneDBFields.NAME: "Psychedelic Space",
      ZoneDBFields.DESCRIPTION: ""
    },
    ZoneDefinitionFields.OCEAN:{
      ZoneDBFields.NAME: "Space Ocean",
      ZoneDBFields.DESCRIPTION: ""
    }
  },
  ZoneGroupFields.LVL_25: {
    ZoneDefinitionFields.WEB:{
      ZoneDBFields.NAME: "Digital Disruption Web",
      ZoneDBFields.DESCRIPTION: ""
    },
    ZoneDefinitionFields.NO_MOON:{
      ZoneDBFields.NAME: "'No Moon' Orbit",
      ZoneDBFields.DESCRIPTION: ""
    },
    ZoneDefinitionFields.WARP:{
      ZoneDBFields.NAME: "Warp Dimension",
      ZoneDBFields.DESCRIPTION: ""
    },
    ZoneDefinitionFields.EVENT_HORIZON:{
      ZoneDBFields.NAME: "Event Horizon",
      ZoneDBFields.DESCRIPTION: ""
    }
  },
  ZoneGroupFields.LVL_30: {
    ZoneDefinitionFields.WORLD_END:{
      ZoneDBFields.NAME: "End of the World",
      ZoneDBFields.DESCRIPTION: ""
    },
    ZoneDefinitionFields.HELL:{
      ZoneDBFields.NAME: "Hell Dimension",
      ZoneDBFields.DESCRIPTION: ""
    },
    ZoneDefinitionFields.BEGINNING:{
      ZoneDBFields.NAME: "Beginning of Time",
      ZoneDBFields.DESCRIPTION: ""
    },
    ZoneDefinitionFields.INFINITE:{
      ZoneDBFields.NAME: "Infinite Improbability Zone",
      ZoneDBFields.DESCRIPTION: ""
    }
  }

}


class ZoneDefinition(Defintions):
  """
    this class will function as a sort of pointer to a zone in the 
    allZones dict. It's needed in case, I need to change one of these
    properties globally. Each model of zone will have one of these.
  """

  global AllZones
  _indexes = {
      ZoneDefinitionFields.HOME: 
        AllZones[ZoneGroupFields.LVL_0][ZoneDefinitionFields.HOME],
      ZoneDefinitionFields.GAS: 
        AllZones[ZoneGroupFields.LVL_1][ZoneDefinitionFields.GAS],
      ZoneDefinitionFields.EMPTY_SPACE: 
        AllZones[ZoneGroupFields.LVL_1][ZoneDefinitionFields.EMPTY_SPACE],
      ZoneDefinitionFields.NEBULA: 
        AllZones[ZoneGroupFields.LVL_1][ZoneDefinitionFields.NEBULA],
      ZoneDefinitionFields.SAFE_SPACE: 
        AllZones[ZoneGroupFields.LVL_1][ZoneDefinitionFields.SAFE_SPACE],
      ZoneDefinitionFields.ASTEROID_FIELD: 
        AllZones[ZoneGroupFields.LVL_5][ZoneDefinitionFields.ASTEROID_FIELD],
      ZoneDefinitionFields.SOLAR: 
        AllZones[ZoneGroupFields.LVL_5][ZoneDefinitionFields.SOLAR],
      ZoneDefinitionFields.UNCHARTED: 
        AllZones[ZoneGroupFields.LVL_5][ZoneDefinitionFields.UNCHARTED],
      ZoneDefinitionFields.BACKWATER: 
        AllZones[ZoneGroupFields.LVL_5][ZoneDefinitionFields.BACKWATER],
      ZoneDefinitionFields.GARBAGE_BALL: 
        AllZones[ZoneGroupFields.LVL_10][ZoneDefinitionFields.GARBAGE_BALL],
      ZoneDefinitionFields.CAVE: 
        AllZones[ZoneGroupFields.LVL_10][ZoneDefinitionFields.CAVE],
      ZoneDefinitionFields.DEFENSE: 
        AllZones[ZoneGroupFields.LVL_10][ZoneDefinitionFields.DEFENSE],
      ZoneDefinitionFields.RESORT: 
        AllZones[ZoneGroupFields.LVL_10][ZoneDefinitionFields.RESORT],
      ZoneDefinitionFields.METROPOLIS: 
        AllZones[ZoneGroupFields.LVL_15][ZoneDefinitionFields.METROPOLIS],
      ZoneDefinitionFields.TEMPLE: 
        AllZones[ZoneGroupFields.LVL_15][ZoneDefinitionFields.TEMPLE],
      ZoneDefinitionFields.INFESTATION:
        AllZones[ZoneGroupFields.LVL_15][ZoneDefinitionFields.INFESTATION],
      ZoneDefinitionFields.MALESTERIUM:
        AllZones[ZoneGroupFields.LVL_20][ZoneDefinitionFields.MALESTERIUM],
      ZoneDefinitionFields.SKY: 
        AllZones[ZoneGroupFields.LVL_20][ZoneDefinitionFields.SKY],
      ZoneDefinitionFields.PSYCHEDELIC: 
        AllZones[ZoneGroupFields.LVL_20][ZoneDefinitionFields.PSYCHEDELIC],
      ZoneDefinitionFields.OCEAN: 
        AllZones[ZoneGroupFields.LVL_20][ZoneDefinitionFields.OCEAN],
      ZoneDefinitionFields.WEB: 
        AllZones[ZoneGroupFields.LVL_25][ZoneDefinitionFields.WEB],
      ZoneDefinitionFields.NO_MOON:
        AllZones[ZoneGroupFields.LVL_25][ZoneDefinitionFields.NO_MOON],
      ZoneDefinitionFields.WARP: 
        AllZones[ZoneGroupFields.LVL_25][ZoneDefinitionFields.WARP],
      ZoneDefinitionFields.EVENT_HORIZON: 
        AllZones[ZoneGroupFields.LVL_25][ZoneDefinitionFields.EVENT_HORIZON],
      ZoneDefinitionFields.WORLD_END: 
        AllZones[ZoneGroupFields.LVL_30][ZoneDefinitionFields.WORLD_END],
      ZoneDefinitionFields.HELL: 
        AllZones[ZoneGroupFields.LVL_30][ZoneDefinitionFields.HELL],
      ZoneDefinitionFields.BEGINNING: 
        AllZones[ZoneGroupFields.LVL_30][ZoneDefinitionFields.BEGINNING],
      ZoneDefinitionFields.INFINITE: 
        AllZones[ZoneGroupFields.LVL_30][ZoneDefinitionFields.INFINITE],
    }



  def get_aliases(self):
    return self._indexes[self._key][ZoneDBFields.ALIASES]

