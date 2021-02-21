import sys
sys.path.append('../src/thequintet')
from Ship import Battleship
import unittest
from unittest import TestCase

class TestInput(TestCase):
    # TODO: check Minesweeper name and length are correct
    def test_Minesweeper(self):
        ms = Battleship('Minesweeper', 2)
        self.assertEqual(ms.getName(), 'Minesweeper')
        self.assertEqual(ms.getLength(), 2)

    # TODO: check Destroyer name and length are correct
    def test_Destroyer(self):
        ds = Battleship('Destroyer', 3)
        self.assertEqual(ds.getName(), 'Destroyer')
        self.assertEqual(ds.getLength(), 3)

    # TODO: check Battleship name and length are correct
    def test_Battleship(self):
        bs = Battleship('Battleship', 4)
        self.assertEqual(bs.getName(), 'Battleship')
        self.assertEqual(bs.getLength(), 4)