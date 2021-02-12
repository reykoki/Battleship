#!/usr/bin/env python
""" generated source for module Ship """
#  This is the  baseclass for your ship.  Modify accordingly
#  TODO: practice good OO design

class Ship(object):
    """
    Generated source for class Ship
    """
    name = str()

    # def __init__(self, name):
    #     self.setName(name)

    #  Team TheQuintet, pair 1 was here.
    #  Team Quintent, pair 2 was here
    #  TODO: create appropriate getter and setter methods
    #  TODO: Understand encapsulation
    #  TODO: Understand what these todo comments mean
    def show(self):
        """
        Generated source for method show
        """
        #  dunno why this is here maybe it is just an example method
        print("IF you can't see this then something is severely wrong!!")

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
