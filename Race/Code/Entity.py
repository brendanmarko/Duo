# Entity.py; base class for in-game objects

# Library imports
import pygame

# Class imports
from Position import *
from ObjectData import *

# Debug info
DEBUG=1
DEBUG_TAG="[Entity]"

class Entity(object):
  'base class for in-game objects'

  def __init__(self, x, y, object_type, ppm):
    if (DEBUG == 1):
      print(DEBUG_TAG + ":init")
  
    # Position data
    self.x=x*ppm.getX()
    self.y=y*ppm.getY()

    # Dimension data    
    self.info=ObjectData(object_type)
    self.width=self.info.getDims().getX()*ppm.getX()
    self.height=self.info.getDims().getY()*ppm.getY()

    # Hitbox setup
    self.calculateHitbox(self.x, self.y, self.width, self.height)

  def getX(self):
    return self.x 

  def getY(self):
    return self.y

  def getWidth(self):
    return self.width

  def getHeight(self):
    return self.height 

  # calculateHitbox(x, y, width, height)
  # Builds the hitbox for the Entity; put as its own function incase more funcionality is needed
  def calculateHitbox(self, x, y, width, height):
    self.hitbox=pygame.Rect(x, y, width, height)
    if (DEBUG == 1):
      print("Values of hitbox: (" + str(x) + "->" + str(x+width) + ", " + str(y) + "->" + str(y+height)  + ")")
      print("Values of Rect: T=" + str(self.hitbox.top) + ", L=" + str(self.hitbox.left) + ", B=" + str(self.hitbox.bottom) + ", R=" + str(self.hitbox.right))

  def getHitbox(self):
    return self.hitbox
