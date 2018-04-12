# TransitionState.py
# Represents interstitial states within the game

import os
import sys
import pygame

from BaseState import *
from FontHandler import *

class TransitionState(BaseState):
  'Represents interstitial states within the game'

  def __init__(self, game, message, delay, next_state):
    super(TransitionState, self).__init__(game)
    self.next_state=next_state
    self.message=message
    self.delay=delay
    self.font=FontHandler("../Bitmaps/font.png", 12, 12) 

  def update(self, elapsed):
    self.delay-=elapsed

    if (self.delay < 0)
      print("[TransitionState]:update:complete")
      self.game.updateState(self.next_state)

    else  
      print("[TransitionState]:update:active")

  def draw(self, surface):
    self.font.centre(surface, self.message, surface.get_rect().height/2)
