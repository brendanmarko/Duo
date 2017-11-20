# Racer.py
# Manages the properties and actions of a Racer

# Imports
from Entity import *

# Debug info
DEBUG=1
DEBUG_TAG="[Racer]"

class Racer(Entity):
	'Manages the properties and actions of a Racer'

	# Racer(self, x, y)
	# Initializes Racer with position[x,y]
	def __init__(self, x, y):
		self.object_type='r'
		Entity.__init__(self, x, y, self.object_type)
