import sys
import numpy as np
import os
import string
import unittest
from unittest import mock
from unittest import TestCase
from subprocess import Popen, PIPE, STDOUT

sys.path.append('../battleship')
from battleship_game import game
from Ship import Battleship
from UserInput import *
import pandas as pd

class TestInput(TestCase):
    #Test class used to mock inputs and test battleship game functionality

    @mock.patch('builtins.input', side_effect=['A2'])
    def test_AttackMove(self, mock):
        '''Test input attack coordinates are correct.'''
        bf_game = game()
        bf_game.player1_move()
        grid = pd.DataFrame('-', index=[str(i) for i in range(1, 11)],
                            columns=[chr(i) for i in range(ord('A'), ord('J') + 1)])
        grid['A']['2'] = 'O'
        self.assertEqual(bf_game.p2bf.grid['A']['2'], grid['A']['2'])

    @mock.patch('builtins.input', side_effect=['A1', 'D5', 'J9'])
    def test_PlayerTurns(self, mock):
        '''Test alternating moves between player1 and player2.'''
        bf_game = game()
        bf_game.player1_move()
        bf_game.player2_move()
        bf_game.player1_move()
        bf_game.player2_move()
        bf_game.player1_move()
        grid = pd.DataFrame('-', index=[str(i) for i in range(1, 11)],
                            columns=[chr(i) for i in range(ord('A'), ord('J') + 1)])
        grid['A']['1'] = 'O'
        grid['D']['5'] = 'O'
        grid['J']['9'] = 'O'
        self.assertEqual(bf_game.p2bf.grid['A']['1'],grid['A']['1'])
        self.assertEqual(bf_game.p2bf.grid['D']['5'],grid['D']['5'])
        self.assertEqual(bf_game.p2bf.grid['J']['9'],grid['J']['9'])

    @mock.patch('builtins.input', side_effect=[])
    def test_AIShips(self, mock):
        #Test AI Ship Setup Board.
        bf_game = game()
        ship = Battleship()
        bf_game.AI_SetUpShips(ship)
        grid = bf_game.p2bf.grid
        self.assertTrue(grid.isin(['Battleship']).any().any())

    def test_player2_move(self):
        '''Test player2 move returns string.'''
        bf_game = game()
        outcome = bf_game.player2_move()
        bf_game.AI_SetUpShips(Battleship())
        self.assertIsInstance(outcome, str)
        attack_coord = bf_game.p2.get_attack_coord()
        self.assertIsInstance(attack_coord[0], str)

    def test_end_game(self):
        '''Test end of game.'''
        bf_game = game()
        with self.assertRaises(SystemExit) as cm:
            bf_game.check_outcome('testing end of game when last ship has been sunk')


    @mock.patch('builtins.input', side_effect=['S', 'E5'])
    def test_sonar(self, mock):
        '''Test sonar'''
        bf_game = game()
        bf_game.p2bf.sonar_unlocked = True
        bf_game.player1_move()
        grid = pd.DataFrame('-', index=[str(i) for i in range(1, 11)],
                            columns=[chr(i) for i in range(ord('A'), ord('J') + 1)])
        grid['E']['3'] = '#'
        grid['E']['4'] = '#'
        grid['E']['5'] = '#'
        grid['E']['6'] = '#'
        grid['E']['7'] = '#'
        grid['D']['4'] = '#'
        grid['D']['6'] = '#'
        grid['F']['4'] = '#'
        grid['F']['6'] = '#'
        grid['C']['5'] = '#'
        grid['D']['5'] = '#'
        grid['E']['5'] = '#'
        grid['F']['5'] = '#'
        grid['G']['5'] = '#'
        ne = (bf_game.p2bf.grid != grid).any(1)
        self.assertFalse(ne.all())
