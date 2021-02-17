import numpy as np

class InputCoordinate(object):

    def __init__(self, input_coord):
        self.input_coord = input_coord

    def check_coord(self):
        input_coord = self.input_coord
        # convert letter to number with index 0
        col = ord(input_coord[0].lower()) - 97
        row = int(input_coord[1:]) - 1
        if len(input_coord[1:]) > 2 :
            print('Invalid length of coordinates! Try this format: A1 - J10')
        elif 0 > col > 9:
            print('Invalid column choice: choose a letter A-J')
        elif 0 > row > 9:
            print('Invalid row choice: choose a number 1-10')
        else:
            # return with index 0
            return [row, col]
        return []


class InitialInputCoordinate(InputCoordinate):

    def __init__(self, input_coord, direction, ship_length):
        super().__init__(input_coord)
        self.direction = direction
        self.ship_length = ship_length

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
            rows, cols = self.on_board(col_o, row_o)
        elif direction == 'v':
            # check vertical length of ship is within grid
            cols, rows = self.on_board(row_o, col_o)
        else:
            print('Invalid direction: please choose between h and v')
            return []
        # create 2D array with [row,col] values
        ship_loc = np.column_stack((cols, rows))
        return ship_loc

    def check_input(self):
        coords = self.check_coord()
        # if this is the initial user input for setting up board there are more steps
        if len(coords) == 2:
            ship_loc = self.check_dir(coords)
            if len(ship_loc) > 0:
                return ship_loc
        return []

    @classmethod
    def get_user_input(self, ship_obj):
        start_coord = input('\nwhich coordinate would you like to place your {} (example A1, D5, or J9)? '.format(ship_obj.getName()))
        direction = input('\nwould you like to place your ship vertically (down) or horizontally (to the right) of your initial coordinate? [v/h] ')
        input_coord = self(start_coord, direction, ship_obj.getLength())

        ship_coords = input_coord.check_input()

        if len(ship_coords) > 0:
            ship_obj.setCoordinates(ship_coords)
        else:
            print('BAD USER INPUT: Try again!')
            self.get_user_input(ship_obj)


class AttackInputCoordinate(InputCoordinate):
    def __init__(self, input_coord):
        super().__init__(input_coord)

    @classmethod
    def get_user_input(self):
        input_coord = input('provide the coordinate you would like to attack: ')
        attack_coord = self(input_coord)
        attack_coord_rc = attack_coord.check_coord()

        if len(attack_coord_rc) == 2:
            return attack_coord_rc
        else:
            print('Try again with valid attack coordinates')
            self.get_user_input()


