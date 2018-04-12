# Menu.py
# Acts as the main menu for the game

import os
import sys
import pygame

from Level import *
from BaseState import *
from FontHandler import *
from MenuHandler import *
from pygame.locals import *

# Title properties
MENU_TITLE="GAME TITLE"
TITLE_SIZE=200
TITLE_COLOR=(0, 255, 0)

# Menu entries
ENTRY_COLOR=(0, 255, 0)
ENTRY_SIZE=50
SELECTED_COLOR=(0, 255, 255)

class Menu(BaseState):
  "Acts as the main menu for the game"
  
  def __init__(self, game):
    super(Menu, self).__init__(game)
    self.curr_state=None
    self.selected=0

    # Font init
    pygame.font.init()
    self.title_font=pygame.font.SysFont("DroidSans", TITLE_SIZE)
    self.entry_font=pygame.font.SysFont("DroidSans", ENTRY_SIZE)

    self.menu_list=["START GAME", "SETTINGS", "QUIT"]
    self.title=None   
    self.menus=[]
 
    # Handles input
    self.handler=MenuHandler()

  # Index arithmetic
  def selectedUp(self):
    if (self.selected == 0):
      self.selected=len(self.menu_list)-1 
    else:
      self.selected-=1

  def selectedDown(self):
    if (self.selected == len(self.menu_list)-1):
      self.selected=0 
    else:
      self.selected+=1

  def onEnter(self, prev_state):
    # Build title
    self.title=self.title_font.render(MENU_TITLE, 1, TITLE_COLOR)

    # Build menu
    for entry in self.menu_list:
      self.menus.append(self.entry_font.render(entry, 1, ENTRY_COLOR))

  def setActiveState(self, state):
    self.curr_state=state

  # Handles input events given by the Game
  def handleEvent(self, event):
    result=self.handler.handleEvent(event)

    if (result == "UP"):
      self.selectedUp()
      print("UP")

    elif (result == "DOWN"):
      self.selectedDown()
      print("DOWN")

    elif (result == "ENTER"):
      # Game
      self.game.getCurrStateMgr().changeState(Level(self.game))
      # Settings

      # Quit
      if (self.selected == 2):
        self.game.getCurrStateMgr().changeState(None)  

  def update(self, elapsed):
    print("[Menu]:update")

    # Update the selected index entry color
    for i in range(0, len(self.menu_list)):
      if (i == self.selected):
        self.menus.pop(i)
        self.menus.insert(i, self.entry_font.render(self.menu_list[i], 1, SELECTED_COLOR))
      else:
        self.menus.pop(i)
        self.menus.insert(i, self.entry_font.render(self.menu_list[i], 1, ENTRY_COLOR))

  # Calculates the center of the screen wrt the surface dimensions
  def calcCenter(self, w):
    return self.game.getWidth()/2 - w/2

  def draw(self, surface):
    print("[Menu]:draw")
  
    # Fill background
    surface.unlock()
    surface.fill((0,0,0))
    
    # Draw title
    surface.blit(self.title, (self.calcCenter(self.title.get_width()), 0))
  
    # Draw menu entries
    spacer_count=TITLE_SIZE
    counter=0

    for entry in self.menus:
      surface.blit(entry, (self.calcCenter(entry.get_width()), spacer_count))
      spacer_count+=ENTRY_SIZE

    surface.lock()

  def onExit(self): 
    print("[Menu]:onExit") 
