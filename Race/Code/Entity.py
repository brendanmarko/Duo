# Entity.py
# Base class for in-game objects; uses Sprites

# Library imports
import pygame, os

# Class imports
from Position import *
from ObjectData import *

class Entity(pygame.sprite.Sprite):
  'base class for in-game objects; uses Sprites'

  def __init__(self, x, y, object_type, ppm):     
    pygame.sprite.Sprite.__init__(self)

    # Dimension data    
    self.info=ObjectData(object_type)
    self.width=self.info.getDims().getX()*ppm.getX()
    self.height=self.info.getDims().getY()*ppm.getY()

    # Loads image file corresponding to object name
    self.image=pygame.image.load('Resources/Images/' + self.info.getName() + '.png').convert_alpha()
    
    # Debug info
    self.DEBUG=1
    self.DEBUG_TAG="[Entity]"
    
    # Position data
    self.x=x*ppm.getX()
    self.y=y*ppm.getY()
    self.e_ppm=ppm
    self.position=Position(self.x, self.y)

    # Movable flag
    self.movable=False
  
    # Speed
    self.speed=self.info.getSpeed()

    # Hitbox setup
    self.calculateHitbox(self.x, self.y, self.width, self.height)

  ##### Position functions
  def getX(self):
    return self.x

  def getY(self):
    return self.y

  def updatePosition(self, displacement):
    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":updatePosition")
      print(self.DEBUG_TAG + ":preUpdate [X=" + str(self.x) + ", [Y=" + str(self.y) + "]")

    self.x+=(displacement.getX()*self.e_ppm.getX())
    self.y+=(displacement.getY()*self.e_ppm.getY())
    self.position.updateStorage(self.x, self.y)

    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":newUpdate [X=" + str(self.x) + ", [Y=" + str(self.y) + "]")

  ##### end : Position functions

  def getImage(self):
    return self.image

  def getWidth(self):
    return self.width

  def getHeight(self):
    return self.height 

  ##### Movable Status 
  def setMovable(self, movable_status):
    if (movable_status == False):
      self.movable=False
    else:
      self.movable=True

  def getMovable(self):
    return self.movable

  def getSpeed(self):
    return self.speed

  ##### end : Movable Status
 
  ##### Hitbox functions 
  # calculateHitbox(x, y, width, height)
  # Builds the hitbox for the Entity; put as its own function incase more functionality is needed
  def calculateHitbox(self, x, y, width, height):
    self.hitbox=pygame.Rect(x, y, width, height)
    if (self.DEBUG == 1):
      print("Values of hitbox: (" + str(x) + "->" + str(x+width) + ", " + str(y) + "->" + str(y+height)  + ")")
      print("Values of Rect: T=" + str(self.hitbox.top) + ", L=" + str(self.hitbox.left) + ", B=" + str(self.hitbox.bottom) + ", R=" + str(self.hitbox.right))

  def updateHitbox(self):
    self.hitbox=pygame.Rect(self.x, self.y, self.width, self.height)

  def getHitbox(self):
    return self.hitbox

  ##### end : Hitbox functions
