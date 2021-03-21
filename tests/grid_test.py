import sys
sys.path.append('../battleship')
import unittest
from unittest import mock
from unittest import TestCase

from UserInput import InputCoordinate
from UserInput import InitialInputCoordinate
from UserInput import AttackInputCoordinate
from Ship import *
from grid import *

class TestInput(TestCase):

    def setUp(self):

    def