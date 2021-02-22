import sys

sys.path.append('../battleship')

from LUT import LUT
from LUT import Ship_LUT

import unittest
from player2 import player2

class LUTTestCase(unittest.TestCase):
    '''Class to test LUT and Ship_LUT class functionality.'''

    def test_Attack_LUT_size(self):
        '''Test attack LUT size.'''
        # the default is 10x10 board
        self.assertEqual(len(LUT.get_Attack_LUT()), 100)
        # # even if row/col are not equal, you get the correct length of legal inputs
        # for row in range(5, 8):
        #     for col in range(5, 8):
        #         expected_len = row * col
        #         lut = LUT(row_size=row, col_size=col)
        #         self.assertEqual(len(lut.get_Attack_LUT()), expected_len)

    def test_Ship_LUT(self):
        '''Test Ship_LUT.
        If you give it a ship of len 3, vertical direction give a 8x10 grid.. etc
        '''
        for shiplength in range(2, 8):
            # number of board positions that are allowed for a ship of length 'shiplength'
            num_legal_pos = (10 - shiplength + 1) * 10
            self.assertEqual(len(Ship_LUT.get_Ship_LUT('v', shiplength)), num_legal_pos)
            self.assertEqual(len(Ship_LUT.get_Ship_LUT('h', shiplength)), num_legal_pos)
