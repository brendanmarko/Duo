# Entity.py; base class for in-game objects

# Imports
from Position import *
from ObjectData import *

# Debug info
DEBUG=1
DEBUG_TAG="[Entity]"

class Entity(object):
	'base class for in-game objects'

	def __init__(self, x, y, object_type):
		if (DEBUG == 1):
			print(DEBUG_TAG + ":init")
		self.curr_pos=Position(x, y)
		self.info=ObjectData(object_type)

	def	getX(self):
		return self.curr_pos.getX()

	def getY(self):
		return self.curr_pos.getY()

	def getWidth(self):
		return self.info.getDims().getX()

	def getHeight(self):
		return self.info.getDims().getY()
