# Level.py
# Empty sandbox

DEBUG=1
TITLE_SIZE=200

from BaseState import *
from BoundChecker import *
from LevelBuilder import *
from CharacterHandler import *
from ProjectileFactory import *

DEBUG=1

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
        
    # Update entities
    for x in self.entities:
      if (x.getMovable() == True):
        x.update()
        self.checker.checkPosition(x)

    # Update projectiles
    for p in self.projectiles.getActiveProjectiles():
      p.update()
      self.checker.checkPosition(p)

  def onExit(self):
    print("[Level]:onExit")

  def draw(self, surface):
    print("[Level]:draw")
      
    # Surface unlocked
    surface.unlock()

    # Draw walls
    for x in range(len(self.walls)):
      y=self.walls[x]
      y.printWall()
      pygame.draw.rect(surface, (169, 169, 169),  y.getHitbox(), 0)

    # Draw entities
    for x in range(len(self.entities)):
      y=self.entities[x]
      scaled_image=pygame.transform.scale(y.getImage(), (y.getWidth(), y.getHeight())) 
      surface.blit(scaled_image, (y.getX(), y.getY()))
      
    # Draw projectiles
    for p in self.projectiles.getActiveProjectiles():
      scaled_image=pygame.transform.scale(p.getImage(), (p.getWidth(), p.getHeight())) 
      surface.blit(scaled_image, (p.getX(), p.getY()))

    # Surface locke
    surface.lock()

  def processEvent(self, result):
    if (result == "N"):
      print("N")
      self.player.rotateN()

    elif (result == "S"):
      print("S")
      self.player.rotateS()

    elif (result == "W"):
      print("W")
      self.player.rotateW()

    elif (result == "E"):
      print("RIGHT")
      self.player.rotateE()

    elif (result == "FIRE"):
      print("FIRE")
      self.projectiles.createProjectile(self.player, 'b')
    

  def handleEvents(self, events):
    if (DEBUG == 1):
      print("[Level]:handleEvents=" + str(len(events)))

    output=""

    for event in events:
      temp=self.handler.handleEvent(event)
      if (DEBUG == 1):
        print(str(temp))

      if (temp == "N" or temp == "S" or temp == "W" or temp == "E"):
        output+=temp
    
      else:
        self.processEvent(temp)

    # Send the cumulative direction to be entity
    if (DEBUG == 1):
      print("[Level]:handleEvents=" + str(output))

  def handleEvent(self, event):
    if (DEBUG == 1):
      print("[Level]:handleEvent=" + str(event))
    result=self.handler.handleEvent(event)
    self.processEvent(result)

