import itertools
import random

from grid import grid
from attack import *
from ship import *


class player:
    '''Player object. Used to manipulate grid and handle user input.
    Attributes:
        ships: list of ships in fleet
        board: grid object, used for attack handling and display
        sonarRemaining: number of sonar attacks remaining
        validAttack: dictionary containing valid initial player options
    '''
    def __init__(self, ships):
        '''Initializes player object. Add ships to fleet, grid object
        and defines valid initial player move options.'''
        self.ships = self.addShips(ships)
        self.board = grid()
        self.sonarRemaining = 2
        self.validAttack = {'c': 'coordinate attack', 'm': 'move fleet'}

    @staticmethod
    def addShips(ships):
        '''Add ships to player fleet.
        Args:
            ships: list of ship object
        '''
        fleet = []
        for s in ships:
            fleet.append(s)
        return fleet

    # observer pattern
    def signalFirstHit(self):
        '''Handle first valid hit. Updates valid attack options to display.'''
        self.validAttack.pop('c')
        self.validAttack.update({'s': 'sonar attack'})
        self.validAttack.update({'l': 'laser attack'})
        print('You have activated your space laser! '
              'This will replace your bomb attacks and allow you to reach '
              'submerged submarines')
        self.board.activate_subs()

    def processResult(self, result):
        '''Process results of first valid hit. Can end game if game was won.
        Args:
            result: string denoting results of hit
        '''
        print(result)
        if 'sunk' in result and 'c' in self.validAttack:
            self.signalFirstHit()
        if 'last' in result:
            print('GAME OVER: you won!')
            exit()

    def setUpShip(self, ship_obj):
        '''Calls user input on ship placement and tries to places ships
        on game board.
        Args:
            ship_obj: used to place ship on player1's game board
        '''
        ship_coords = self.getUserShipInput(ship_obj)
        print('Ship coords: ', ship_coords)
        if not self.board.placeOnBoard(ship_coords, ship_obj.getName(), True):
            print('\nthe space you chose to put your {} is already occupied, '
                  'choose another'.format(ship_obj.getName()))
            self.setUpShip(ship_obj)

    def getUserShipInput(self, ship_obj):
        '''Used to get user input such as starting coordinates and direction of ship.
        Args:
            ship_obj: used to get ship length
        Returns:
            ship_coords: returns ship coordinates if they were valid
            Calls itself again if ship position chosen wasn't valid
        '''
        good_coords = True
        start_coord = input('\nwhich coordinate would you like to place your {} '
                            '(example A1, D5, or J9)? '.format(ship_obj.getName()))
        # turn 'A1' to ('1', 'A') -> (row, col)
        start_coord = (start_coord[1:], start_coord[0].upper())
        # if initial coordinate is on board, get direction
        if self.board.onBoard(start_coord, True):
            direction = input('\nwould you like to place your ship vertically (down)'
                              ' or horizontally (to the right) of your initial coordinate?'
                              ' [v/h] ')
            ship_coords = ship_obj.checkDir(start_coord, direction)
            for coord in ship_coords:
                if not self.board.onBoard(coord):
                    print('Portion of ship is off the board, choose another starting '
                          'coordinate')
                    good_coords = False
                    break
            if good_coords and len(ship_coords):
                return ship_coords
        return self.getUserShipInput(ship_obj)

    def getAttackCoordinate(self, attack_type):
        '''Handles getting coordinate for attack from user.
        Args:
            attack_type: type of attack
        '''
        input_coord = input('Provide the coordinate for your {}: '.format(attack_type))
        coord = self.board.checkCoord(input_coord)
        if len(coord) == 2:
            return coord
        else:
            print('\nTry again with valid attack coordinates')
            return self.getAttackCoordinate(attack_type)

    def getAttackType(self):
        '''Get attack type from user.'''
        print('Attack Options:')
        for key, value in self.validAttack.items():
            print('enter', key, 'for ', value)

        attack_type = input('\nProvide which type of attack you''d like to '
                            'use: ').lower()

        if attack_type == 's':
            if self.sonarRemaining > 1:
                self.sonarRemaining -= 1
            else:
                self.validAttack.pop(attack_type)

        if attack_type not in self.validAttack:
            print('Invalid input, try again')
            return self.getAttackType()
        return attack_type

    def moveFleet(self):
        '''Ask user to input which direction to move fleet in.
        Valid options defined in valid_dirs.
        Returns:
            call moveFleet() if input was not valid.
            direction: if valid input
        '''
        valid_dirs = ['N', 'S', 'W', 'E', 'U', 'R']
        direction = input('Please choose between N, S, W or E movement and '
                          'u/r for undo/redo: ').upper()
        if direction not in valid_dirs:
            return self.moveFleet()
        else:
            return direction

    def getAttack(self):
        '''Get attack object.
        Returns:
            at: attack object
        '''
        attack_type = self.getAttackType()
        if attack_type == 'm':
            coord = self.moveFleet()
        else:
            coord = self.getAttackCoordinate(self.validAttack[attack_type])
        a = attack()
        at = a.createAttack(attack_type[0], coord)
        return at


class notAIBot(player):
    '''Opponent class. Child of player class.
    Attributes:
        attack_LUT: LUT tables for attack
    '''
    def __init__(self, ships):
        '''Initializes bot class.
        Creates attack LUT for bot.
        '''
        super().__init__(ships)
        self.attack_LUT = self.create_attack_LUT()

    def create_attack_LUT(self):
        '''Create attack LUT. Called on initialization.
        Returns:
            LUT: look up tables
        '''
        num_rows = self.board.grid.shape[0]
        num_cols = self.board.grid.shape[1]
        possible_rows = [str(i) for i in range(1, num_rows+1)]
        possible_cols = [chr(i) for i in range(ord('A'), ord('Z')+1)][:num_cols]
        LUT = list(itertools.product(possible_rows, possible_cols))
        return LUT

    def remove_attack_coord(self, attack):
        '''Ensures bot doesn't attack same place twice.
        Args:
            attack: attack coordinate
        '''
        self.attack_LUT = [x for x in self.attack_LUT if x != attack]

    def get_attack(self):
        '''Gets random attack coordinate from attack LUT.
        Calls remove_attack_coord to verify attack coordinate hasn't already
        been used
        Returns:
            at: attack type. Bot can only use coordinate attack type.
        '''
        attack_coord = random.choice(self.attack_LUT)
        self.remove_attack_coord(attack_coord)
        a = attack()
        at = a.createAttack('c', attack_coord)
        return at

    def setUpShip(self, ship_obj):
        '''Try to place ship on board. If position not valid, call
        function again with same ship object.'''
        coords = self.place_ship(ship_obj)
        if not self.board.placeOnBoard(coords, ship_obj.getName(), True):
            self.setUpShip(ship_obj)

    def place_ship(self, ship_obj):
        '''Randomly chooses ship orientation and creates coordinates.
        Args:
            ship_obj: used to create correct number of coordinates
        Returns:
            coords: ship coordinates
            ship_obj.getName(): ship type
        '''
        direction = random.choice(['v', 'h'])
        if direction == 'h':
            init_coord = random.choice(self.attack_LUT)
            coords = []
            for idx in range(ship_obj.getLength()):
                next_coord = (init_coord[0], chr(ord(init_coord[1]) + idx))
                coords.append(next_coord)
        else:
            init_coord = random.choice(self.attack_LUT)
            coords = []
            for idx in range(ship_obj.getLength()):
                next_coord = (str(int(init_coord[0]) + idx), init_coord[1])
                coords.append(next_coord)
        for coord in coords:
            if not self.board.onBoard(coord) or not self.board.notOccupied(coord):
                return self.place_ship(ship_obj)
        return coords
