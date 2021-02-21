import sys
sys.path.append('../battleship')
import unittest
from unittest import mock
from unittest import TestCase

from UserInput import InputCoordinate
from UserInput import InitialInputCoordinate
from UserInput import AttackInputCoordinate
from Ship import Battleship

class TestInput(TestCase):
    # TODO: check battleship stores coordinates
    @mock.patch('builtins.input', side_effect=['A2', 'v'])
    def test_user_input(self, mock):
        test_ship = Battleship()
        InitialInputCoordinate.get_user_input(test_ship)
        self.assertNotEqual(test_ship.coordinates, [])

    # TODO: check if initial input coordinate returns proper vertical coordinates
    @mock.patch('builtins.input', side_effect=['A1', 'v'])
    def test_all_coords_v(self, mock):
        test_ship = Battleship()
        InitialInputCoordinate.get_user_input(test_ship)
        self.assertEqual(test_ship.coordinates, [(0, 0), (1, 0), (2, 0), (3, 0)])

    # TODO: check if initial input coordinate returns proper horizontal coordinates
    @mock.patch('builtins.input', side_effect=['A1', 'h'])
    def test_all_coords_h(self, mock):
        test_ship = Battleship()
        InitialInputCoordinate.get_user_input(test_ship)
        self.assertEqual(test_ship.coordinates, [(0, 0), (0, 1), (0, 2), (0, 3)])

    # TODO: verify attackInputCoordinate returns correct coordinates
    @mock.patch('builtins.input', side_effect=['A1'])
    def test_attackInputCoordinate(self, mock):
        attack_coord = AttackInputCoordinate.get_user_input()
        self.assertEqual(attack_coord, (0, 0))
