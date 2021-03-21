#!/usr/bin/env python

class ship:
    '''Battleship class used to store ship type, length,
    coordinates and look up tables.
    Attributes:
        name: ship name - 'Minesweeper', 'Destroyer' or 'Battleship'
        length: ship length
    '''

    def __init__(self, name, length, CQ_idx):
        '''Initialized Battlefield class.
        Sets ship name, length, coordinates and gets ship's horizontal
        Args:
            name: ship type
            length: ship length
        '''
        self._name = name
        self._length = length
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

    def checkCQ(self, idx):
        sink_ship = False
        if idx == self.CQ[0]:
            if len(self.CQ) == 1:
                sink_ship = True
            else:
                self.CQ.pop()
        return sink_ship

    def checkDir(self, trans_coord, direction):
        '''
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
            ship_coords = self.getAllHCoords(trans_coord)
        elif self._direction == 'v':
            ship_coords = self.getAllVCoords(trans_coord)
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

class minesweeper(ship):
    '''Creates Minesweeper class.
    Default length = 2.
    '''
    def __init__(self):
        super().__init__(name='MINESWEEPER', length=2, CQ_idx=1)

class destroyer(ship):
    '''Creates Destroyer class.
    Default length = 3.
    '''
    def __init__(self):
        super().__init__(name='DESTROYER', length=3, CQ_idx=2)

class battleship(ship):
    '''Creates Battleship class.
    Default length = 4.
    '''
    def __init__(self):
        super().__init__(name='BATTLESHIP', length=4, CQ_idx=3)

class submarine(ship):
    '''Creates Submarine class.
    '''
    def __init__(self):
        super().__init__(name='submarine', length=4, CQ_idx=4)

    def getAllHCoords(self, trans_coord):
        ship_coords = []
        for idx in range(self._length):
            next_coord = (trans_coord[0], chr(ord(trans_coord[1]) + idx))
            ship_coords.append(next_coord)
            if idx == 1:
                next_coord = (next_coord[0]+1, next_coord[1])
                ship_coords.append(next_coord)
        return ship_coords

    def getAllVCoords(self, trans_coord):
        ship_coords = []
        for idx in range(self._length):
            next_coord = (str(int(trans_coord[0]) + idx), trans_coord[1])
            ship_coords.append(next_coord)
            if idx == 1:
                next_coord = (next_coord[0], chr(ord(next_coord[1])-1))
                ship_coords.append(next_coord)
        return ship_coords

