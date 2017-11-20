# Player.py
# Manages the properties and actions of the Player
class Player(object):
	'Manages the properties and actions of the Player'

	# Player(self)
	# Initializes empty Player
	def __init(self):
		print(":Constructor:Empty Player")
		
	# Player(self, x, y)
	# Initializes Player with position[x,y]
	def __init__(self, x, y):

		# Debug info
		self.DEBUG=1
		self.DEBUG_TAG="[Player]"
		
		if (self.DEBUG == 1):
			print(self.DEBUG_TAG + ":Constructor:Player:" + str(x) + ":" + str(y))		

		# Variables
		self.curr_pos=[x,y]

	# info(self)
	# This function is used for debugging and shows Player data
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
	# Returns current Player position
	def getPosition(self):
		if (self.DEBUG == 1):
			print(self.DEBUG_TAG + ":getPosition:" + str(self.curr_pos[0]) + ":" + str(self.curr_pos[1]))		
		return self.curr_pos
