# WallSegment.py
# Manipulates/Creates the Wall object in the game world

# Imports
import pygame

# Class imports
from Entity import *

# Debug info
DEBUG=1
DEBUG_TAG="[WallSegment]"

class WallSegment(Entity):
  'Manipulates/Creates the Wall object in the game world'

  # Wall(self, start, close)
  # Begins the build process of the Wall
  def __init__(self, x, y, ppm):
    if (DEBUG == 1):
      print(DEBUG_TAG + ":init:" + str(x) + ":" + str(y))
    Entity.__init__(self, x, y, 'w', ppm)
    
  # printWall(self)
  # Prints the positions of the wall
  def printWall(self):
    print(DEBUG_TAG + ":printWall")
    print("[" + str(self.hitbox.left) + "->" + str(self.hitbox.right) + "],[" + str(self.hitbox.top) + "->" + str(self.hitbox.bottom) + "]")
