# WallBuilder.py
# Handles the building of Wall objects passed from LevelBuilder

# Imports
from Wall import *

class WallBuilder(object):
	'Handles the building of Wall objects passed from LevelBuilder'

	# WallBuilder(self, row, col)
	# Starts a wall with the leftmost position at (row, col)
	def __init__(self, row, col):
		print("WallBuilder created.")
			
		# Debug info
		self.DEBUG=1
		self.DEBUG_TAG="[WallBuilder]"

		# Variables
		self.x_start=row
		self.y_start=col
		self.active=0
		
		# Storage?

		if (self.DEBUG == 1):
			print("Start pos of Wall (" + str(row) + ", " + str(col) + ")")

	# Functions
	# builderActive(self)
	# Checks to see if the WallBuilder has been initialized
	def builderActive(self):
		if (self.active == 1):
			return 1
		else:
			return 0

	# activateBuilder(self)
	# Activates the WallBuilder; informs us that a Wall has begun construction
	def activateBuilder(self):
		
		if (self.DEBUG == 1):
				print(self.DEBUG_TAG + ":activateBuilder")
		
		# WB now active
		self.active=1

	# extendWall(self)
	# Extends walls one block to the right
	def extendWall(self):
		print("Extending Wall...")

	# closeWall(self)
	# Closes the Wall and creates a Wall object
	def closeWall(self):
		print(self.DEBUG_TAG + ":closeWall")

		# Build Wall
		new_wall = Wall(0,0)
