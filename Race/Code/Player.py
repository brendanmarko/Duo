# Player.py
# Manages the properties and actions of the Player

# Imports
from MovableEntity import *

# Debug info
DEBUG=1
DEBUG_TAG="[Player]"

class Player(MovableEntity):
  'Manages the properties and actions of the Player'
  
  # Player(self, x, y)
  # Initializes Player with position[x,y]
  def __init__(self, x, y, ppm):    
    self.object_type='p'
    MovableEntity.__init__(self, x, y, self.object_type, ppm)
