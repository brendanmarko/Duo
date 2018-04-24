# Player.py
# Manages the properties and actions of the Player

# Imports
from ArmedEntity import *
from CharacterHandler import *

DEBUG=1
DEBUG_TAG="[Player]"

class Player(ArmedEntity):
  'Manages the properties and actions of the Player'
  
  # Initializes player
  def __init__(self, pos, object_type):    
    ArmedEntity.__init__(self, pos, object_type)

  def update(self):
    print("[Player]:update")
    ArmedEntity.update(self)
