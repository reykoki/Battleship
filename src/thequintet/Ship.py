#!/usr/bin/env python

# baseclass for Ship
class Ship:
    """
    Generated source for class Ship
    """
    def __init__(self, name = ''):
        self._name = name

    #  Team TheQuintet, pair 1 was here.
    #  Team Quintent, pair 2 was here

    def show(self):
        """
        Generated source for method show
        """
        print("IF you can't see this then something is severely wrong!!")

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
