# Entity.py
# Base class for in-game objects; uses Sprites

# Library imports

import os
import pygame

# Class imports
from Position import *
from ObjectData import *

DEBUG=1

class Entity(pygame.sprite.Sprite):
  'Base class for in-game objects; uses Sprites'

  def __init__(self, pos, input_type):
    pygame.sprite.Sprite.__init__(self)
   
    # Object Data 
    self.info=ObjectData(input_type)

    # Position data
    self.position=Position(pos[0], pos[1])

    if (DEBUG == 1):
      print("[Entity]:pos=" + str(self.position.getX()) + "," + str(self.position.getY()))

    # Loads image file corresponding to object name
    self.image=pygame.image.load('Bitmaps/' + self.info.getName() + '.png').convert()
    self.setMovable(False)

  ##### Position functions
  def getX(self):
    return self.position.getX()

  def getY(self):
    return self.position.getY()

  def getPos(self):
    return self.position

  def setX(self, x):
    self.position.updateX(x)

  def setY(self, y):
    self.position.updateY(y)

  # This function expects calcDisplacement output as input
  def updatePosition(self, displacement):
    if (DEBUG == 1):
      print("[Entity]:updatePosition")
      print("[Entity]:preUpdate [X=" + str(self.getX()) + ", Y=" + str(self.getY()) + "]")

    x=self.getX() + displacement.getX()
    y=self.getY() + displacement.getY()
    self.position.updateStorage(x,y)

    if (DEBUG == 1):
      print("[Entity]:newUpdate [X=" + str(self.getX()) + ", Y=" + str(self.getY()) + "]")

  ##### end : Position functions

  ##### Dimensions & Images 
  def getImage(self):
    return self.image

  def getWidth(self):
    return self.info.getDims().getX()

  def getHeight(self):
    return self.info.getDims().getY()

  ##### end : Dimensions & Images 

  ##### Movable Status 
  def setMovable(self, movable_status):
    if (movable_status == False):
      self.movable=False
    else:
      self.movable=True

  def getMovable(self):
    return self.movable
 
  ##### Hitbox functions 
  # calculateHitbox(x, y, width, height)
  # Builds the hitbox for the Entity; separate function (incase more functionality is needed)
  def calculateHitbox(self, x, y, width, height):
    self.hitbox=pygame.Rect(x, y, width, height)
    if (DEBUG == 1):
      print("Values of hitbox: (" + str(x) + "->" + str(x+width) + ", " + str(y) + "->" + str(y+height)  + ")")
      print("Values of Rect: T=" + str(self.hitbox.top) + ", L=" + str(self.hitbox.left) + ", B=" + str(self.hitbox.bottom) + ", R=" + str(self.hitbox.right))

  def updateHitbox(self):
    self.hitbox=pygame.Rect(self.x, self.y, self.width, self.height)

  def getHitbox(self):
    return self.hitbox

  ##### end : Hitbox functions
