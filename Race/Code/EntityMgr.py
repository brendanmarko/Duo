# EntityMgr.py
# Handles the management of Entity groups

# Library imports
import pygame

# Class imports
from Position import *
from CustomGroup import *

class EntityMgr(object):
  'Handles the management of Entity groups'

  def __init__(self, curr_lvl):
    # Debug info
    self.DEBUG=1
    self.DEBUG_TAG='[EntityMgr]'

    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ':init')

    # Groups
    # [Entity, Wall]
    self.e_group=curr_lvl.getEntities()
    self.w_group=curr_lvl.getWalls()

    # Player tracking
    self.player=curr_lvl.getPlayer()

    # PPM
    self.ppm=Position(0,0)

  def getEntities(self):
    return self.e_group

  def getPlayer(self):
    return self.player

  def getWalls(self):
    return self.w_group
