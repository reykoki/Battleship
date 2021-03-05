import sys
sys.path.append('../src/thequintet')
sys.path.append('../battleship')

import unittest
from unittest import TestCase
from player2 import player2


class Player2TestCase(TestCase):
    '''Class to test player2 functionality.'''

    def setUp(self):
        '''Set up fixtures for tests.'''
        self.p2 = player2()

    def test_coord_removal(self):
        '''Test coordinate removal.'''
        # when player2 chooses an attack coordinate, that coordinate is removed from the LUT
        orig_len = len(self.p2.attack_LUT)
        self.p2.get_attack_coord()
        red_len = len(self.p2.attack_LUT)
        # make sure it is removed without leaving any artifacts
        self.assertTrue(orig_len == red_len + 1)

    def test_attack_coord(self):
        '''Test attack coordinate.'''
        coord = self.p2.get_attack_coord()
        # make sure the used attack coordinate is not in the LUT
        self.assertFalse(coord in self.p2.attack_LUT)
