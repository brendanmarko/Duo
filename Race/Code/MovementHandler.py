# MovementHandler.py
# Handles movement wrt entities

class MovementHandler(object):
  'Handles movement wrt entities'

  def __init__(self):
    # Debug info
    self.DEBUG=1
    self.DEBUG_TAG="[MovementHandler]"
   
    if (self.DEBUG == 1): 
      print(self.DEBUG_TAG + ":Created")

  def initMovement(self):
    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":Starting movement")  

  def stopMovement(self):
    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":Stopping movementd")  

  def moveForward(self):
    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":Forward movement detected")  
  
  def moveReverse(self):
    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":Reverse movement detected")  
