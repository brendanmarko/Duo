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

	# getPosition(self)
	# Returns current Racer position
	def getPosition(self):
		if (self.DEBUG == 1):
			print(self.DEBUG_TAG + ":getPosition:" + str(self.curr_pos[0]) + ":" + str(self.curr_pos[1]))		
		return self.curr_pos
