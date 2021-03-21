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

    def __init__(self, name, length, CQ_idx):
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
        self.CQ = self.setCQ(CQ_idx)

    def setCQ(self, CQ_idx):
        CQ = [CQ_idx, CQ_idx]
        if self._length == 2:
            CQ.pop()
        return CQ

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

    def checkCQ(self, idx):
        sink_ship = False
        if idx == self.CQ[0]:
            if len(self.CQ) == 1:
                sink_ship = True
            else:
                self.CQ.pop()
        return sink_ship

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

class minesweeper(Ship):
    '''Creates Minesweeper class.
    Default length = 2.
    '''
    def __init__(self):
        super().__init__(name='MINESWEEPER', length=2, CQ_idx=1)

class destroyer(Ship):
    '''Creates Destroyer class.
    Default length = 3.
    '''
    def __init__(self):
        super().__init__(name='DESTROYER', length=3, CQ_idx=2)

class battleship(Ship):
    '''Creates Battleship class.
    Default length = 4.
    '''
    def __init__(self):
        super().__init__(name='BATTLESHIP', length=4, CQ_idx=3)

class submarine(Ship):
    '''Creates Submarine class.
    '''
    def __init__(self):
        super().__init__(name='submarine', length=4, CQ_idx=4)

