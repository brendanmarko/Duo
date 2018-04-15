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

  # self, pos, direction, object_type, owner, ppm
  def createProjectile(self, o, p_type): 
    if (DEBUG == 1):
      print("[ProjectileFactory]:create")
    p=Projectile(o.getPos(), o.getDirection(), p_type, o, self.ppm)
    return p
