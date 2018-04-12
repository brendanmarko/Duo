# Main.py; launches the game

# Imports
import sys
import pygame

from Game import *

def main():
  g=Game()
  g.run(Menu(g))
  return 0

main()
