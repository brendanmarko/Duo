# LevelBuilder.py
# Reads in Level data and populates a collection to store the layout

# Imports
from Level import *
from Racer import *
from Player import *
from WallBuilder import *

# PPM Values
PPM_X=60
PPM_Y=90

class LevelBuilder:
  'Reads in Level data and populates a collection to store the layout'
    
    # Constructor(self)
  def __init__(self):
    print("LevelBuilder created.")

    # Constructor (self, level)
    # This constructor takes string; the level to be loaded
  def __init__(self, level_number):
    print("LevelBuilder created with: " + level_number)  

    # Debug info
    self.DEBUG=0
    self.DEBUG_TAG="[LevelBuilder]"

    # Variable init
    self.level_storage=[]
    self.file_path="Levels/Level" + level_number + ".txt"  
    self.curr_reader_pos=[0,0]

    # Player 
    self.p=None

		# PPM
    self.ppm=Position(PPM_X, PPM_Y)

    # WallBuilder
    self.wall_builder=WallBuilder(0, 0, self.ppm)

    # Storage
    self.wall_list=[]
    self.entity_list=[]

    # File path check
    if (self.DEBUG == 1):
      print("Value of file_path: " + self.file_path)

    self.curr_level=self.setup()

  # printLayout(self)
  # Prints current level
  def printLayout(self):
    for i in range(len(self.level_storage)):
      print(self.level_storage[i])
    
  # Returns level dimensions
  def getDimensions(self):
    return self.dimensions

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
      if (self.wall_builder.activeBuild() == 1):
        self.wall_builder.closeWall()
      
      # Previous wall endpoint NOT created; No Wall
      else:
        self.wall_builder.activateBuilder()
        self.wall_builder.updateStartPosition(self.curr_reader_pos[1], self.curr_reader_pos[0])

    # Handles Racers
    elif (char == 'r'):
      # Must scale position/dims due to origin within level file
      new_racer=Racer((PPM_X*self.curr_reader_pos[1], PPM_Y*self.curr_reader_pos[0]), 'r')
      self.entity_list.append(new_racer)  

    elif (char == 'p'):
      # Must scale position/dims due to origin within level file
      self.p=Player((PPM_X*self.curr_reader_pos[1], PPM_Y*self.curr_reader_pos[0]), 'p')
      self.entity_list.append(self.p)

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
   
    width=len(self.level_storage)
    length=len(self.level_storage[0])

    self.dimensions=[length*PPM_X, width*PPM_Y]

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
          print(self.DEBUG_TAG + ":buildGameWorld:[" + str(self.curr_reader_pos[1]) + "," + str(self.curr_reader_pos[0]) + "] " + (self.level_storage[row])[column])
  
        # Handles each individual character
        self.handleChar((self.level_storage[row])[column])
    
    # Assigns Walls to wall_list
    self.wall_list=self.wall_builder.wallCollection()
    print("[Game world build complete]")

  # setup(self)
  # Performs LevelBuilder setup
  def setup(self):
    curr_file=open(self.file_path, "r")
       
    # Reads lines from LevelXX
    for line in curr_file:
      self.level_storage.append(line.strip())

    # Close the file when finished
    curr_file.close()

    # Build Objects
    self.buildGameWorld()

  def getEntities(self):
    return self.entity_list

  def getWalls(self):
    return self.wall_list

  # getLevel(self)
  # Returns the Level object created by LevelBuilder
  def getLevel(self):
    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":getLevel")
    return self.curr_level

  # getLevel(self)
  # Returns the list containing the current Level
  def getLevelList(self):
    return self.level_storage

  # getPlayer(self)
  # Returns player object
  def getPlayer(self):
    return self.p

  # getPPM(self)
  # Returns PPM values as position
  def getPPM(self):
    return ((PPM_X, PPM_Y))
