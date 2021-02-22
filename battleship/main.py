#!/usr/bin/env python

from Ship import Battleship
from battleship_game import game


def main():
    '''Runs main game loop'''
    curr_game = game()
    curr_game.SetUpBoard()

if __name__ == "__main__":
    main()
