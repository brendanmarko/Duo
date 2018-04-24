# Game.py
# Handles the launching of the game

import os
import sys
import pygame

from Menu import *
from StateMgr import *
from pygame.locals import *

# Variables
DEBUG=1
TITLE="SAMPLE"
FPS=30

class Game(object):

  def __init__(self):
    'Handles the launching of the game'
    print("[Game]:init")
    
    # Initialization
    pygame.init()
    pygame.key.set_repeat()
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
      # Actively loaded state
      curr_state=self.state_mgr.getCurrState()

      # Input handler
      inputs=pygame.event.get()

      if (DEBUG == 1):
        print("[Game]:event_size=" + str(len(inputs)))

      # Handles different input sizes
      if (len(inputs) == 1):
        if (DEBUG == 1):
          print("[Game]:input_single")
        curr_state.handleEvent(inputs[0])
      
      elif (len(inputs) > 1):
        if (DEBUG == 1):
          print("[Game]:input_multi")
        curr_state.handleEvents(inputs)

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
