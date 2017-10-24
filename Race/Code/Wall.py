# Wall.py
# Manipulates/Creates the Wall object in the game world

class Wall(object):
	'Manipulates/Creates the Wall object in the game world'

	# wallBounds(self)
	# Constructs the ranges the Wall will occupy
	def wallBounds(self):
		if (self.DEBUG == 1):
			print(self.DEBUG_TAG + ":wallBounds")

	# Wall(self, start, close)
	# Begins the build process of the Wall
	def __init__(self, root_x, root_y, span):

		# Debug info
		self.DEBUG=1
		self.DEBUG_TAG="[Wall]"
		
		# Range
		self.x_range=[0,0]
		self.y_range=[0,0]
		
		# Root positions
		self.start_x=root_x
		self.start_y=root_y

		# Affected by direction of span
		self.close_pos_x=(root_x + span) # Only Temporary until Vertical walls
		self.close_pos_y=0

		if (self.DEBUG == 1):
			print(self.DEBUG_TAG + ":Constructor:" + str(root_x) + ":" + str(root_y) + ":" + str(span))

		
