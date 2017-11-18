# Main.py; launches the game

# Imports
import sys
import pygame

# Class imports
from time import sleep
from EventHandler import *
from LevelBuilder import *

# Game Info
GAME_X_DIM=800
GAME_Y_DIM=600
GAME_TITLE="RACE 0.12"

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

		# Init pygame info
		pygame.init()
  		self.display_surface = pygame.display.set_mode((GAME_X_DIM, GAME_Y_DIM))
   		pygame.display.set_caption(GAME_TITLE)
 		self.clock = pygame.time.Clock()

		# Init EventHandler
		self.event_handler=EventHandler()

		# Build Level
		self.lvl_builder=LevelBuilder(self.level_num)

	def start(self):
		if (self.DEBUG == 1):
			print(self.DEBUG_TAG + ":start")
		
		self.gameLoop(self.lvl_builder.getLevel())

	def gameLoop(self, curr_level):
		if (self.DEBUG == 1):
			print(self.DEBUG_TAG + ":gameLoop")

		# Game loop
		while True:
			for event in pygame.event.get():
          
				# Event handler called
				self.event_handler.handleEvent(event)
       		
			pygame.draw.rect(self.display_surface, (0, 255, 0), pygame.Rect(0, 0, 60, 60))
			pygame.display.flip()
			self.clock.tick(60)


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

		# Print Level	
		print(curr_level)

# Execute the Game
main=Main()
main.start()
