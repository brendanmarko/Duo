# Projectile.py
# Acts as base-class for all projectiles

from MovableEntity import *

class Projectile(MovableEntity):
  def __init__(self, pos, direction, object_type, owner, ppm):
    print("[Projectile]:init") 
    MovableEntity.__init__(self, pos, object_type, ppm)

    # Projectile owner and direction
    self.owner=owner
    self.setDirection(direction)
  
