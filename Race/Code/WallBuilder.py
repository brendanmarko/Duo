# WallBuilder.py
# Handles the building of Wall objects passed from LevelBuilder

class WallBuilder:
	'Handles the building of Wall objects passed from LevelBuilder'

	# Debug info
	DEBUG=1
	DEBUG_TAG="WallBuilder"

	# Variables
	x_start=0
	y_start=0
	x_close=0
	y_close=0

	# WallBuilder(self, row, col)
	# Starts a wall with the leftmost position at (row, col)
	def WallBuilder(self, row, col):
		print("WallBuilder created.")
		
