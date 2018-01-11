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

    # Movable flag and speed
    self.setMovable(True)
    self.speed=self.getInfo().getSpeed()

    # Direction
    self.move_direction='E'

    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":Fin")

  ##### Speed
  def getSpeed(self):
    return self.speed

  ##### end : Speed

  ##### Movement Management
  ##  Handles updating entity position and hitbox 
  def update(self):
    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":update")
    displacement=self.movement_controls.calcDisplacement(self.getSpeed(), self.move_direction)
    self.updatePosition(displacement)
    self.updateHitbox() 
    
    if (self.DEBUG == 1):
      displacement.printPos()

  def moveE(self):
    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":moveE")
    self.move_direction='E'

  def moveW(self):
    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":moveW")
    self.move_direction='W'
  
  def moveN(self):
    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":moveN")
    self.move_direction='N'

  def moveS(self):
    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":moveS")
    self.move_direction='S'
  ##### end : Movement Management
