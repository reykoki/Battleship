import sys
sys.path.append('../battleship')
import unittest
from unittest import mock
from unittest import TestCase
import pandas as pd

from Ship import *
from grid import *

class TestInput(TestCase):

    def setUp(self):
        '''Set up fixtures for tests.'''
        self.g = grid()
        self.board_shape = (10, 10)
        self.test_grid = self.buildSampleBoard()

    def buildSampleBoard(self):
        '''Build sample board. Needed for tests.'''
        return pd.DataFrame('-', index=[str(i) for i in range(1, 11)],
                            columns=[chr(i) for i in range(ord('A'), ord('J') + 1)])

    def test_GridSize(self):
        '''Check size of grid.'''
        self.assertEqual(self.g.grid.shape, self.board_shape)

    def test_checkCoord(self):
        '''Test coordinate check functionality.'''
        test_coord = ('11', 'A')
        result = self.g.checkCoord(test_coord)
        self.assertEqual(result, ())

    def test_gameBoardArrange(self):
        '''Check arrangement of game board.'''
        game_board = self.buildSampleBoard()
        self.assertTrue((self.g.grid == game_board).any().any())

    def test_placeOnBoard(self):
        '''Test placeOnBoard functionality.'''
        test_coords = [('3', 'A'), ('4', 'A')]
        place_results = self.g.placeOnBoard(test_coords, 'minesweeper')
        self.assertEqual(place_results, True)

    def test_CorrectShips(self):
        '''Check if ships are placed in correct coordinates.'''
        test_coords = [('5', 'I'), ('5', 'J')]
        test_ship_name = 'minesweeper'
        self.g.placeOnBoard(test_coords, test_ship_name)
        val = self.g.getGridSpace(test_coords[1][0], test_coords[1][1])
        self.assertEqual(val, test_ship_name)

    def test_coordinateAttack(self):
        '''Test coordinate hit functionality.'''
        test_coords = [('3', 'A'), ('4', 'A')]
        place_results = self.g.placeOnBoard(test_coords, 'minesweeper')
        result = self.g.coordinate_attack(test_coords[1])
        self.assertEqual(result, ['YOU MISSED', None])
        self.assertEqual(self.g.grid[test_coords[1][1]][test_coords[1][0]], 'O')

    def test_sonarAttack(self):
        '''Test sonar attack functionality.'''
        ship_coord = [('5', 'D'), ('5', 'E')]
        sonar_coord = ('5', 'B')
        ms = minesweeper()
        self.g.placeOnBoard(ship_coord, ms.getName())
        self.g.sonar_attack(sonar_coord)
        self.assertTrue((self.g.grid == ms.getName()).any().any())