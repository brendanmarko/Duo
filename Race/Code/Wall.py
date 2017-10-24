# Wall.py
# Manipulates/Creates the Wall object in the game world

class Wall(object):
	'Manipulates/Creates the Wall object in the game world'

	# Variables
	destructible=False

	# Wall(self)
	def __init__(self):
		print("Wall created.")

	# Wall(self, start, close)
	def __init__(self, start, close):
		print("Wall created.")

		# Debug info
		self.DEBUG=0
		self.DEBUG_TAB="Wall"
		
		# Variables
		self.start_pos_x=0
		self.start_pos_y=0
		self.close_pos_x=0
		self.close_pos_y=0
