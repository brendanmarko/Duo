# Main.py
# Launches the application

# Imports
import sys
import pygame

# Class imports
from time import sleep
from Game import *
from EventHandler import *

# Game Info
GAME_FPS=30
GAME_X_DIM=900
GAME_Y_DIM=600
GAME_TITLE="RACE 0.15c"

class Main(object):
  'launches the game'  

  def __init__(self):
    # Variables
    self.level_num=""

    # Debug info
    self.DEBUG=1
    self.DEBUG_TAG="[Main]"

    # Reads arguments from command line for which level to load
    # If no argument is entered, 00 is rendered
    if (len(sys.argv) > 1):
      self.level_num=sys.argv[1]
    else:
      self.level_num="00"

    # Initialize pygame info
    pygame.init()
    self.display_surface = pygame.display.set_mode((GAME_X_DIM, GAME_Y_DIM))
    pygame.display.set_caption(GAME_TITLE)
    self.clock = pygame.time.Clock()

    # Init EventHandler
    self.event_handler=EventHandler()

    # Build and start game
    self.game=Game(self.level_num)
    self.gameLoop()

  def gameLoop(self):
    while True:
      
      if (self.DEBUG == 1):
        print(self.DEBUG_TAG + " = = = = = = = = = = = = = = = = = =")

      # Fill background
      self.display_surface.fill((0, 0, 0))

      # Captures events and handles them
      for event in pygame.event.get():
        self.event_handler.handleEvent(event, self.game.getPlayer())

      # Update
      self.game.update()
      self.display_surface.unlock()
 
      # Draw Entities
      self.game.draw(self.display_surface)           
      self.display_surface.lock()

      # surface_display update information
      pygame.display.update()
      pygame.time.Clock().tick(GAME_FPS)
  
# Execute the Game
main=Main()
