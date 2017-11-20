# ObjectData.py; stores information wrt game world objects

# Imports
from Position import *

# Debug info
DEBUG=1
DEBUG_TAG="[ObjectData]"

class ObjectData(object):
	'stores information regarding game world objects'
	
	def __init__(self, input_char):
		if (DEBUG == 1):
			print(DEBUG_TAG + ":init")

		# Variables
		self.dim=Position(0,0)

		# Build object
		self.buildObject(input_char)
		
	def buildObject(self, input_char):
		if (DEBUG == 1):
			print(DEBUG_TAG + ":buildObject:" + str(input_char))

		if (input_char == 'p'):
			width=1			
			height=1
			self.dim.updateData(width, height)

		elif (input_char == 'r'):
			width=1
			height=1
			self.dim.updateData(width, height)
	
		elif (input_char == 'w'):
			width=1
			height=1	
			self.dim.updateData(width, height)

	# Helpers
	def getDims(self):
		return self.dim	
