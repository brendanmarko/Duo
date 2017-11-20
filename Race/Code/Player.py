# Player.py
# Manages the properties and actions of the Player

# Imports
from Entity import *

# Debug info
DEBUG=1
DEBUG_TAG="[Player]"

class Player(Entity):
	'Manages the properties and actions of the Player'
	
	# Player(self, x, y)
	# Initializes Player with position[x,y]
	def __init__(self, x, y):		
		self.object_type='p'
		Entity.__init__(self, x, y, self.object_type)
