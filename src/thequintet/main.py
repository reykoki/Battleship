#!/usr/bin/env python

from Ship import Battleship
from battleship_game import game

def main():
    curr_game = game()
    x = input('pause')
    curr_game.SetUpBoard()

if __name__ == "__main__":
    main()
