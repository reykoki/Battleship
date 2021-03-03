import itertools


class LUT():
    '''LUT table used by ships and for attacks. Parent of Ship_LUT class.
    Attributes:
        row_size: row size of LUT table
        col_size: column size of LUT table
    '''

    def __init__(self, row_size=10, col_size=10):
        '''Initializes LUT class with row and column size with default being 10.'''
        self.row_size = row_size
        self.col_size = col_size

    def create_LUT(self):
        '''Creates LUT with row and column size defined.
        Returns:
            LUT: look up table with all rows and columns
        '''
        possible_rows = [str(i) for i in range(1, self.row_size+1)]
        possible_cols = [chr(i) for i in range(ord('A'),ord('Z')+1)][:self.col_size]
        LUT = list(itertools.product(possible_rows, possible_cols))
        return LUT

    @classmethod
    def get_Attack_LUT(self, row_size = 10, col_size = 10):
        attack_LUT = self(row_size, col_size)
        return attack_LUT.create_LUT()

class Ship_LUT(LUT):
    '''Creates ship LUT.'''

    def __init__(self, direction, ship_len):
        '''Initializes Ship_LUT class.
        Args:
            direction: direction of ship. 'h' for horizontal, 'v' for vertical
            ship_len: length of ship
        '''
        super().__init__()
        self.direction = direction
        self.ship_len = ship_len

    @classmethod
    def get_Ship_LUT(self, direction, ship_len):
        '''Returns ship LUT based on ship length.
        Args:
            direction: direction of ship. 'h' for horizontal, 'v' for vertical
            ship_len: length of ship
        '''
        ship_LUT = self(direction, ship_len)
        if ship_LUT.direction == 'h':
            ship_LUT.col_size = ship_LUT.col_size - ship_len + 1
        if ship_LUT.direction == 'v':
            ship_LUT.row_size = ship_LUT.row_size - ship_len + 1
        return ship_LUT.create_LUT()
