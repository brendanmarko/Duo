# ProjectileFactory.py
# Handles the creation of projectiles, returns result to objects

DEBUG=1

from Projectile import *

class ProjectileFactory(object):
  'Handles the creation of projectiles, returns result to objects'

  def __init__(self, input_ppm):
    if (DEBUG == 1):
      print("[ProjectileFactory]:init")
    self.ppm=input_ppm
    self.active_p=[]
  
  # Create and add Projectile to object targeted by createProjectile()
  def createProjectile(self, o, projectile_type): 
    if (DEBUG == 1):
      print("[ProjectileFactory]:create")

    # Projectile requires position tuple, not Position object
    p=Projectile((o.getX(),o.getY()), projectile_type, o)
    self.active_p.append(p)

  def update(self):
    # Update projectiles
    for p in self.active_p:
      p.update()

  def getActiveProjectiles(self):
    return self.active_p
