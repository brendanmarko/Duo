# Menu.py
# Acts as the main menu for the game, limits input rates

import os
import sys
import pygame

from BaseState import *
from FontHandler import *
from pygame.locals import *

# Variables
MENU_TITLE="GAME NAME"

class Menu(BaseState):
  "Acts as the main menu for the game"
  
  def __init__(self, game):
    super(Menu, self).__init__(game)
    self.curr_state=None
    self.active_menu_index=0
    self.font=FontHandler("Bitmaps/font.png", 12, 12) 
    self.input_tick=0
    self.menu_list=["Start Game", "Settings", "Quit"]
    
  def onEnter(self, prev_state):
    print("[Menu]:onEnter_prev=" + str(prev_state))

  def setActiveState(self, state):
    self.curr_state=state

  def update(self, elapsed):
    # Captures the current pressed key
    curr_key=pygame.key.get_pressed()

    # Checks current pressed key for menu navigation
    if (curr_key[K_UP] or curr_key[K_DOWN] and self.input_tick == 0):
      self.input_tick=250

      if (curr_key[K_UP]):
        self.active_menu_index-=1
        if (self.active_menu_index < 0):
          self.active_menu_index=len(self.menu_list)-1
      
        elif (curr_key[K_DOWN]):
          self.active_menu_index+=1
        if (self.active_menu_index == len(self.menu_list)):
          self.active_menu_index=0

    elif (self.input_tick > 0):
      self.input_tick-=elapsed
    
    if (self.input_tick < 0):
      self.input_tick=0

    # Checks current key for menu selection input
    if (curr_key[K_SPACE] or curr_key[K_RETURN]):
      print("[Menu]:selection_made")
  
      # Quit selected
      if (self.active_menu_index == 2):
        self.game.getStateMgr().updateState(self.curr_state(None))

      elif (self.active_menu_index == 1):
        print("[Menu]:settings_selected")

      else:
        self.game.getStateMgr().updateState(self.curr_state)


  def draw(self, surface):
    count=0
  
    # Surface info
    self.font.centre(surface, MENU_TITLE, 48)
    y=surface.get_rect().height-len(self.menu_list)*160

    # Iterate Menu
    for menu_item in self.menu_list:

      # Menu item position equals the active index selected 
      if (count == self.active_menu_index):
        text="> "
  
      else:
        text=" "  
       
      # Append text to current menu item
      text+=menu_item
      self.font.draw(surface, text, 25, y)
  
      # Loop value changes
      y+=24
      count+=1
