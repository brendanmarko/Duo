# MovableEntity.py; entities with the ability to move

# Imports
from Entity import *
from MovementHandler import *

class MovableEntity(Entity):
  'This class represents entities with the ability to move'

  def __init__(self, x, y, object_type, ppm):
    # Debug info
    self.DEBUG=1
    self.DEBUG_TAG="[MovableEntity]"

    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":Constructor")

    self.movement_controls=MovementHandler()
    Entity.__init__(self, x, y, object_type, ppm)

    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":Fin")
