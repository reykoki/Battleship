#!/usr/bin/env python

from LUT import Ship_LUT


class Battleship:
    '''Battleship class used to store ship type, length,
    coordinates and look up tables.
    Attributes:
        coordinates: ship's location coordinates
    '''

    def __init__(self, name='Battleship', length=4, coordinates=[]):
        '''Initialized Battlefield class.
        Sets ship name, length, coordinates and gets ship's horizontal
        and vertical LUTs
        Args:
            name: ship type, default is 'Battleship'
            length: ship length, default is 4
            coordinates: list of ship coordinates on board
        '''
        self._name = name
        self._length = length
        self.coordinates = coordinates
        self._LUT_v = Ship_LUT.get_Ship_LUT('v', self._length)
        self._LUT_h = Ship_LUT.get_Ship_LUT('h', self._length)

    def setName(self, ship_name):
        '''Set ship name.'''
        self._name = ship_name

    def getName(self):
        '''Returns ship name.'''
        return self._name

    def getLength(self):
        '''Returns ship length.'''
        return self._length

    def getVerticalLUT(self):
        '''Returns ship's vertical LUT.'''
        return self._LUT_v

    def getHorizontalLUT(self):
        '''Returns ship's horizontal LUT.'''
        return self._LUT_h

    def setCoordinates(self, ship_coords):
        '''Set ship coordinates on board.
        Args:
            ship_coords: list of ship coordinates
        '''
        self.coordinates = ship_coords

    def getCoordinates(self):
        '''Get ship coordinates on board.'''
        return self.coordinates
