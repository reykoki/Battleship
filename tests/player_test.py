from io import StringIO
import sys
from unittest import mock
from unittest import TestCase
sys.path.append('../battleship')
from player import *
from ship import *


class TestInput(TestCase):
    '''Test functionality of player and notAIBot classes.'''
    def setUp(self):
        '''Define test fixtures.'''
        self.ships = [minesweeper(), destroyer(), battleship(), submarine()]
        self.p = player(self.ships)
        self.bot = notAIBot(self.ships)

    def test_playerShips(self):
        '''Test player class ships were saved correctly.'''
        self.assertEqual(self.p.ships, self.ships)

    def test_notAIBotShips(self):
        '''Test notAIBot class ships were saved correctly.'''
        self.assertEqual(self.bot.ships, self.ships)

    def test_processResult(self):
        '''Test result processing is done correctly.'''
        with self.assertRaises(SystemExit) as cm:
            result = 'last'
            self.p.processResult(result)
        self.assertEqual(cm.exception.code, None)

        result = 'sunk'
        self.p.processResult(result)
        allAttacks = {'m': 'move fleet', 's': 'sonar attack', 'l': 'laser attack'}
        self.assertEqual(self.p.validAttack, allAttacks)

    @mock.patch('builtins.input', side_effect=['A2', 'v'])
    def test_getUserShipInput(self, mock):
        '''Verify user input is correct.'''
        coords = self.p.getUserShipInput(minesweeper())
        self.assertEqual([('2', 'A'), ('3', 'A')], coords)

    @mock.patch('builtins.input', side_effect=['A2'])
    def test_getAttackCoordinate(self, mock):
        '''Verify attack coordinates are correct.'''
        coords = self.p.getAttackCoordinate('c')
        self.assertEqual(('2', 'A'), coords)

    @mock.patch('builtins.input', side_effect=['m'])
    def test_getAttackType(self, mock):
        '''Verify attack type returned is correct.'''
        allAttacks = {'m': 'move fleet', 's': 'sonar attack', 'l': 'laser attack'}
        self.p.validAttack = allAttacks
        att = self.p.getAttackType()
        self.assertEqual(att, 'm')

    @mock.patch('builtins.input', side_effect=['N'])
    def test_moveFleet(self, mock):
        '''Test move fleet functionality.'''
        dir =self.p.moveFleet()
        self.assertEqual(dir, 'N')

    @mock.patch('builtins.input', side_effect=['c', 'A1'])
    def test_moveFleet(self,mock):
        'Test move fleet attack type.'
        at =self.p.getAttack()
        self.assertEqual('c', at.getName())
        self.assertEqual(('1', 'A'), at.getCoords())

    def test_bot_ship_place(self):
        '''Verify bot ship was placed correctly.'''
        min = minesweeper()
        coords = self.bot.place_ship(min)
