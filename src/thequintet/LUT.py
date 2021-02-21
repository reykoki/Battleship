import itertools

class LUT():
    def __init__(self, row_size = 10, col_size = 10):
        self.row_size = row_size
        self.col_size = col_size

    def create_LUT(self):
        possible_rows = list(range(self.row_size))
        possible_cols = list(range(self.col_size))
        LUT = list(itertools.product(possible_rows, possible_cols))
        return LUT

    @classmethod
    def get_Attack_LUT(self, row_size = 10, col_size = 10):
        attack_LUT = self(row_size, col_size)
        return attack_LUT.create_LUT()

class Ship_LUT(LUT):
    def __init__(self, direction, ship_len):
        super().__init__()
        self.direction = direction
        self.ship_len = ship_len

    @classmethod
    def get_Ship_LUT(self, direction, ship_len):
        ship_LUT = self(direction, ship_len)
        if ship_LUT.direction == 'h':
            ship_LUT.col_size = ship_LUT.col_size - ship_len + 1
        if ship_LUT.direction == 'v':
            ship_LUT.row_size = ship_LUT.row_size - ship_len + 1
        return ship_LUT.create_LUT()




