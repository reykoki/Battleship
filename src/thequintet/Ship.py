#!/usr/bin/env python

# baseclass for Ship
from LUT import Ship_LUT
class Battleship:
    """
    Generated source for class Ship
    """
    def __init__(self, name = 'Battleship', length = 4, coordinates = []):
        self._name = name
        self._length = length
        self.coordinates = coordinates
        self._LUT_v = Ship_LUT.get_Ship_LUT('v', self._length)
        self._LUT_h = Ship_LUT.get_Ship_LUT('h', self._length)

    # getter/setters ensure encapsulation in OO programming by bundling the
    # data with the methods that operate on the data
    def setName(self, ship_name):
        """
        Set ship name
        """
        self._name = ship_name

    def getName(self):
        """
        Get ship name
        """
        return self._name

    def getLength(self):
        """
        Get ship name
        """
        return self._length

    def getVerticalLUT(self):
        """
        Get ship name
        """
        return self._LUT_v

    def getHorizontalLUT(self):
        """
        Get ship name
        """
        return self._LUT_h

    def setCoordinates(self, ship_coords):
        """
        Set ship coordinates on board
        """
        self.coordinates = ship_coords
