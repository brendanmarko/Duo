# Level.py
# Empty sandbox

DEBUG=1
TITLE_SIZE=200

from BaseState import *
from BoundChecker import *
from LevelBuilder import *
from CharacterHandler import *
from ProjectileFactory import *

class Level(BaseState):
  def __init__(self, game):
    super(Level, self).__init__(game)
    self.curr_state=None
    print("[Level]:init")

    # Font init
    pygame.font.init()
    self.title_font=pygame.font.SysFont("DroidSans", TITLE_SIZE)

    # Builds level from text file
    self.builder=LevelBuilder("00")

    # Assign wall, player, and entities to Level
    self.walls=self.builder.getWalls()
    self.entities=self.builder.getEntities()
    self.player=self.builder.getPlayer()
    self.ppm=self.builder.getPPM()

    # ProjectileFactory
    self.projectiles=ProjectileFactory(self.ppm)

    self.checker=BoundChecker(self.builder.getDimensions())
    self.handler=CharacterHandler()

  def onEnter(self, prev_state):
    if (DEBUG == 1):    
      print("[Level]:onEnter")

  def update(self, elapsed):
    if (DEBUG == 1):    
      print("[Level]:update=" + str(elapsed))
        
    for x in range(len(self.entities)):
      y=self.entities[x]
      if (y.getMovable() == True):
        y.update()
        self.checker.checkPosition(y)

  def onExit(self):
    print("[Level]:onExit")

  def draw(self, surface):
    print("[Level]:draw")
      
    # Surface unlocked
    surface.unlock()

    # Build walls
    for x in range(len(self.walls)):
      y=self.walls[x]
      y.printWall()
      pygame.draw.rect(surface, (169, 169, 169),  y.getHitbox(), 0)

    # Build entities
    for x in range(len(self.entities)):
      y=self.entities[x]
      scaled_image=pygame.transform.scale(y.getImage(), (y.getWidth(), y.getHeight())) 
      surface.blit(scaled_image, (y.getX(), y.getY()))

    # Surface locked
    surface.lock()

  def handleEvent(self, event):
    print("[Level]:handleEvent=" + str(event))
    result=self.handler.handleEvent(event)

    if (result == "UP"):
      print("UP")
      self.player.rotateNorth()

    elif (result == "DOWN"):
      print("DOWN")
      self.player.rotateSouth()

    elif (result == "LEFT"):
      print("LEFT")
      self.player.rotateWest()

    elif (result == "RIGHT"):
      print("RIGHT")
      self.player.rotateEast()

    elif (result == "FIRE"):
      print("FIRE")
      self.projectiles.createProjectile(self.player, 'b')
