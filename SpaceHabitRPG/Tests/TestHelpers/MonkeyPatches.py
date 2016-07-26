import random

testRandomNum = 0
testRandomIterDict = {}
testZoneGroup = "lvl1Zones"
random_choice = random.choice
random_randint = random.randint

def mock_randint(lowerBound,upperBound):
  """
    this will be used to replace the default random.randint method.
    We need a test method that will act consistently.

    args:
      lowerBound:
        this should be the mininum value that this method can return
      upperBound:
        this should be the maximum value that this method can return

    returns:
      the global variable testRandomNum
  """
  global testRandomNum
  if testRandomNum < lowerBound or testRandomNum > upperBound:
    raise OverflowError("out of bounds")
  testRandomNum += 1
  return testRandomNum -1


def mock_choice_first_index(array):
  """
    this will be used to replace the default random.choice method.
    We need a test method that will act consistently.

    args:
      array:
        figure it out!
    returns:
      the first item from the input array
  """
  s = sorted(array)
  return s[0]


def mock_choice(array):
  
  s = sorted(array)
  global testZoneGroup
  if s[0] == "lvl1Zones":
    return testZoneGroup

  global testRandomIterDict
  if not s[0] in testRandomIterDict:
    testRandomIterDict[s[0]] = iter(s)

  return next(testRandomIterDict[s[0]])


def set_mock_choice():
  random.choice = mock_choice

def set_mock_choice_first_index():
  random.choice = mock_choice_first_index

def set_mock_randint():
  random.randint = mock_randint

def reset_choice():
  random.choice = random_choice

def reset_randint():
  random.randint = random_randint



