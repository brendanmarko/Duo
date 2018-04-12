# Game.py
# Handles the launching of the game

import os
import sys
import pygame

from Menu import *
from StateMgr import *
from pygame.locals import *

# Variables
TITLE="SAMPLE"
FPS=30

class Game(object):

  def __init__(self):
    'Handles the launching of the game'
    print("[Game]:init")
    
    # Initialization
    pygame.init()
    pygame.display.set_caption(TITLE)

    # Display info
    self.width=pygame.display.Info().current_w
    self.height=pygame.display.Info().current_h

    print("[Game]:init:display_size=" + str(self.width) + "," + str(self.height))

    self.fps=pygame.time.Clock()
    self.window=pygame.display.set_mode((self.width, self.height))
    # self.window=pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
    self.background=pygame.Color(0,0,0) 

    # State changes
    self.state_mgr=StateMgr(None)

  def getCurrStateMgr(self):
    return self.state_mgr

  def getWidth(self):
    return self.width

  def getHeight(self):
    return self.height

  def run(self, curr_state):
    self.state_mgr.changeState(curr_state)
   
    # EVENT HANDLING
    while (True):
      curr_state=self.state_mgr.getCurrState()
      for event in pygame.event.get():
        curr_state.handleEvent(event) 
      active_time=self.fps.get_time()

      # UPDATE
      if (curr_state != None):
        curr_state.update(active_time)

      self.window.fill(self.background)    

      # DRAW
      if (curr_state != None):
        curr_state.draw(self.window)

      pygame.display.update()
      self.fps.tick(FPS)
