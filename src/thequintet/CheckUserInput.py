import numpy as np

class InputCoordinate(object):

    def __init__(self, input_coord, direction = None, ship_length = None):
        self.input_coord = input_coord
        self.direction = direction
        self.ship_length = ship_length
        self.init_coords = []

    def check_coord(self):
        input_coord = self.input_coord
        # convert letter to number with index 0
        col = ord(input_coord[0].lower()) - 97
        row = int(input_coord[1:]) - 1
        print('------')
        print(row, col)
        print('------')
        if len(input_coord) !=2:
            print('Invalid length of coordinates (must be string of length 2)')
        elif 0 > col > 9:
            print('Invalid column choice: choose a letter A-J')
        elif 0 > row > 9:
            print('Invalid row choice: choose a number 1-10')
        else:
            # return with index 0
            return [row, col]
        return []

    def on_board(self, init_coord_c, init_coord_s):
        ship_len = self.ship_length
        # init_coord_c is the one changing
        end_coord = init_coord_c + ship_len
        if end_coord > 9:
            print('Invalid coordinates, the end of the ship is off the board')
            return [], []
        coord_c_array = np.arange(init_coord_c, end_coord)
        # init_coord_s is stationary
        coord_s_array = np.zeros(ship_len, dtype=int) + init_coord_s
        return coord_c_array, coord_s_array

    def check_dir(self, init_coords):
        row_o = init_coords[0]
        col_o = init_coords[1]
        direction = self.direction.lower()

        if direction == 'h':
            # check horizontal length of ship is within grid
            rows, cols = InputCoordinate.on_board(self, col_o, row_o)
        elif direction == 'v':
            # check vertical length of ship is within grid
            cols, rows = InputCoordinate.on_board(self, row_o, col_o)
        else:
            print('Invalid direction: please choose between h and v')
            return []
        # create 2D array with [row,col] values
        ship_loc = np.column_stack((cols, rows))
        return ship_loc

    def check_input(self):
        coords = InputCoordinate.check_coord(self)
        # if this is the initial user input for setting up board there are more steps
        if self.direction:
            if len(coords) == 2:
                ship_loc = InputCoordinate.check_dir(self, coords)
                if len(ship_loc) > 0:
                    return ship_loc
            return []
        # check for if the attack coordinates are good then convert from letter/num pair to num/num pair
        else:
            return coords

