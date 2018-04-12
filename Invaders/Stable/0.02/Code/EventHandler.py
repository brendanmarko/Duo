# EventHandler.py
# Handles input; base-class for Player and Menu handlers

# Imports
import sys
import pygame

# DEBUG info
DEBUG=1

class EventHandler(object):
  'Handles input; base-class for Player and Menu handlers'
  
  def __init__(self):
    if (DEBUG == 1):
      print("[EventHandler]:init")

  def handleEvent(self, event):
    pass
