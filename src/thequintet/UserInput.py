import numpy as np

class InputCoordinate(object):

    def __init__(self, input_coord):
        self.input_coord = input_coord
        self.trans_coord = ()

    def check_coord(self):
        input_coord = self.input_coord
        # convert letter to number with index 0
        try:
            col = ord(input_coord[0].lower()) - 97
            row = int(input_coord[1:]) - 1
        except:
            return

        if len(input_coord[1:]) > 2 :
            print('Invalid length of coordinates! Try this format: A1 - J10')
        elif not 0 <= col <= 9:
            print('Invalid column choice: choose a letter A-J')
        elif not 0 <= row <= 9:
            print('Invalid row choice: choose a number 1-10')
        else:
            # transformed return with index 0
            self.trans_coord = (row, col)


class InitialInputCoordinate(InputCoordinate):

    def __init__(self, input_coord, direction, ship_length):
        super().__init__(input_coord)
        self.direction = direction
        self.ship_length = ship_length

    def get_all_coords_v(self):
        ship_coords = []
        for idx in range(self.ship_length):
            next_coord = (self.trans_coord[0] + idx, self.trans_coord[1])
            ship_coords.append(next_coord)
        return ship_coords

    def get_all_coords_h(self):
        ship_coords = []
        for idx in range(self.ship_length):
            next_coord = (self.trans_coord[0], self.trans_coord[1] + idx)
            ship_coords.append(next_coord)
        return ship_coords

    def on_board(self, LUT):
        if self.trans_coord not in LUT:
            print("Invalid coordinates, the end of the ship is off the board!!")
            return False
        else:
            return True

    def check_dir(self, ship_obj):
        direction = self.direction.lower()
        if direction == 'h':
            LUT = ship_obj.getHorizontalLUT()
            if self.on_board(LUT):
                ship_coords = self.get_all_coords_h()
        elif direction == 'v':
            LUT = ship_obj.getVerticalLUT()
            if self.on_board(LUT):
                ship_coords = self.get_all_coords_v()
        else:
            print('Invalid directions: please choose between h and v')
            return ()
        return ship_coords

    def check_input(self, ship_obj):
        self.check_coord()
        if len(self.trans_coord) == 2:
            ship_loc = self.check_dir(ship_obj)
            return ship_loc
        return ()

    @classmethod
    def get_user_input(cls, ship_obj):
        start_coord = input('\nwhich coordinate would you like to place your {}? '.format(ship_obj.getName()))
        direction = input('\nwould you like to place your ship vertically (down) or horizontally (to the right) of your initial coordinate? [v/h] ')
        input_coordinates = cls(start_coord, direction, ship_obj.getLength())
        ship_coords = input_coordinates.check_input(ship_obj)
        if len(ship_coords) > 0:
            ship_obj.setCoordinates(ship_coords)
        else:
            cls.get_user_input(ship_obj)


class AttackInputCoordinate(InputCoordinate):
    def __init__(self, input_coord):
        super().__init__(input_coord)

    @classmethod
    def get_user_input(cls):
        input_coord = input('provide the coordinate you would like to attack: ')
        attack_coord = cls(input_coord)
        attack_coord.check_coord()

        if len(attack_coord.trans_coord) == 2:
            return attack_coord.trans_coord
        else:
            print('Try again with valid attack coordinates')
            return cls.get_user_input()




