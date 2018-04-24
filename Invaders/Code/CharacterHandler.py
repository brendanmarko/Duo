# CharacterHandler.py
# Handles controls for character object

from EventHandler import *

# Debug info
DEBUG=1

class CharacterHandler(EventHandler):
  def __init__(self):
    print("[CharacterHandler]:init")

  def handleEvent(self, event):
    if (DEBUG == 1):
      print("[CharacterHandler]:handleEvent: " + str(event))
    
    # Handles quit
    if (event.type == pygame.QUIT):
      pygame.quit()
      sys.exit()
  
    # Handles key pressed
    pressed=event.key
        
    if (DEBUG == 1):
      print("[CharacterHandler]:key_value=" + str(pressed))

    # Handles movement [N]
    if (pressed == 119 or pressed == 273):
      if (DEBUG == 1):
        print("[CharacterHandler]:up_move_cap]")
      return "N"

    # Handles movement [S]
    elif (pressed == 115 or pressed == 274): 
      if (DEBUG == 1):
       print("[CharacterHandler]:down_move_cap]")
      return "S"

    # Handles movement [W]
    elif (pressed == 97 or pressed == 276):
      if (DEBUG == 1):
        print("[CharacterHandler]:left_move_cap]")
      return "W"

		# Handles movement [E]
    elif (pressed == 100 or pressed == 275):
      if (DEBUG == 1):
        print("[CharacterHandler]:right_move_cap]")
      return "E"

    # Handles spacebar as input
    elif (pressed == 32):
      if (DEBUG == 1):
        print("[CharacterHandler]:space_cap]")
      return "FIRE"

    # Handles entry selection
    elif (pressed == 13):
      if (DEBUG == 1):
        print("[CharacterHandler]:enter_cap]")
      return "ENTER"
    
    else:
      return "OTHER"
