import sys
sys.path.append('../src/thequintet')
from Ship import Battleship
import unittest
from unittest import TestCase


class TestInput(TestCase):
    '''Test class used to mock inputs and test battleship game functionality.'''

    def test_Minesweeper(self):
        '''Test to ensure Battleship class returns correct information
        for Minesweeper type.'''
        ms = Battleship('Minesweeper', 2)
        self.assertEqual(ms.getName(), 'Minesweeper')
        self.assertEqual(ms.getLength(), 2)

    def test_Destroyer(self):
        '''Test to ensure Battleship class returns correct information
        for Destroyer type.'''
        ds = Battleship('Destroyer', 3)
        self.assertEqual(ds.getName(), 'Destroyer')
        self.assertEqual(ds.getLength(), 3)

    def test_Battleship(self):
        '''Test to ensure Battleship class returns correct information
        for Battleship type.'''
        bs = Battleship('Battleship', 4)
        self.assertEqual(bs.getName(), 'Battleship')
        self.assertEqual(bs.getLength(), 4)
