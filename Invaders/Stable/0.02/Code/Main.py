from Game import *

import os
import sys
import pygame

# Varibles

def main():
  g=Game()
  g.run(Menu(g))
  return 0;

# Launch main
main()
