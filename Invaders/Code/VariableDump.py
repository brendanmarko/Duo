# VariableDump.py
# Somewhere to store some variables being used by multiple classes

from Position import *

class VariableDump(object):
  def __init__(self):
    self.PPM_X=60
    self.PPM_Y=90

  def getPixelScale(self):
    return Position(self.PPM_X, self.PPM_Y)
