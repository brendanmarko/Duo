# Position.py; serves as storage for a position (or any structure with two points)

DEBUG=1
DEBUG_TAG="[Position]"

class Position(object):
  'serves as storage for a position (or any structure with two points)'

  def __init__(self, x, y):
    if (DEBUG == 1):
      print(DEBUG_TAG + ":init")
    self.curr_pos=[x,y]

  def getX(self):
    return self.curr_pos[0]

  def getY(self):
    return self.curr_pos[1]

  def updateData(self, new_x, new_y):
    self.curr_pos[0]=new_x
    self.curr_pos[1]=new_y

  def getPosition(self):
    return self.curr_pos
