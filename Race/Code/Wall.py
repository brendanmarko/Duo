# Wall.py
# Manipulates/Creates the Wall object in the game world

# Imports
import pygame

# Debug info
DEBUG=1
DEBUG_TAG="[Wall]"

class Wall(object):
  'Manipulates/Creates the Wall object in the game world'

  # collisionCheck(self, pos)
  # Checks if an object is colliding with the Wall
  def collisionCheck(self, pos):
    if (DEBUG == 1):
      print(DEBUG_TAG + ":collisionCheck")

    # No row/column collision occured
    return 0;
    
  # printWall(self)
  # Prints the positions of the wall
  def printWall(self):
    print(DEBUG_TAG + ":printWall")
    print("[" + str(self.hitbox.left) + "->" + str(self.hitbox.right) + "],[" + str(self.hitbox.top) + "->" + str(self.hitbox.bottom) + "]")

  # getHitbox(self):
  # Returns the Rect box that denotes a Wall
  def getHitbox(self):
    return self.hitbox

  # Wall(self, start, close)
  # Begins the build process of the Wall
  def __init__(self, x, y, span_x, span_y):
    if (DEBUG == 1):
      print(DEBUG_TAG + ":init:" + str(x) + ":" + str(y) + ":" + str(span_x) + ":" + str(span_y))

    # Build Wall (L, T, W, H)
    self.hitbox=pygame.Rect(x, y, span_x, span_y)
