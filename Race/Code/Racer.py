# Racer.py
# Manages the properties and actions of a Racer
class Racer(object):
	'Manages the properties and actions of a Racer'

	# Racer(self)
	# Initializes empty Racer
	def __init(self):
		print(":Constructor:Empty Racer")
		
	# Racer(self, x, y)
	# Initializes Racer with position[x,y]
	def __init__(self, x, y):

		# Debug info
		self.DEBUG=1
		self.DEBUG_TAG="[Racer]"
		
		if (self.DEBUG == 1):
			print(self.DEBUG_TAG + ":Constructor:Racer:" + str(x) + ":" + str(y))		

		# Variables
		self.curr_pos=[x,y]

	# info(self)
	# This function is used for debugging and shows Racer data
	def info(self):
		if (self.DEBUG == 1):
			print(self.DEBUG_TAG + ":info")
			print("Position: [" + str(self.curr_pos[0]) + ":" + str(self.curr_pos[1]) + "]")		

	# getX(self)
	# Return X location of Entity
	def getX(self):
		return self.curr_pos[0]

	# getY(self)
	# Return Y location of Entity
	def getY(self):
		return self.curr_pos[1]

	# getPosition(self)
	# Returns current Racer position
	def getPosition(self):
		if (self.DEBUG == 1):
			print(self.DEBUG_TAG + ":getPosition:" + str(self.curr_pos[0]) + ":" + str(self.curr_pos[1]))		
		return self.curr_pos
