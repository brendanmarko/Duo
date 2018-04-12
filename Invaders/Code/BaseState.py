# BaseState.py
# Serves as the base for subsequent game states

import os
import sys
import pygame

class BaseState(object):
  def __init__(self, game):
    self.game=game
    
  def onEnter(self, prev_state):
    pass

  def onExit(self):
    pass

  def draw(self, surface):
    pass

  def update(self):
    pass

  def handleEvent(self, event):
    pass
