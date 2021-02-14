#!/usr/bin/env python

# baseclass for Ship
class Battleship:
    """
    Generated source for class Ship
    """
    def __init__(self, name = 'Battleship', length = 4, coordinates = []):
        self._name = name
        self._length = length
        self.coordinates = coordinates

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

    def setCoordinates(self, ship_coords):
        """
        Set ship coordinates on board
        """
        self.coordinates = ship_coords
