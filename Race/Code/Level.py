# Level.py
# Stores lists of game objects wrt a given level

class Level(object):

	# Level(walls, entities)
	# Creates a Level given two input lists
	def __init__(self, walls, entities):
		' Stores lists of game objects wrt a given level'

		# Debug Info
		self.DEBUG=1
		self.DEBUG_TAG="[Level]"	

		if (self.DEBUG == 1):
			print(self.DEBUG_TAG + ":Constructor")

		# Populate Level object lists
		self.w_list=walls
		self.e_list=entities

		# Preview Lists
		if (self.DEBUG == 1):
			print(self.w_list)
			print(self.e_list)

	def getWalls(self):
		return self.w_list

	def getEntities(self):
		return self.e_list
