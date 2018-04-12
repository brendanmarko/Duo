# Level.py
# Empty sandbox

from BaseState import *

class Level(BaseState):
  def __init__(self, game):
    super(Level, self).__init__(game)
    self.curr_state=None
    print("[Level]:init")

  def onEnter(self, prev_state):
    print("[Level]:onEnter")
