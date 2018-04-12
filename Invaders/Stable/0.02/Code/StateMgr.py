# StateMgr.py
# Handles the management of game states within the application

import os
import sys
import pygame

class StateMgr(object):
  'Handles the management of game states within the application'

  def __init__(self, state):
    print("[StateMgr]:init")
    self.curr_state=state
    print("[StateMgr]:state=" + str(self.curr_state))

  # Handles the changing of states
  def updateState(self, new_state):
    print("[StateMgr]:update=" + str(new_state))
  
    # Checks if current state is None
    if (self.curr_state != None):
      self.curr_state.onExit()

    # Checks if new state is None
    if (new_state == None):
      pygame.quit()
      sys.exit()
    
    # Update to next state
    prev=self.curr_state
    self.curr_state=new_state
    new_state.onEnter(prev) 
    
  def getState(self):
    return self.curr_state
