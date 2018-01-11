# EventHandler.py
# Handles player input

# Imports
import sys
import pygame

# Class Imports
from MovementHandler import *

class EventHandler(object):
  'Handles player input'
  
  def __init__(self):
    # self.DEBUG info
    self.DEBUG=1
    self.DEBUG_TAG="[Eventhandler]"
    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":init")
    movement_handler=MovementHandler()

  def handleEvent(self, event, player):
    if (self.DEBUG == 1):
      print("[Event passed to handleEvent: " + str(event) + "]")
    
    # Handles [Quit]
    if (event.type == pygame.QUIT):
      pygame.quit()
      sys.exit()
  
    # Handles key presses
    pressed = pygame.key.get_pressed()
       
    # Handles rotation of player
    if (pressed[pygame.K_q]):
      if (self.DEBUG == 1):
        print(self.DEBUG_TAG + ":CCW Rotation")
      player.rotateCCW()

    elif (pressed[pygame.K_e]):
      if (self.DEBUG == 1):
        print(self.DEBUG_TAG + ":CW Rotation")
      player.rotateCW()
 
    # Handles movement [N] 
    if (pressed[pygame.K_w] or pressed[pygame.K_UP]):
      if (self.DEBUG == 1):
        print(self.DEBUG_TAG + ":NORTH movement captured")
      player.moveN()

    # Handles movement [S]
    elif (pressed[pygame.K_s] or pressed[pygame.K_DOWN]): 
      if (self.DEBUG == 1):
        print(self.DEBUG_TAG + ":SOUTH movement captured")
      player.moveS()

    # Handles movement [W]
    elif (pressed[pygame.K_a] or pressed[pygame.K_LEFT]):
      if (self.DEBUG == 1):
        print(self.DEBUG_TAG + ":WEST movement captured")
      player.moveW()

    # Handles movement [E]
    elif (pressed[pygame.K_d] or pressed[pygame.K_RIGHT]):
      if (self.DEBUG == 1):
        print(self.DEBUG_TAG + ":EAST movement captured")
      player.moveE() 
