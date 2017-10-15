# Level.py; reads from a text file to construct the level for an instance

class Level:
	name=""
	complete=False
	
	# getName()
	# This function returns the name of the current level object
	def getName():
		return name

	# completed()
	# This function checks if the level is completed
	def completed():
		return complete

	# levelComplete()
	# This function sets the Level to be completed
	def levelComplete():
		complete=True
