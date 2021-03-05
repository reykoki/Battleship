import sys
sys.path.append('../battleship')
import unittest
from unittest import mock
from unittest import TestCase

from UserInput import InputCoordinate
from UserInput import InitialInputCoordinate
from UserInput import AttackInputCoordinate
from Ship import *

class TestInput(TestCase):
    '''Test class used to mock inputs and InitialInputCoordinate and
    AttackInputCoordinate classes. Used unittest mock to mock user input.'''

    def setUp(self):
        '''Set up fixtures for tests.'''
        self.ship = Battleship()

    @mock.patch('builtins.input', side_effect=['A2', 'v'])
    def test_user_input(self, mock):
        '''Check battleship stores coordinates and doesn't return empty list.
        Mock input:
            'A2': initial starting coordinate
            'v': denoting vertical orientation
        '''
        coords = InitialInputCoordinate.get_user_input(self.ship)
        self.assertNotEqual(coords, '')

    @mock.patch('builtins.input', side_effect=['A1', 'v'])
    def test_all_coords_v(self, mock):
        '''Verifies that get_all_coords_v returns all vertical coordinates.
        Mock input:
            'A1': initial starting coordinate
            'v': denoting vertical orientation
        '''
        coords = InitialInputCoordinate.get_user_input(self.ship)
        self.assertEqual(coords, [('1', 'A'), ('2', 'A'), ('3', 'A'), ('4','A')])

    @mock.patch('builtins.input', side_effect=['A1', 'h'])
    def test_all_coords_h(self, mock):
        '''Verifies that get_all_coords_h returns all horizontal coordinates.
        Mock input:
            'A1': initial starting coordinate
            'h': denoting horizontal orientation
        '''
        coords = InitialInputCoordinate.get_user_input(self.ship)
        self.assertEqual(coords ,[('1', 'A'), ('1', 'B'), ('1', 'C'), ('1','D')])

    @mock.patch('builtins.input', side_effect=['A1'])
    def test_attackInputCoordinate(self, mock):
        '''Verify attackInputCoordinate returns correct transformed coordinates.
        Mock input:
            'A1': input attack coordinate
        '''
        attack_coord = AttackInputCoordinate.get_user_input()
        self.assertEqual(attack_coord[0], ('1', 'A'))
