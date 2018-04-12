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

  def handleEvent(self, event, curr_player):
    if (DEBUG == 1):
      print("[Event passed to handleEvent: " + str(event) + "]")
    
    # Handles [Quit]
    if (event.type == pygame.QUIT):
      pygame.quit()
      sys.exit()
  
    # Handles key presses
    pressed = pygame.key.get_pressed()
         
    if (pressed[pygame.K_w] or pressed[pygame.K_UP]):
      if (DEBUG == 1):
        print("[UP movement capture]")
      curr_player.rotateNorth()

    elif (pressed[pygame.K_s] or pressed[pygame.K_DOWN]): 
      if (DEBUG == 1):
        print("[DOWN movement capture]")
      curr_player.rotateSouth()

    # Handles movement [W]
    elif (pressed[pygame.K_a] or pressed[pygame.K_LEFT]):
      if (DEBUG == 1):
        print("[LEFT movement capture]")
      curr_player.rotateWest()

		# Handles movement [E]
    elif (pressed[pygame.K_d] or pressed[pygame.K_RIGHT]):
      if (DEBUG == 1):
        print("[EAST movement captured]")
      curr_player.rotateEast()
      
