from Game import *

# Varibles
W=800
H= 600
C="SAMPLE"

def main():
  g=Game(C, W, H)
  g.run(Menu(g))
  return 0;

# Launch main
main()
