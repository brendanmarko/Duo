# Position.py
# Serves as storage for a position (or any data type with two fields!)

class Position(object):
  'serves as storage for a position (or any structure with two points)'

  def __init__(self, x, y):

    self.DEBUG=1
    self.DEBUG_TAG="[Position]"

    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":init")

    self.curr_pos=[x,y]

  def getX(self):
    return self.curr_pos[0]

  def getY(self):
    return self.curr_pos[1]

  def updateStorage(self, new_x, new_y):
    self.curr_pos[0]=new_x
    self.curr_pos[1]=new_y

  def getStorage(self):
    return self.curr_pos
  
  def printPos(self):
    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":X=" + str(self.getX()) + ", Y=" + str(self.getY()))
