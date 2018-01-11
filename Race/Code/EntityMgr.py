# EntityMgr
# Handles the management of Entity groups

# Library imports
import pygame

# Class imports
from Position import *
from CustomGroup import *

class EntityMgr(object):
  'Handles the management of Entity groups'

  def __init__(self):
    # Debug info
    self.DEBUG=1
    self.DEBUG_TAG='[EntityMgr]'

    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ':init')

    # Groups
    # [Entity, Wall]
    self.e_group=CustomGroup()
    self.w_group=CustomGroup()

    # PPM
    self.ppm=Position(0,0)

  # Must be called during initialization
  def setPixelSize(self, ppm_x, ppm_y):
    self.ppm.updateStorage(ppm_x, ppm_y)
