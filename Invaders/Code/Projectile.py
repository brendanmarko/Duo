# Projectile.py
# Acts as base-class for all projectiles

from MovableEntity import *

DEBUG=0

class Projectile(MovableEntity):
  def __init__(self, pos, object_type, owner):
  # def __init__(self, pos, direction, object_type, owner):
    print("[Projectile]:init") 
    MovableEntity.__init__(self, pos, object_type)

    # Projectile owner and direction
    self.owner=owner
    # self.setDirection(direction)
  
  def update(self):
    if (DEBUG == 1):
      print("[Projectile]:update") 
    MovableEntity.update(self)
