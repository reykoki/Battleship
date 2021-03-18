#!/usr/bin/env python

from Ship import *
from battleship_game import game
from battleshipGame import Game


def main():
    '''Runs main game loop'''
    # curr_game = game()
    # curr_game.SetUpBoard()
    ships = [Minesweeper(), Destroyer(), Battleship(), Submarine()]
    g = Game(ships)
    g.play_game()

if __name__ == "__main__":
    main()
