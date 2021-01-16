import pygame
from player import Player

# create a second class that will represent our game
class Game:

    def __init__(self):
        # generate our player
        self.player = Player()
        self.pressed = {}