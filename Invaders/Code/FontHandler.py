# FontHandler.py
# Manages the display of fonts in the game

import os
import sys
import math
import pygame

DEBUG=1

class FontHandler(object):
  'Manages the display of fonts in the game'

  def __init__(self, filename):
    self.image=pygame.image.load(filename)
    self.cols=16
    self.rows=4
    self.cell_width=self.image.get_rect().width/self.cols
    self.cell_height=self.image.get_rect().height/self.rows

    if (DEBUG == 1):
      print("[FontHandler]:init:dims=" + str(self.cell_width) + "," + str(self.cell_height))

  def draw(self, surface, text, x, y):
    if (DEBUG == 1):
      print("[FontHandler]:draw=" + str(text) + " [" + str(x) + "," + str(y) + "]")

    for ch in text:
      c=self.getIndex(ch)
      
      if (DEBUG == 1):
        print("[FontHandler]:draw:char_value=" + str(c));  
    
      image_root_x=math.floor(c%self.cols)*self.cell_width
      image_root_y=math.floor(c/self.cols)*self.cell_height

      if (DEBUG == 1):
        print("[FontHandler]:draw:tx=" + str(image_root_x));  
        print("[FontHandler]:draw:ty=" + str(image_root_y));  

      # Construct rectangle for text
      rect=(image_root_x, image_root_y, self.cell_width, self.cell_height)
      surface.blit(self.image, (x, y, self.cell_width, self.cell_height), rect)
      x+=self.cell_width

  def centre(self, surface, message, y):
    width=len(message)*self.cell_width
    surface_width=surface.get_rect().width
    x=(surface_width-width)/2
    self.draw(surface, message, x, y)

  def getCellwidth(self):
    return self.cell_width

  def getCellHeight(self):
    return self.cell_height

  def getIndex(self, c):
    return ord(c)-ord(' ')
