import sys
import numpy as np
import pandas as pd
import os
import string
import unittest
from unittest import mock
from unittest import TestCase
sys.path.append('../battleship')
from battlefield import battlefield
from Ship import Battleship

class TestInput(TestCase):
    '''Class to test battlefield class.'''

    def setUp(self):
        '''Set up fixtures for tests.'''
        self.bf = battlefield()
        self.board_size = (10, 10)
        self.test_bf = self.buildSampleBoard()

    def buildSampleBoard(self):
        '''Build sample board. Needed for tests.'''
        game_board = pd.DataFrame('-', index=[str(i) for i in range(1, self.board_size[0]+1)],
                                  columns=[chr(i)  for i in range(ord('A'),
                                  ord('Z')+1)][:self.board_size[1]])
        return game_board

    def test_GridSize(self):
        '''Check size of grid.'''
        grid = self.bf.grid
        self.assertEqual(grid.shape, self.board_size)

    def test_GameBoardArrange(self):
        '''Check arrangement of game board.'''
        game_board = self.buildSampleBoard()
        self.assertTrue((self.bf.grid == game_board).any().any())

    def test_hit(self):
        '''Check manipulation of game board.'''
        test_coords = [('3', 'A'), ('4', 'A')]
        self.bf.place_on_board(test_coords, 'Minesweeper')
        result = self.bf.attack(test_coords[1])
        self.assertEqual(result, 'You have sunk your opponents Minesweeper')
        self.assertEqual(self.bf.grid[test_coords[1][1]][test_coords[1][0]], 'X')

    def test_CorrectShips(self):
        '''Check if ships are placed in correct coordinates.'''
        test_coords = [('5', 'I'), ('5', 'J')]
        test_ship_name = 'Minesweeper'
        self.bf.place_on_board(test_coords, test_ship_name)
        val = self.bf.grid[test_coords[1][1]][test_coords[1][0]]
        self.assertEqual(val, test_ship_name)

    def test_AttackShip(self):
        '''Check that if a ship is hit, it is reported.'''
        test_coords = [('5', 'H'), ('5', 'I'), ('5', 'J')]
        test_ship_name = 'Destroyer'
        self.bf.place_on_board(test_coords, test_ship_name)
        outcome = self.bf.attack(('10', 'J'))
        self.assertEqual(outcome, 'YOU MISSED')
