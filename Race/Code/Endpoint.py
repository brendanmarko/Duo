# Endpoint.py
# Represents an exit condition for level

from Entity import *

class Endpoint(Entity):
  'Represents an exit condition for level'

  def __init__(self, x, y, ppm):
    # Debug info
    self.DEBUG=1
    self.DEBUG_TAG="[Endpoint]"

    if (self.DEBUG == 1):
      print(self.DEBUG_TAG + ":init")

    self.object_type='e'
    Entity.__init__(self, x, y, self.object_type, ppm)
