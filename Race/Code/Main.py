# Main.py; launches the game

# Imports
import sys
import pygame

# Class imports
from time import sleep
from EventHandler import *
from LevelBuilder import *

# Game Info
GAME_FPS=30
GAME_X_DIM=800
GAME_Y_DIM=600
GAME_TITLE="RACE 0.15c"

class Main(object):
  'launches the game'  

  def __init__(self):
    # Variables
    self.level_num=""
    self.curr_player=None

    # Debug info
    self.DEBUG=1
    self.DEBUG_TAG="[Main]"

    # Reads arguments from command line for which level to load
    # If no argument is entered, 00 is rendered
    if (len(sys.argv) > 1):
      self.level_num=sys.argv[1]
    else:
      self.level_num="00"

    # Init pygame info
    pygame.init()
    self.display_surface = pygame.display.set_mode((GAME_X_DIM, GAME_Y_DIM))
    pygame.display.set_caption(GAME_TITLE)
    self.clock = pygame.time.Clock()

    # Init EventHandler
    self.event_handler=EventHandler()

    # Build Level
    self.lvl_builder=LevelBuilder(self.level_num)
    self.curr_player=self.lvl_builder.getPlayer()

  def start(self):
    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":start")
    
    self.gameLoop(self.lvl_builder.getLevel())    

  def gameLoop(self, curr_level):
    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":gameLoop")

    # Game loop
    while True:
      
      if (self.DEBUG == 1):
        print(self.DEBUG_TAG + " = = = = = = = = = = = = = = = = = =")

      # Fill background
      self.display_surface.fill((0, 0, 0))

      # Captures events and handles them
      for event in pygame.event.get():
        self.event_handler.handleEvent(event, self.curr_player)

      # Update
      self.update(curr_level)
 
      self.display_surface.unlock()
 
      # Draw Entities
      self.draw(curr_level)           

      self.display_surface.lock()

      # Display update
      pygame.display.update()
      pygame.time.Clock().tick(GAME_FPS)

  # update(self, curr_level)
  # Updates data wrt Entities
  def update(self, curr_level):
    if (DEBUG == 1):
      print(self.DEBUG_TAG + ":update")  
    entity_list=curr_level.getEntities()
    
    for x in range(len(entity_list)):
      y=entity_list[x]
      if (y.getMovable() == True):
        y.update()

  # draw(self, curr_level)
  # Prints to the Screen
  def draw(self, curr_level):
    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":draw")
    
    # Draw the Walls
    if (DEBUG == 1):
      print(self.DEBUG_TAG + ":draw:Walls:" + str(len(curr_level.getWalls())))
    
    wall_list=curr_level.getWalls()
    for x in range(len(wall_list)):
      y=wall_list[x]
      y.printWall()
      pygame.draw.rect(self.display_surface, (169, 169, 169),  y.getHitbox(), 0)
    
    # Draw the Entities
    entity_list=curr_level.getEntities()
    if (DEBUG == 1):
      print(self.DEBUG_TAG + ":draw:Entities:" + str(len(entity_list)))
    for x in range(len(entity_list)):
      y=entity_list[x]

			# Scale image to proper size
      scaled_image=pygame.transform.scale(y.getImage(), (y.getWidth(), y.getHeight())) 

      # Blits (draws) entity to surface
      self.display_surface.blit(scaled_image, (y.getX(), y.getY()))
  
# Execute the Game
main=Main()
main.start()
