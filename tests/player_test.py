import unittest
from unittest import mock
from unittest import TestCase

import sys
sys.path.append('../battleship')
from player import *
from Ship import *

class TestInput(TestCase):
    '''Test functionality of player and notAIBot classes'''

    def setUp(self):
        self.ships = [Minesweeper(), Destroyer(), Battleship(), Submarine()]
        self.p = player(self.ships)
        self.bot = notAIBot(self.ships)

    def test_playerShips(self):
        self.assertEqual(self.p.ships, self.ships)

    def test_notAIBotShips(self):
        self.assertEqual(self.bot.ships, self.ships)
