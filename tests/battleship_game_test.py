import sys
import numpy as np
import os
import string
import unittest
from unittest import mock
from unittest import TestCase
from subprocess import Popen, PIPE, STDOUT

sys.path.append('../src/thequintet')
from battleship_game import game
from Ship import Battleship
from UserInput import *

class TestInput(TestCase):
    @mock.patch('builtins.input', side_effect=['A2'])
    #TODO: Test input attack coordinates are correct
    def test_AttackMove(self, mock):
        bf_game = game()
        bf_game.player1_move()
        self.assertEqual(bf_game.p1bf.game_board, [[' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
                                                   ['1', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                   ['2', 'O', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                   ['3', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                   ['4', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                   ['5', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                   ['6', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                   ['7', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                   ['8', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                   ['9', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                   ['10', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']])
#TODO: Test alternating moves
    @mock.patch('builtins.input', side_effect=['A1','D5','J9'])
    def test_PlayerTurns(self, mock):
        bf_game = game()
        bf_game.player1_move()
        bf_game.player2_move()
        bf_game.player1_move()
        bf_game.player2_move()
        bf_game.player1_move()

        self.assertEqual(bf_game.p1bf.game_board, [[' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
                                                   ['1', 'O', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                   ['2', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                   ['3', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                   ['4', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                   ['5', '-', '-', '-', 'O', '-', '-', '-', '-', '-', '-'],
                                                   ['6', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                   ['7', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                   ['8', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                   ['9', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'O'],
                                                   ['10', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']])
#TODO: Test AI Ship Setup Board
    @mock.patch('builtins.input', side_effect=[])
    def test_AIShips(self, mock):
        bf_game = game()
        ship = Battleship()
        bf_game.AI_SetUpShips(ship)
        grid = bf_game.p2bf.grid
        if any('Battleship' in sl for sl in grid):
            assert True
        else:
            assert False

