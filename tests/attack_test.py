import unittest
from unittest import mock
from unittest import TestCase

import sys
sys.path.append('../battleship')
from attack import *

class TestInput(TestCase):
    '''Test class used to mock inputs and test attack functionality.'''

    def setUp(self):
        '''Set up fixtures for attack type tests.'''
        self.coords = ('2', 'D')
        self.direction = 'h'

    def test_coordAttack(self):
        '''Test coordAttack functionality.'''
        name = 'c'
        a = attack()
        at = a.createAttack(name, self.coords)
        self.assertEqual(at.getCoords(), self.coords)

    def test_sonarAttack(self):
        '''Test sonarAttack functionality.'''
        name = 's'
        s = attack()
        sp = s.createAttack(name, self.coords)
        self.assertEqual(sp.getCoords(), self.coords)

    def test_spaceLaserAttack(self):
        '''Test sonarAttack functionality.'''
        name = 'l'
        l = attack()
        la = l.createAttack(name, self.coords)
        self.assertEqual(la.getCoords(), self.coords)

    def test_moveFleet(self):
        '''Test move fleet functionality.'''
        name = 'm'
        m = attack()
        mf = m.createAttack(name, self.direction)
        self.assertEqual(mf.getDirection(), self.direction)
