# MovementHandler.py
# Handles movement wrt entities

# Imports
from Position import *

class MovementHandler(object):
  'Handles movement wrt entities'

  def __init__(self):
    # Debug info
    self.DEBUG=1
    self.DEBUG_TAG="[MovementHandler]"
   
    if (self.DEBUG == 1): 
      print(self.DEBUG_TAG + ":Created")

  def calcDisplacement(self, speed, direction):
    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":Calculating displacement")  
    
    # Displacement values
    if (speed == 0):
      displacement=Position(0,0)
      return displacement
    if (direction == 'E'):
      displacement=Position(speed, 0)
      return displacement
    elif (direction == 'N'):
      displacement=Position(0, 0-speed)
      return displacement
    elif (direction == 'S'):
      displacement=Position(0, speed)
      return displacement
    elif (direction == 'W'):
      displacement=Position(0-speed, 0)
      return displacement

  def stopMovement(self):
    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":Stopping movement")  

