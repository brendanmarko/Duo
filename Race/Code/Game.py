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
  
    # Build && Assign Level
    self.lvl_builder=LevelBuilder(level_string, PPM_X, PPM_Y)
    self.current_lvl=self.lvl_builder.setup()    

  def getPlayer(self):
    return self.current_lvl.getPlayer()

  # update(self)
  # Updates data wrt Entities
  def update(self):
    if (DEBUG == 1):
      print(self.DEBUG_TAG + ":update")  
    
    for y in self.current_lvl.getEntities():
      if (y.getMovable() == True):
        y.update()

  # draw(self, display_surface)
  # Prints to the Screen
  def draw(self, display_surface):
    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":draw")
    
    # Draw the Walls
    if (DEBUG == 1):
      print(self.DEBUG_TAG + ":draw:Walls:" + str(len(self.current_lvl.getWalls())))
    
    wall_list=self.current_lvl.getWalls()
    for x in range(len(wall_list)):
      y=wall_list[x]
      y.printWall()
      pygame.draw.rect(display_surface, (169,169,169),  y.getHitbox(), 0)
    
    # Draw the Entities
    entity_list=self.current_lvl.getEntities()
    if (DEBUG == 1):
      print(self.DEBUG_TAG + ":draw:Entities:" + str(len(entity_list)))
    for y in entity_list:
      # Scale and draw image
      scaled_image=pygame.transform.scale(y.getImage(), (y.getWidth(), y.getHeight())) 
      display_surface.blit(scaled_image, (y.getX(), y.getY()))
  
