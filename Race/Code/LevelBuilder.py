# LevelBuilder.py
# Reads in Level data and populates a collection to store the Level layout

# Imports
from WallBuilder import *

class LevelBuilder:
	'Reads in Level data and populates a collection to store the Level layout'
		
    # Constructor(self)
	def __init__(self):
		print("LevelBuilder created.")

    # Constructor (self, level)
    # This constructor takes a String; the level to be loaded
	def __init__(self, level):
		print("LevelBuilder created with: " + level)	

    	# Debug info
		self.DEBUG=1
		self.DEBUG_TAG="LevelBuilder"

		# Variable init
		self.level_storage=[]
		self.file_path="Levels/Level" + level + ".txt"	

		# WallBuilder
		self.wall_builder=WallBuilder(0,0)

		# File path check
		if (self.DEBUG == 1):
			print("Value of file_path: " + self.file_path)

    # printLayout(self)
    # Prints current level
	def printLayout(self):
		for i in range(len(self.level_storage)):
			print(self.level_storage[i])
    
	# handleChar(self, char)
	# Constructs Objects based upon character being passed
	def handleChar(self, char):
		print("Inside handleChar with: " + char)
		
		# Handles characters wrt their designation	
		if (char == '.'):
			print("Empty space found.")
		
		# Deals with walls
		elif (char == 'w'):
			print("Wall found.")

			# Closing endpoint for active Wall found
			if (self.wall_builder.builderActive() == 1):
				print("WallBuilder already awake.")
				self.wall_builder.closeWall()
			
			# Previous wall piece NOT detected
			elif (self.wall_builder.builderActive() == 0):
				self.wall_builder.activateBuilder()
				print("wallBuilder awake.")

		elif (char == 'd'):
			print("Destructible found.")

		elif (char == '-'):
			print("Wall connector found.")
			
			# Handles the extensions of the Wall
			self.wall_builder.extendWall()

		else:
			print("Default case.")
		

	# buildGameWorld(self)
	# Reads from level_storage and builds Objects
	def buildGameWorld(self):
		print("[Building Game world]")

		row=0
		col=0
		
		# Outer for-loop iterates over rows
		for x in range(len(self.level_storage)):
	
			# Inner for-loop iterates over columns
			for y in range(len(self.level_storage[x])):
				
				# Outputs the current character being read within the Level
				if (self.DEBUG == 1):
					print("Value: " + str(row) + ", " + str(col) + "	" + (self.level_storage[x])[y])
	
				# Handles each individual character
				self.handleChar((self.level_storage[x])[y])
				col+=1

			# Iterations between rows
			row+=1
			col=0

		print("[Game world complete]")

    # setup(self)
    # Performs LevelBuilder setup
	def setup(self):
		# Opens the specified file
		curr_file=open(self.file_path, "r")
       
        # Reads lines from LevelXX
		for line in curr_file:
			self.level_storage.append(line.strip())

		# Close the file when finished
		curr_file.close()

        # Build Objects
		self.buildGameWorld()
	
	# getLevel(self)
	# Returns the list containing the current Level
	def getLevelList(self):
		return self.level_storage
