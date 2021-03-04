import numpy as np


class InputCoordinate(object):
    '''Class to manipulate input coordinates.
    Parent class to InitialInputCoordinate and AttackInputCoordinate
    Attributes:
        input_coord: user input coordinates
        trans_coord: initialized as empty but represent transformed coordinates
    '''

    def __init__(self, input_coord):
        '''Initializes InputCoordinate class.
        Creates empty tuple for transformed coordinates which are coordinates
        in terms of the grid rather than game board
        Args:
            input_coord: user input coordinates
        '''
        self.input_coord = input_coord
        self.trans_coord = ()

    def check_coord(self):
        '''Verifies user input coordinates are inside the game board.
        Converts input coordinates from game board coordinates to grid
        coordinates
        Stores transformed coordinates if inside game board
        Prints invalid choice of coordinates message
        '''
        #TODO: make it so that if you change the board dimensions, this will also be changed
        valid_cols = [chr(i) for i in range(ord('A'),ord('J')+1)]
        valid_rows = [str(i) for i in range(1,11)]
        input_coord = self.input_coord
        good_coords = True
        # convert letter to number with index 0
        try:
            col = input_coord[0].upper()
            row = input_coord[1:]
        except:
            return

        if col not in valid_cols:
            print('\nInvalid column choice: choose a letter A-J')
            good_coords = False
        if row not in valid_rows:
            print('\nInvalid row choice: choose a number 1-10')
            good_coords = False
        if good_coords:
            # transformed return with index 0
            self.trans_coord = (row, col)


class InitialInputCoordinate(InputCoordinate):
    '''Class used to process user input coordinates for ship placement.
    Child of InputCoordinate.'''
    def __init__(self, input_coord, direction, ship_length):
        '''Initializes InitialInputCoordinate.
        Args:
            input_coord: user given input coordinate
            direction: ship direction. 'h' for horizontal and 'v' for vertical
            ship_length: ship length
        '''
        super().__init__(input_coord)
        self.direction = direction
        self.ship_length = ship_length

    def get_all_coords_v(self):
        '''Returns all vertical ship coordinates.
        Returns:
            ship_coords: list of vertical ship coordinates
        '''
        ship_coords = []
        for idx in range(self.ship_length):
            next_coord = (str(int(self.trans_coord[0]) + idx), self.trans_coord[1])
            ship_coords.append(next_coord)
        return ship_coords

    def get_all_coords_h(self):
        '''Returns all horizontal ship coordinates.
        Returns:
            ship_coords: list of horizontal ship coordinates
        '''
        ship_coords = []
        for idx in range(self.ship_length):
            next_coord = (self.trans_coord[0], chr(ord(self.trans_coord[1])+idx))
            ship_coords.append(next_coord)
        return ship_coords

    def on_board(self, LUT):
        '''Verifies transformed coordinates are in LUT.
        Returns:
            True: if trans_coord in LUT
            False: if trans_coord not in LUT
        '''
        if self.trans_coord not in LUT:
            print("\nInvalid coordinates, the end of the ship is off the board, choose another coordinate.")
            return False
        else:
            return True

    def check_dir(self, ship_obj):
        '''Verifies coordinates are in LUT.
        Verifies direction is either 'h' for horizontal or 'v' for vertical
        Args:
            ship_obj: needed to get ship's direction
        Returns:
            ship_coords: returns ship horizontal or vertical coordinates
        '''
        direction = self.direction.lower()
        if direction == 'h':
            LUT = ship_obj.getHorizontalLUT()
            if self.on_board(LUT):
                ship_coords = self.get_all_coords_h()
            else:
                return ()
        elif direction == 'v':
            LUT = ship_obj.getVerticalLUT()
            if self.on_board(LUT):
                ship_coords = self.get_all_coords_v()
            else:
                return ()
        else:
            print('\nInvalid directions: please choose between h and v')
            return ()
        return ship_coords

    def check_input(self, ship_obj):
        '''Verifies user input.
        Args:
            ship_obj: used to check ship direction
        Returns:
            ship_loc: ships coordinates
            (): if the length of the user input was greater than 2
        '''
        self.check_coord()
        if len(self.trans_coord) == 2:
            ship_loc = self.check_dir(ship_obj)
            return ship_loc
        return ()

    @classmethod
    def get_user_input(cls, ship_obj):
        '''Used to get user input such as starting coordinates and direction of ship.
        Args:
            ship_obj: used to get ship length
        '''
        start_coord = input('\nwhich coordinate would you like to place your {} '
                            '(example A1, D5, or J9)? '.format(ship_obj.getName()))
        direction = input('\nwould you like to place your ship vertically (down)'
                          ' or horizontally (to the right) of your initial coordinate?'
                          ' [v/h] ')
        input_coordinates = cls(start_coord, direction, ship_obj.getLength())
        ship_coords = input_coordinates.check_input(ship_obj)
        if len(ship_coords) > 0: # check length of ship coordinates
            return ship_coords
        else:
            return cls.get_user_input(ship_obj)


class AttackInputCoordinate(InputCoordinate):
    '''Class used to process attack input coordinates.
    Child of InputCoordinate
    '''

    def __init__(self, input_coord):
        '''Initializes AttackInputCoordinate.
        Stores input_coord
        '''
        super().__init__(input_coord)

    @classmethod
    def get_user_input(cls):
        '''Get user input for attack coordinates.
        Returns:
            attack_coord.trans_coord: transformed attack coordinates if attack
                                      coordinates are valid
            cls.get_user_input(): circles back to getting user input after error
                                  message was displayed
        '''
        input_coord = input('Provide the coordinate you would like to attack: ')
        attack_coord = cls(input_coord)
        attack_coord.check_coord()

        if len(attack_coord.trans_coord) == 2:
            return attack_coord.trans_coord
        else:
            print('\nTry again with valid attack coordinates')
            return cls.get_user_input()
