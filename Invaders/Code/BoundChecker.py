# BoundChecker.py
# Checks if updated positions are within level constraints

DEBUG=1

class BoundChecker(object):
  def __init__(self, dimensions):
    print("[BoundChecker]:init=" + str(dimensions[0]) + "," + str(dimensions[1]))
    self.max_x=dimensions[0]
    self.max_y=dimensions[1]

  # Checks if current position falls within level boundaries
  def checkPosition(self, target):
    
    # Checks x co-ordinate
    x=target.getX()
    if (x < 0):
      target.setX(0)

    elif (x > self.max_x-target.getWidth()):
     target.setX(self.max_x-target.getWidth()) 

    # Checks y co-ordinate
    y=target.getY()
    if (y < 0):
      target.setY(0)

    elif (y > self.max_y-target.getHeight()):
     target.setY(self.max_y-target.getHeight()) 

    if (DEBUG == 1):
      print("[BoundChecker]:checkPosition:completed")
