# LevelBuilder.py
# Reads in Level data and populates a collection to store the Level layout

class LevelBuilder:
	'Reads in Level data and populates a collection to store the Level layout'
		
    # Debug info
	DEBUG=0
	DEBUG_TAG="LevelBuilder"
	
    # Variables
	curr_file=None
	file_path=""
	level_storage=None

    # Constructor(self)
	def __init__(self):
		print("LevelBuilder created.")

    # Constructor (self, level)
    # This constructor takes a String; the level to be loaded
	def __init__(self, level):
		print("LevelBuilder created with: " + level)	
		
		# Variable init
		self.DEBUG=1
		self.level_storage=[]
		self.file_path="Levels/Level" + level + ".txt"	

		# Debug
		if (self.DEBUG == 1):
			print("Value of file_path: " + self.file_path)

    # printLayout(self)
    # Prints current level
	def printLayout(self):
		for i in range(len(self.level_storage)):
			print(self.level_storage[i]), 
    
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

		elif (char == 'd'):
			print("Destructible found.")

		elif (char == '-'):
			print("Wall connector found.")

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
