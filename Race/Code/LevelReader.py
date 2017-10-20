# LevelReader.py
# This file will read in the Level data and populate a collection that stores the Level layout

class LevelReader:
    'Reads in Level data and populates a collection to store the Level layout'
		
    # Debug info
    DEBUG=0
    DEBUG_TAG="LevelReader"
	
    # Variables
    curr_file=None
    file_path=""
    level_storage=None

    # Constructor
    def __init__(self):
        print("LevelReader created.")

    # Constructor (1-arg)
    # This constructor takes a String as input for the level to be loaded
    def __init__(self, level):
	
        print("LevelReader created with: " + level)	
		
	# Variable init
        DEBUG=1
        self.level_storage=[]
        self.file_path="../Levels/Level" + level + ".txt"	

	# Debug
        if (DEBUG == 1):
            print("Value of file_path: " + self.file_path)

    # printLayout()
    # Prints current level
    def printLayout(self):
        for i in range(len(self.level_storage)):
            print(self.level_storage[i])
    
    # setup()
    # Performs LevelReader setup
    def setup(self):
	# Opens the specified file
        curr_file=open(self.file_path, "r")
       
        # Reads lines from LevelXX
        for line in curr_file:
            self.level_storage.append(line)

	# Close the file when finished
        curr_file.close()

        # Test list
        print(self.level_storage)

        # Test layout
        printLayout()
