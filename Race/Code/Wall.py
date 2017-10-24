# Wall.py
# Manipulates/Creates the Wall object in the game world

class Wall:
	'Manipulates/Creates the Wall object in the game world'
	
	# Debug info
	DEBUG=0
	DEBUG_TAB="Wall"

	# Variables
	start_pos=None
	close_pos=None
	destructible=False

	# Wall(self)
	def Wall(self):
		print("Wall created.")

	# Wall(self, start, close)
	def Wall(self, start, close)
		start_pos=start
		close_pos=close
