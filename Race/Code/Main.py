# Main.py; launches the game

# Imports
import sys
from LevelBuilder import *

# Variables
level_num=""
DEBUG=0

# Reads arguments from command line for which level to load
# If no argument is entered, 00 is rendered
if (len(sys.argv) > 1):
    level_num=sys.argv[1]
else:
    level_num="00"

# Build Level
lvl_builder=LevelBuilder(level_num)

# Assign Level
curr_level=lvl_builder.getLevel()
