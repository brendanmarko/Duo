# Wall.py
# Manipulates/Creates the Wall object in the game world

# Imports
import pygame

class Wall(object):
	'Manipulates/Creates the Wall object in the game world'

	# collisionCheck(self, pos)
	# Checks if an object is colliding with the Wall
	def collisionCheck(self, pos):
		if (self.DEBUG == 1):
			print(self.DEBUG_TAG + ":collisionCheck")
		
		# Checks for row collision
		if (pos[0] >= self.row_range[0] and pos[0] <= self.row_range[1]):
			print(":collisionTrueRow")
			return 1;
		
		# Checks for column collision
		if (pos[0] >= self.col_range[0] and pos[1] <= self.col_range[1]):
			print(":collisionTrueCol")
			return 1;

		# No row/column collision occured
		return 0;
		
	# printWall(self)
	# Prints the positions of the wall
	def printWall(self):
		print(self.DEBUG_TAG + ":printWall")
		print("[" + str(self.row_range[0]) + "," + str(self.col_range[0]) + "]--->[" + str(self.row_range[1]) + "," + str(self.col_range[1]) + "]")

	# getHitbox(self):
	# Returns the Rect box that denotes a Wall
	def getHitbox(self):
		return self.hitbox

	# Wall(self, start, close)
	# Begins the build process of the Wall
	def __init__(self, root_row, root_col, span):

		# Debug info
		self.DEBUG=1
		self.DEBUG_TAG="[Wall]"
		
		# Range
		self.row_range=[0,0]
		self.col_range=[0,0]
		
		# Root positions
		self.row_range[0]=root_row
		self.col_range[0]=root_col
	
		# End positions 
		# These values will update wrt which direction the span moves
		self.row_range[1]=root_row
		self.col_range[1]=self.col_range[0]+span

		# Build Rect
		self.hitbox=pygame.Rect(self.row_range[0], self.col_range[0], 800, 200)

		if (self.DEBUG == 1):
			print(self.DEBUG_TAG + ":Constructor:" + str(root_row) + ":" + str(root_col) + ":" + str(span))
			print(self.DEBUG_TAG + ":Constructor:" + ":row_span:" + str(self.row_range))
			print(self.DEBUG_TAG + ":Constructor:" + ":col_span:" + str(self.col_range))
