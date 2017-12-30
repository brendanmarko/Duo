# EventHandler.py; handles input given by the Player

# Imports
import sys
import pygame

# Class Imports

# DEBUG info
DEBUG=1

class EventHandler(object):
  'handles input given by the Player'
  
  def __init__(self):
    if (DEBUG == 1):
      print("[EventHandler created]")

  def handleEvent(self, event):
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
    elif (pressed[pygame.K_s] or pressed[pygame.K_DOWN]): 
      if (DEBUG == 1):
        print("[DOWN movement capture]")
    elif (pressed[pygame.K_a] or pressed[pygame.K_LEFT]):
      if (DEBUG == 1):
        print("[LEFT movement capture]")
    elif (pressed[pygame.K_d] or pressed[pygame.K_RIGHT]):
      if (DEBUG == 1):
        print("[RIGHT movement capture]")
