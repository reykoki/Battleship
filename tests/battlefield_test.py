import sys
import numpy as np
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

    def buildSampleBoard(self):
        '''Build sample board. Needed for tests.'''
        numbers = []
        for i in range(1,11):
            numbers.append(str(i))
        letters = []
        letters.extend(' ')
        letters.extend(map(chr, range(ord('A'), ord('J')+1)))
        game_board = []
        game_board.append(letters)
        for number in numbers:
                row = []
                row.append(number)
                row.extend(['-'] * 10)
                game_board.append(row)
        return game_board

    def test_GridSize(self):
        '''Check size of grid.'''
        grid = np.array(self.bf.grid)
        self.assertEqual(grid.shape[0], 10)
        self.assertEqual(grid.shape[1], 10)

    def test_GameBoardSize(self):
        '''Check size of game board.'''
        self.assertEqual(len(self.bf.number_coordinates), 10)
        self.assertEqual(len(self.bf.letter_coordinates), 11)

    def test_GameBoardArrange(self):
        '''Check arrangement of game board.'''
        game_board = self.buildSampleBoard()
        self.assertEqual(self.bf.game_board, game_board)

    def test_GameBoardManipulation(self):
        '''Check manipulation of game board.'''
        self.bf.modifyBoardAttacks((4, 3), 'MISS')
        board_miss = [[' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
                      ['1', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                      ['2', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                      ['3', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                      ['4', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                      ['5', '-', '-', '-', 'O', '-', '-', '-', '-', '-', '-'],
                      ['6', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                      ['7', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                      ['8', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                      ['9', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                      ['10', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]
        self.assertEqual(self.bf.game_board, board_miss)
    def test_CorrectShips(self):
        '''Check if ships are placed in correct coordinates.'''
        ship_test = Battleship(length=2, coordinates=[[0, 0], [1, 0]])
        self.bf.modifyBoardShips(ship_test)
        board_ship = [[' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
                      ['1', '&', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                      ['2', '&', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                      ['3', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                      ['4', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                      ['5', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                      ['6', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                      ['7', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                      ['8', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                      ['9', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                      ['10', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]
        self.assertEqual(self.bf.game_board, board_ship)

    def test_AttackShip(self):
        '''Check that if a ship is hit, it is reported.'''
        ship_test = Battleship(length=2, coordinates=[[0, 0], [1, 0]])
        self.bf.modifyBoardShips(ship_test)
        outcome = self.bf.attack([0, 0])
        self.assertEqual(outcome, 'MISS')
