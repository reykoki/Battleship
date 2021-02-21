import sys
sys.path.append('../battleship')

import unittest
from player2 import player2


class Player2TestCase(unittest.TestCase):

    def test_coord_removal(self):
        p2 = player2()
        # when player2 chooses an attack coordinate, that coordinate is removed from the LUT
        orig_len = len(p2.attack_LUT)
        p2.get_attack_coord()
        red_len = len(p2.attack_LUT)
        # make sure it is removed without leaving any artifacts
        self.assertTrue(orig_len == red_len + 1)

    def test_attack_coord(self):
        p2 = player2()
        coord = p2.get_attack_coord()
        # make sure the used attack coordinate is not in the LUT
        self.assertFalse(coord in p2.attack_LUT)


