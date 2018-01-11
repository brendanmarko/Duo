# CustomGroup.py
# An extension of the standard 'Group' storage container used by sprites

import pygame

class CustomGroup(pygame.sprite.Group): 

  def __init__(self):
    pygame.sprite.Group.__init__(self)

    # Debug info
    self.DEBUG=1
    self.DEBUG_TAG="[CustomGroup]"

    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":init")
    
    
