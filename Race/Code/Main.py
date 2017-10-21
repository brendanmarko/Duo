# Main.py; launches the game

# Imports
import sys
from LevelReader import *

# Variables
level_num=""
DEBUG=1

# Reads arguments from command line for which level to load
# If no argument is entered, 00 is rendered
if (len(sys.argv) > 1):
    level_num=sys.argv[1]
else:
    level_num="00"

# Gather level information
curr_level = LevelReader(level_num)
curr_level.setup()

if (DEBUG == 1):
	curr_level.printLayout()
