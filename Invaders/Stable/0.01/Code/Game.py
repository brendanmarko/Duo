# Game.py
# Handles the launching of the game

import os
import sys
import pygame

from Menu import *
from StateMgr import *
from pygame.locals import *

# Variables
FPS=30

class Game(object):

  def __init__(self, caption, width, height):
    'Handles the launching of the game'
    print("[Game]:init")
    
    # Initialization
    pygame.init()
    pygame.display.set_caption(caption)

    # Main info
    self.caption=caption
    self.width=width
    self.height=height 
    self.fps=pygame.time.Clock()
    self.window=pygame.display.set_mode((self.width, self.height))
    self.background=pygame.Color(0,0,0) 

    # State changes
    self.states=StateMgr(None)

  def getStateMgr(self):
    return self.states

  def run(self, curr_state):
    self.states.updateState(curr_state)
   
    # EVENT HANDLING
    while (True):
      for event in pygame.event.get():
        if (event.type == QUIT):
          pygame.quit()
          sys.exit() 
        
      active_time=self.fps.get_time()

      # UPDATE
      if (self.states.getState() != None):
        self.states.getState().update(active_time)

      self.window.fill(self.background)    

      # DRAW
      if (self.states.getState() != None):
        self.states.getState().draw(self.window)

      pygame.display.update()
      self.fps.tick(FPS)
