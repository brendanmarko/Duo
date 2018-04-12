# MenuHandler.py
# Handles controls within menu screens

from EventHandler import *

# Debug info
DEBUG=1

class MenuHandler(EventHandler):
  def __init__(self):
    print("[MenuHandler]:init")

  def handleEvent(self, event):
    if (DEBUG == 1):
      print("[MenuHandler]:handleEvent: " + str(event))
    
    # Handles [Quit]
    if (event.type == pygame.QUIT):
      pygame.quit()
      sys.exit()
  
    # Handles key presses
    pressed=pygame.key.get_pressed()
         
    if (pressed[pygame.K_w] or pressed[pygame.K_UP]):
      if (DEBUG == 1):
        print("[MenuHandler]:up_move_cap]")
      return "UP"

    elif (pressed[pygame.K_s] or pressed[pygame.K_DOWN]): 
      if (DEBUG == 1):
        print("[MenuHandler]:down_move_cap]")
      return "DOWN"

    # Handles movement [W]
    elif (pressed[pygame.K_a] or pressed[pygame.K_LEFT]):
      if (DEBUG == 1):
        print("[MenuHandler]:left_move_cap]")
      return "LEFT"

		# Handles movement [E]
    elif (pressed[pygame.K_d] or pressed[pygame.K_RIGHT]):
      if (DEBUG == 1):
        print("[MenuHandler]:right_move_cap]")
      return "RIGHT"

    # Handles entry selection
    elif (pressed[pygame.K_RETURN]):
      if (DEBUG == 1):
        print("[MenuHandler]:enter_cap]")
      return "ENTER"
    
    else:
      return "OTHER"
