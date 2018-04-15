# ObjectData.py; stores information wrt game world objects

# Imports
from Position import *

# PPM Values
PPM_X=60
PPM_Y=90

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

    # WIDTH && HEIGHT
    self.dimensions=Position(0,0)

    self.color=C_BLK
    self.speed_factor=0.0
    self.name='none'

    # Build object
    self.buildObject(input_char)
    
  def buildObject(self, input_char):
    if (DEBUG == 1):
      print(DEBUG_TAG + ":buildObject:" + str(input_char))

    if (input_char == 'p'):
      self.name='player'
      self.color=C_GRN

      # Width and Height
      self.dimensions.updateStorage(PPM_X*1, PPM_Y*1)
      self.speed_factor=0.3

    elif (input_char == 'r'):
      self.name='racer'
      self.color=C_RED

      # Width and Height
      self.dimensions.updateStorage(PPM_X*1, PPM_Y*1)
      self.speed_factor=0.3

    # Projectiles 
    ## Bullet
    elif (input_char == 'b'):
      self.name='bullet'
      self.color=C_YLW
      
      # Width and Height
      self.dimensions.updateStorage(PPM_X*1, PPM_Y*1)
      self.speed_factor=0.5

    # Wall
    elif (input_char == 'w'):
      self.name='wall'
      self.color=C_GRY
      self.dimensions.updateStorage(1, 1)
      self.speed_factor=0.0

  # Helpers
  def getDims(self):
    return self.dimensions  

  def getName(self):
    return self.name

  def getColor(self):
    return self.color

  def getSpeed(self):
    return self.speed_factor
