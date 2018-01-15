# Wall.py
# A collection of WallSegments form Walls

# Class imports
from Entity import *
from CustomGroup import *
from WallSegment import *

class Wall(object):
  'A collection of WallSegments form Walls'
  
  def __init__(self, x_start, y_start, x_span, y_span, ppm):
    # Debug info
    self.DEBUG=1
    self.DEBUG_TAG="[Wall]"
  
    # Storage 
    self.wall_section=CustomGroup()

    # Build WallSegments
    for x in range(x_span):
      new_segment=WallSegment(x_start + x, y_start, ppm)
      self.wall_section.add(new_segment) 

  def getWall(self):
    return self.wall_section
