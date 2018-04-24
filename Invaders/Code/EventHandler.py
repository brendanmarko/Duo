# EventHandler.py
# Handles player input

# Imports
import sys
import pygame

# Class Imports
from MovementHandler import *

# DEBUG info
DEBUG=1

class EventHandler(object):
  'Handles player input'
  
  def __init__(self):
    if (DEBUG == 1):
      print("[EventHandler created]")
      movement_handler=MovementHandler()

  def handleEvent(self, event):
    pass

  def handleEvents(self, events):
    pass
