# WallBuilder.py
# Handles the building of Wall objects passed from LevelBuilder

# Imports
from Wall import *
from CustomGroup import *

class WallBuilder(object):
  'Handles the building of Wall objects passed from LevelBuilder'

  # WallBuilder(self, row, col)
  # Starts a wall with the leftmost position at (row, col)
  def __init__(self, row, col, ppm):
    print("WallBuilder created.")
      
    # Debug info
    self.DEBUG=1
    self.DEBUG_TAG="[WallBuilder]"

    # PPM
    self.ppm=ppm

    # Variables
    self.x_start=row
    self.y_start=col
    self.active_check=0
    self.x_span=0
    self.y_span=0
    self.line_type=""
    
    # Storage
    self.wall_storage=CustomGroup()

  # Functions
  # active(self)
  # Checks to see if the WallBuilder has been initialized
  def activeBuild(self):
    if (self.active_check == 1):
      return 1
    else:
      return 0

  # activateBuilder(self)
  # Activates the WallBuilder; informs us that a Wall has begun construction
  def activateBuilder(self):
    
    if (self.DEBUG == 1):
        print(self.DEBUG_TAG + ":activateBuilder")
    
    # WB now active
    self.active_check=1
    self.x_span=1
    self.y_span=1

  # resetBuilder(self)
  # Returns the WallBuilder to default setup for next Wall
  def resetBuilder(self):
    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":resetBuilder")
    self.active_check=0
    self.x_span=0
    self.y_span=0    
    self.x_start=0
    self.y_start=0

  # extendWall(self)
  # Extends walls one block to the right
  def extendWall(self):
    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":extendWall")
    self.x_span+=1

  # updateStartPosition(self, x, y)
  # Updates the position where WallBuilder creates a new wall
  def updateStartPosition(self, x, y):
    if (self.DEBUG == 1):  
      print(self.DEBUG_TAG + ":updateStartPosition:" + str(x) + ":" + str(y))
    self.x_start=x
    self.y_start=y

  # closeWall(self)
  # Closes the Wall and creates a Wall object
  def closeWall(self):
    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":closeWall")
    
    self.x_span+=1

    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":closeWall:span:" + str(self.x_span) + ":" + str(self.y_span))
      print(self.DEBUG_TAG + ":closeWall:pos:" + str(self.x_start) + ":" + str(self.y_start))

    # Build Wall; value of y_span still needs to be used for vertical walls later
    new_wall=Wall(self.x_start, self.y_start, self.x_span, self.y_span)
    self.wall_storage.add(new_wall)

    # Resets the WallBuilder
    self.resetBuilder()

  # wallCollection(self)
  # Returns all Wall objects
  def wallCollection(self):
    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":wallCollection")
    return self.wall_storage
