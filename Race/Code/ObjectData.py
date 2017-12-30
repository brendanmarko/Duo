# ObjectData.py; stores information wrt game world objects

# Imports
from Position import *

# Debug info
DEBUG=1
DEBUG_TAG="[ObjectData]"

# Colors
C_GRN=(0, 255, 0)
C_WHT=(255, 255, 255)
C_RED=(255, 0, 0)
C_BLK=(0, 0, 0)
C_BLU=(0, 0, 255)
C_YLW=(255, 255, 0)
C_GRY=(169, 169, 169)
C_ORG=(255, 169, 0)
C_PNK=(255, 0, 255)
C_PRP=(169, 0, 255)
 
class ObjectData(object):
  'stores information regarding game world objects'
  
  def __init__(self, input_char):
    if (DEBUG == 1):
      print(DEBUG_TAG + ":init")

    # Variables
    self.dim=Position(0,0)
    self.color=C_BLK

    # Build object
    self.buildObject(input_char)
    
  def buildObject(self, input_char):
    if (DEBUG == 1):
      print(DEBUG_TAG + ":buildObject:" + str(input_char))

    if (input_char == 'p'):
      width=1
      height=1
      self.color=C_GRN
      self.dim.updateData(width, height)

    elif (input_char == 'r'):
      width=1
      height=1
      self.color=C_RED
      self.dim.updateData(width, height)
  
    elif (input_char == 'w'):
      width=1
      height=1
      self.color=C_GRY
      self.dim.updateData(width, height)

  # Helpers
  def getDims(self):
    return self.dim  
  
  def getColor(self):
    return self.color
