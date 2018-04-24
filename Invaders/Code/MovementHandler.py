# MovementHandler.py
# Handles movement wrt entities

# Imports
from Position import *
from VariableDump import *

DEBUG=1
DEBUG_TAG="[MovementHandler]"
SPEED_FACTOR=2 #1/X
class MovementHandler(object):
  'Handles movement wrt entities'

  def __init__(self):
    if (DEBUG == 1): 
      print(DEBUG_TAG + ":init")
    self.data=VariableDump()
    self.ppm_x=self.data.getPixelScale().getX()
    self.ppm_y=self.data.getPixelScale().getY()

  def calcDisplacement(self, direction, speed):
    if (DEBUG == 1):
      print(DEBUG_TAG + ":single_disp")  
    
    # Displacement 
    displacement=Position(0,0)

    # Update displacement wrt speed
    if (speed == 0):
      return displacement

    # !!!
    # Need to reconfigure the way displacement is calculated, reliance upon PPM IS BAD
    if (direction == 'E'):
      displacement.updateX(self.ppm_x/SPEED_FACTOR * speed)

    if (direction == 'N'):
      displacement.updateY(self.ppm_y/SPEED_FACTOR * (0-speed))

    if (direction == 'S'):
      displacement.updateY(self.ppm_y/SPEED_FACTOR * speed)

    if (direction == 'W'):
      displacement.updateX(self.ppm_x/SPEED_FACTOR * (0-speed))
    
    if (DEBUG == 1):
      print("[MovementHandler]:disp=" + str(displacement.getX()) + ", " + str(displacement.getY()))

    # Updated displacement vector returned
    return displacement

  def stopMovement(self):
    if (DEBUG == 1):
      print(DEBUG_TAG + ":Stopping movement")  

