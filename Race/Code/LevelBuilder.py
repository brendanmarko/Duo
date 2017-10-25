# LevelBuilder.py
# Reads in Level data and populates a collection to store the Level layout

# Imports
from Racer			import *
from WallBuilder 	import *

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
		self.DEBUG_TAG="[LevelBuilderl"

		# Variable init
		self.level_storage=[]
		self.file_path="Levels/Level" + level + ".txt"	
		self.curr_reader_pos=[0,0]

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
		print(self.DEBUG_TAG + ":handleChar:" + char)
		
		# Handles characters wrt their designation	
		if (char == ' '):
			print("Empty space found.")
		
		# Handles walls
		elif (char == 'w'):
			print("Wall found.")

			# Previous Wall endpoint created; Wall opened
			if (self.wall_builder.builderActive() == 1):
				self.wall_builder.closeWall()
			
			# Previous wall endpoint NOT created; No Wall
			elif (self.wall_builder.builderActive() == 0):
				self.wall_builder.activateBuilder()
				self.wall_builder.updateStartPosition(self.curr_reader_pos[0], self.curr_reader_pos[1])

		# Handles Racers
		elif (char == 'r'):
			print("Racer found.")
			new_racer=Racer(self.curr_reader_pos[0], self.curr_reader_pos[1])
			

		elif (char == 'd'):
			print("Destructible found.")

		elif (char == '-'):
			print("Wall connector found.")
			self.wall_builder.extendWall()

		else:
			print("Default case.")
		

	# buildGameWorld(self)
	# Reads from level_storage and builds Objects
	def buildGameWorld(self):
		print("[Building Game world]")

		# Represents Rows and Columns respectively
		self.curr_reader_pos[0]=0
		self.curr_reader_pos[1]=0
		
		# Outer for-loop iterates over rows (Y-axis)
		for row in range(len(self.level_storage)):
	
			# Update row before next columns iteration
			self.curr_reader_pos[0]=row

			# Inner for-loop iterates over columns (X-axis)
			for column in range(len(self.level_storage[row])):
				
				# Update column value before next row
				self.curr_reader_pos[1]=column

				# Outputs the current character being read within the Level
				if (self.DEBUG == 1):
					print(self.DEBUG_TAG + ":buildGameWorld:[" + str(self.curr_reader_pos[0]) + "," + str(self.curr_reader_pos[1]) + "] " + (self.level_storage[row])[column])
	
				# Handles each individual character
				self.handleChar((self.level_storage[row])[column])

		print("[Game world build complete]")

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
	
		# Preview Walls
		self.wall_builder.wallCollection()

	# getLevel(self)
	# Returns the list containing the current Level
	def getLevelList(self):
		return self.level_storage
