# ObjectData.py; stores information wrt game world objects

# Imports
from Position import *

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
    # Debug info
    self.DEBUG=1
    self.DEBUG_TAG="[ObjectData]"
    
    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":init")

    # Variables
    self.dim=Position(0,0)
    self.color=C_BLK
    self.speed=0
    self.name='none'

    # Build object
    self.buildObject(input_char)
    
  def buildObject(self, input_char):
    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":buildObject:" + str(input_char))

    # Player
    if (input_char == 'p'):
      width=1
      height=2
      self.name='player'
      self.color=C_GRN
      self.dim.updateStorage(width, height)

      # Speed
      self.speed=0.15

    # Racer
    elif (input_char == 'r'):
      width=1
      height=2
      self.name='racer'
      self.color=C_RED
      self.dim.updateStorage(width, height)
  
      # Speed
      self.speed=0.125

    # Wall
    elif (input_char == 'w'):
      width=1
      height=1
      self.name='wall'
      self.color=C_GRY
      self.dim.updateStorage(width, height)

    # Endpoint
    elif (input_char == 'e'):
      width=1
      height=2
      self.name='endpoint'
      self.color=C_GRY
      self.dim.updateStorage(width, height)

  # Helpers
  def getDims(self):
    return self.dim  

  def getName(self):
    return self.name

  def getColor(self):
    return self.color

  def getSpeed(self):
    return self.speed
