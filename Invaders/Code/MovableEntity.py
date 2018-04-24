# MovableEntity.py; entities with the ability to move

# Imports
from Entity import *
from MovementHandler import *
  
DEBUG=1

class MovableEntity(Entity):
  'This class represents entities with the ability to move'

  def __init__(self, pos, object_type):

    if (DEBUG == 1):
      print("[MovableEntity]:init")

    self.mover=MovementHandler()
    Entity.__init__(self, pos, object_type)
    self.setMovable(True)

    # Speed and direction
    self.speed=self.info.getSpeed()
    self.direction='E'

  ### Direction helpers
  ### Set direction
  def setDirection(self, new_dir):
    self.direction=new_dir

  def getDirection(self):
    return self.direction

  # Update wrt movement changes
  def update(self):
    if (DEBUG == 1):
      print("[MovableEntity]:update")
    displacement=self.mover.calcDisplacement(self.direction, self.speed) 
    self.updatePosition(displacement)

  # Rotation by direction helpers
  def rotateE(self):
    if (DEBUG == 1):
      print("[MovableEntity]:rotateE")
    self.direction='E'

  def rotateW(self):
    if (DEBUG == 1):
      print("[MovableEntity]:rotateW")
    self.direction='W'

  def rotateS(self):
    if (DEBUG == 1):
      print("[MovableEntity]:rotateS")
    self.direction='S'

  def rotateN(self):
    if (DEBUG == 1):
      print("[MovableEntity]:rotateN")
    self.direction='N'

  # Speed helpers
  def getSpeed(self):
    return self.speed

  def setSpeed(self, new_speed):
    self.speed=new_speed
