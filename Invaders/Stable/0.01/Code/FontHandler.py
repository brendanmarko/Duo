# FontHandler.py
# Manages the display of fonts in the game

import os
import sys
import pygame

class FontHandler(object):
  'Manages the display of fonts in the game'

  def __init__(self, filename, width, height):
    self.image=pygame.image.load(filename)
    self.cell_width=width
    self.cell_height=height
    self.cols=(self.image.get_rect().width/self.cell_width)
    self.rows=(self.image.get_rect().height/self.cell_height)

  def draw(self, surface, text, x, y):
    for ch in text:
      c=self.getIndex(ch)
      tx=(c%self.cols)*self.cell_width
      ty=(c%self.cols)*self.cell_height

      # Construct rectangle for text
      rect=(tx, ty, self.cell_width, self.cell_height)
      surface.blit(self.image, (x, y, self.cell_width, self.cell_height), rect)
      x+=self.cell_width

  def centre(self, surface, message, y):
    width=len(message)*self.cell_width
    h_width=surface.get_rect().width
    x=(h_width-width)/2
    self.draw(surface, message, x, y)

  def getIndex(self, c):
    return ord(c)-ord(' ')
