# Player.py
# Manages the properties and actions of the Player

# Imports
from MovableEntity import *
from CharacterHandler import *

DEBUG=1
DEBUG_TAG="[Player]"

class Player(MovableEntity):
  'Manages the properties and actions of the Player'
  
  # Player(self, x, y)
  # Initializes Player with position[x,y]
  def __init__(self, pos, object_type):    
    MovableEntity.__init__(self, pos, object_type)
    self.controls=CharacterHandler()

  def update(self):
    print("[Player]:update")
    displacement=self.mover.calcDisplacement(self.direction, self.speed) 
    self.updatePosition(displacement)

  def handleEvent(self, event):
    result=self.controls.handleEvent(event)
    
    if (result == "LEFT"):
      self.rotateEast()
