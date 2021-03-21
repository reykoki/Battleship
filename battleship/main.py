#!/usr/bin/env python

from ship import *
from battleshipGame import Game


def main():
    '''Initializes list of ships for game and calls game loop.'''
    ships = [minesweeper(), destroyer(), battleship(), submarine()]
    g = Game(ships)
    g.play_game()


if __name__ == "__main__":
    main()
