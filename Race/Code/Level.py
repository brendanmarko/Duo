# Level.py
# Stores Groups of game objects wrt a given level

class Level(object):

  # Level(walls, entities)
  # Creates a Level given two input lists
  def __init__(self, walls, entities, points_of_interest):
    'Stores Groups of game objects wrt a given level'

    # Debug Info
    self.DEBUG=1
    self.DEBUG_TAG="[Level]"  

    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":Constructor")

    # Populate level groups
    self.list_w=walls
    self.list_e=entities
    self.list_p=points_of_interest

  def __repr__(self):
    return self.DEBUG_TAG + ":toString"

  def getPOIs(self):
    return self.list_p

  def getWalls(self):
    return self.list_w

  def getEntities(self):
    return self.list_e

  def buildLevel(self, walls, entities, endpoints):
    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":buildLevel")
     
