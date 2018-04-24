# ArmedEntity.py
# Represents entities with weapons attached

DEBUG=1

from MovableEntity import *

class ArmedEntity(MovableEntity):
  def __init__(self, pos, object_type):
    MovableEntity.__init__(self, pos, object_type)

  def update(self):
    if (DEBUG == 1):
      print("[ArmedEntity]:update") 
    MovableEntity.update(self)    
