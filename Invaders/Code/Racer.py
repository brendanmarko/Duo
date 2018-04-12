# Racer.py
# Manages the properties and actions of a Racer

# Imports
from MovableEntity import *

# Debug info
DEBUG=1
DEBUG_TAG="[Racer]"

class Racer(MovableEntity):
  'Manages the properties and actions of a Racer'

  # Racer(self, x, y)
  # Initializes Racer with position[x,y]
  def __init__(self, x, y, ppm):
    self.object_type='r'
    MovableEntity.__init__(self, x, y, self.object_type, ppm)
