# Game.py
# Handles management of the game

# Class imports
from Level import *
from EntityMgr import *
from LevelBuilder import *

# Game Info
PPM_X=32
PPM_Y=18

class Game(object):
  'Handles management of the game'

  def __init__(self, level_string):
    # Debug info
    self.DEBUG=1
    self.DEBUG_TAG='[Game]'
  
    # Build and assign level
    self.lvl_builder=LevelBuilder(level_string, PPM_X, PPM_Y)
    self.current_lvl=self.lvl_builder.setup()    

    # Initialize EntityMgr
    self.entity_mgr=EntityMgr(self.current_lvl)

  def getPlayer(self):
    return self.entity_mgr.getPlayer()

  # update(self)
  # Updates data wrt Entities
  def update(self):
    if (DEBUG == 1):
      print(self.DEBUG_TAG + ":update")  
    
    for y in self.entity_mgr.getEntities():
      if (y.getMovable() == True):
        y.update()

  # draw(self, display_surface)
  # Prints to the Screen
  def draw(self, display_surface):
    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":draw")
    
    # Draw the Walls 
    for x in self.entity_mgr.getWalls():
      for y in x.getWall():
        scaled_image=pygame.transform.scale(y.getImage(), (y.getWidth(), y.getHeight())) 
        display_surface.blit(scaled_image, (y.getX(), y.getY()))
    
    # Draw the Entities
    for y in self.entity_mgr.getEntities():
      # Scale and draw image
      scaled_image=pygame.transform.scale(y.getImage(), (y.getWidth(), y.getHeight())) 
      display_surface.blit(scaled_image, (y.getX(), y.getY()))
  
