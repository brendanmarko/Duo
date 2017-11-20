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
GAME_TITLE="RACE 0.13"

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
			
			if (self.DEBUG == 1):
				print(self.DEBUG_TAG + " = = = = = = = = = = = = = = = = = =")

			# Captures events and handles them
			for event in pygame.event.get():
          
				# Event handler called
				self.event_handler.handleEvent(event)

			# Update Entities
			self.update()
	
			# Draw Entities
			self.draw(curr_level)       		

			# pygame.draw.rect(self.display_surface, (0, 255, 0), pygame.Rect(0, 0, 60, 60))
			pygame.display.flip()
			self.clock.tick(60)

	# update(self)
	# Updates data wrt Entities
	def update(self):
		if (DEBUG == 1):
			print(self.DEBUG_TAG + ":update")

	# draw(self, curr_level)
	# Prints to the Screen
	def draw(self, curr_level):
		if (self.DEBUG == 1):
			print(self.DEBUG_TAG + ":draw")
		
		# Draw the Walls
		if (DEBUG == 1):
			print(self.DEBUG_TAG + ":draw:Walls")
		
		wall_list=curr_level.getWalls()
		for x in range(len(wall_list)):
			y=wall_list[x]
			y.printWall()
			pygame.draw.rect(self.display_surface,(169, 169, 169),  y.getHitbox(), 0)
		
		# Draw the Entities
		if (DEBUG == 1):
			print(self.DEBUG_TAG + ":draw:Entities")

		entity_list=curr_level.getEntities()
		for x in range(len(entity_list)):
			y=entity_list[x]
			y.info()
			pygame.draw.circle(self.display_surface, (0, 255, 0), (y.getX() + 50, y.getY() + 50), 100, 0)
	
# Execute the Game
main=Main()
main.start()
