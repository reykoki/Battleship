#!/usr/bin/env python

from LUT import Ship_LUT


class Ship:
    '''Battleship class used to store ship type, length,
    coordinates and look up tables.
    Attributes:
        name: ship name - 'Minesweeper', 'Destroyer' or 'Battleship'
        length: ship length
        LUT_v: vertical look up table
        LUT_h: horizontal look up table
    '''

    def __init__(self, name, length):
        '''Initialized Battlefield class.
        Sets ship name, length, coordinates and gets ship's horizontal
        and vertical LUTs
        Args:
            name: ship type
            length: ship length
        '''
        self._name = name
        self._length = length
        self._LUT_v = Ship_LUT.get_Ship_LUT('v', self._length)
        self._LUT_h = Ship_LUT.get_Ship_LUT('h', self._length)
        self._direction = None
        self._last_coord = None
        self.cq_coord = None

    def getName(self):
        '''Returns ship name.'''
        return self._name

    def getLength(self):
        '''Returns ship length.'''
        return self._length

    def getDirection(self):
        '''Returns ship direction.
        Horizontal or vertical'''
        return self._direction

    def getVerticalLUT(self):
        '''Returns ship's vertical LUT.'''
        return self._LUT_v

    def getHorizontalLUT(self):
        '''Returns ship's horizontal LUT.'''
        return self._LUT_h

    def setCQCoord(self):
        '''Sets the captain's quarters based on last coordinate'''
        if self._direction == 'h':
            self.cq_coord = (self._last_coord[0], chr(ord(self._last_coord[1] - 1)))
            print('{} h cq coor {}', self._name, self.cq_coord)
        elif self._direction == 'v':
            self.cq_coord = (str(int(self._last_coord[0] - 1)), self._last_coord[1])
            print('{} v cq coor {}', self._name, self.cq_coord)

    def checkDir(self, trans_coord, direction):
        '''Verifies coordinates are in LUT.
        Verifies direction is either 'h' for horizontal or 'v' for vertical
        Args:
            trans_coord: transformed coordinates
            direction: from user
        Returns:
            (): if invalid input
            ship_coords: returns ship horizontal or vertical coordinates
        '''
        self._direction = direction.lower()
        if self._direction == 'h':
            LUT = self.getHorizontalLUT()
            if self.inLUT(trans_coord, LUT):
                ship_coords = self.getAllHCoords(trans_coord)
                self._last_coord = ship_coords[-1]
                # self.setCQCoord()
            else:
                return ()
        elif self._direction == 'v':
            LUT = self.getVerticalLUT()
            if self.inLUT(trans_coord, LUT):
                ship_coords = self.getAllVCoords(trans_coord)
                self._last_coord = ship_coords[-1]
                # self.setCQCoord()
            else:
                return ()
        else:
            print('\nInvalid directions: please choose between h and v')
            return ()
        return ship_coords

    def getAllHCoords(self, trans_coord):
        ship_coords = []
        for idx in range(self._length):
            next_coord = (trans_coord[0], chr(ord(trans_coord[1]) + idx))
            ship_coords.append(next_coord)
        return ship_coords

    def getAllVCoords(self, trans_coord):
        ship_coords = []
        for idx in range(self._length):
            next_coord = (str(int(trans_coord[0]) + idx), trans_coord[1])
            ship_coords.append(next_coord)
        return ship_coords

    @staticmethod
    def inLUT(trans_coord, LUT):
        '''Verifies transformed coordinates are in LUT.
        Returns:
            True: if trans_coord in LUT
            False: if trans_coord not in LUT
        '''
        if trans_coord not in LUT:
            print("\nInvalid coordinates, the end of the ship is off the board, "
                  "choose another coordinate.")
            return False
        else:
            return True

class Minesweeper(Ship):
    '''Creates Minesweeper class.
    Default length = 2.
    '''
    def __init__(self):
        super().__init__(name='Minesweeper', length=2)

class Destroyer(Ship):
    '''Creates Destroyer class.
    Default length = 3.
    '''
    def __init__(self):
        super().__init__(name='Destroyer', length=3)

class Battleship(Ship):
    '''Creates Battleship class.
    Default length = 4.
    '''
    def __init__(self):
        super().__init__(name='Battleship', length=4)

class Submarine(Ship):
    '''Creates Submarine class.
    '''
    def __init__(self):
        super().__init__(name='Submarine', length=4)
        # self.submerged = submerged

    # def isSubmerged(self):
    #     '''Returns submarine submerged status.
    #
    #     Returns:
    #         True: if submerged
    #         False: if not submerged
    #     '''
    #     return self.submerged
