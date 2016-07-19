import random


def calculate_lvl(lvl,offset):
  """
    calculates the lvl for an obstacle given an imput

    args:
      lvl:
        this is a positive integer. Not much to say here.
      offset:
        this needs to be a positive integer. It's used to calculate the range 
        of output values, i.e. max and min.

      returns:
        this is an integer. The return value should be at least lvl -offset or 0
        and at most lvl + offset
  """
  outputLvl = lvl
  lvlOffset = offset
  lvlAdjLowBound = 0
  if lvl <= lvlOffset:
    lvlAdjLowBound = -lvl +1
  else:
    lvlAdjLowBound = - lvlOffset
  lvlAdjustment = random.randint(lvlAdjLowBound,lvlOffset)
  outputLvl += lvlAdjustment
  return outputLvl

def adjust_timestamp_from_js_to_python(jsTimestamp):
  """
    javascript and python produce slightly different POSIX timestamps.
    This converts the javascript timestamps to python.
    args:
      jsTimestamp:
        this should come from the client. It will probably be the output
        of Date.now()
      returns:
        converted timestamp

  """
  
  return float(jsTimestamp)/1000


