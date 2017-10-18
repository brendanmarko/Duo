# LevelReader.py
# This file will read in the Level data and populate a collection that stores the Level layout

class LevelReader:
	'Reads in Level data and populates a collection to store the Level layout'
		
	# Debug info
	DEBUG=0
	DEBUG_TAG="LevelReader"
	
	# Variables
	curr_file=None	

	# Constructor
	def __init__(self):
		print("LevelReader created.")

	# Constructor (1-arg)
	# This constructor takes a String as input for the level to be loaded
	def __init__(self, level):
		print("LevelReader created with: " + level)	
		
		# Variable init
		DEBUG=1
		file_path="../Levels/Level" + level + ".txt"	

		# Debug
		if (DEBUG == 1):
			print("Value of file_path: " + file_path)

		# Opens the specified file with the permissions read-only
		curr_file=open(file_path, "r")

		# Close the file when finished
		curr_file.close()
