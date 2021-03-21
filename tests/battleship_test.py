import sys
sys.path.append('../battleship')
from ship import *
import unittest
from unittest import TestCase


class TestInput(TestCase):
    '''Test class used to mock inputs and test battleship game functionality.'''

    def test_Minesweeper(self):
        '''Test to ensure Battleship class returns correct information
        for Minesweeper type.'''
        ms = minesweeper()
        self.assertEqual(ms.getName(), 'MINESWEEPER')
        self.assertEqual(ms.getLength(), 2)

    def test_Destroyer(self):
        '''Test to ensure Battleship class returns correct information
        for Destroyer type.'''
        ds = destroyer()
        self.assertEqual(ds.getName(), 'DESTROYER')
        self.assertEqual(ds.getLength(), 3)

    def test_Battleship(self):
        '''Test to ensure Battleship class returns correct information
        for Battleship type.'''
        bs = battleship()
        self.assertEqual(bs.getName(), 'BATTLESHIP')
        self.assertEqual(bs.getLength(), 4)

    def test_Submarine(self):
        '''Test to ensure Submarine class returns correct information
        for Submarine type.'''
        sm = submarine()
        self.assertEqual(sm.getName(), 'submarine')
        self.assertEqual(sm.getLength(), 4)
