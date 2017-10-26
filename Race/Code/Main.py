# Main.py; launches the game

# Imports
import sys
from time import sleep
from LevelBuilder import *

class Main(object):
	'launches the game'	

	def __init__(self):
		# Variables
		self.level_num=""

		# Debug info
		self.DEBUG=1
		self.DEBUG_TAG="[Main]"

		# Reads arguments from command line for which level to load
		# If no argument is entered, 00 is rendered
		if (len(sys.argv) > 1):
			self.level_num=sys.argv[1]
		else:
			self.level_num="00"

		# Build Level
		self.lvl_builder=LevelBuilder(self.level_num)

	def start(self):
		if (self.DEBUG == 1):
			print(":start")
		
		self.gameLoop(self.lvl_builder.getLevel())

	def gameLoop(self, curr_level):
		if (self.DEBUG == 1):
			print(self.DEBUG_TAG + ":gameLoop")

		# Game loop
		x=0
		while(x <= 180):
			print(str(x))
			
			# Delays updates for 1/60s : 60FPS
			sleep(1/60)
			
			# Update

			# Print 
			self.draw(curr_level)

			x+=1

	# draw(self)
	# Prints to the Screen
	def draw(self, curr_level):
		if (self.DEBUG == 1):
			print(self.DEBUG_TAG + ":draw")
		
		# Draw Walls
		for wall in curr_level.getWalls():
			print("WALL")

		# Draw entities
		for entity in curr_level.getEntities():
			print("ENTITY")

# Execute the Game
main=Main()
main.start()
