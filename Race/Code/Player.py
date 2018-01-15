# Player.py
# Manages the properties and actions of the Player

# Imports
from MovableEntity import *

class Player(MovableEntity):
  'Manages the properties and actions of the Player'
  
  # Player(self, x, y)
  # Initializes Player with position[x,y]
  def __init__(self, x, y, ppm):    

    # Debug info
    self.DEBUG=1
    self.DEBUG_TAG="[Player]"

    self.object_type='p'
    MovableEntity.__init__(self, x, y, self.object_type, ppm)

  def tester(self):
    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":test")
    return "test"
