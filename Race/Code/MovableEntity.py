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

    self.setMovable(True)

    # Direction
    self.direction='E'

    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":Fin")

  ### Movement Management
  ##  Handles updating entity position and hitbox 
  def update(self):
    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":update")
    displacement=self.movement_controls.calcDisplacement(self.getSpeed(), self.direction)
    self.updatePosition(displacement)
    self.updateHitbox() 
    
    if (self.DEBUG == 1):
      displacement.printPos()

  def rotateEast(self):
    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":rotateEast")
    self.direction='E'

  def rotateWest(self):
    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":rotateWest")
    self.direction='W'

  ### end : Movement Management
