#!/usr/bin/env python

# baseclass for Ship
class Battleship:
    """
    Generated source for class Ship
    """
    def __init__(self, name = ''):
        self._name = name

    # getter/setters ensure encapsulation in OO programming by bundling the
    # data with the methods that operate on the data
    def setName(self, ship_name):
        """
        Set ship name
        """
        self.name = ship_name

    def getName(self):
        """
        Get ship name
        """
        return self.name

