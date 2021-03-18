import random
from LUT import LUT
from grid import grid
from attack import *
from UserInput import *
from Ship import *

class player:
    def __init__(self, ships):
        self.ships = self.addShips(ships)
        self.board = grid()
        self.sonarUnlocked = False
        self.laserUnlocked = False
        self.sonarRemaining = 2
        self.numShipsSunk = 0

    @staticmethod
    def addShips(ships):
        fleet = []
        for s in ships:
            fleet.append(s)
        return fleet

    def setUpBoard(self):
        for s in self.ships:
            self.setUpShip(s)

    def setUpShip(self, ship_obj):
        '''Sets up ships for player1.
        Takes in player1 input for where should be placed
        Args:
            ship_obj: used to place ship on player1's game board
        '''
        ship_coords = self.getUserShipInput(ship_obj)
        print('Ship coords: ', ship_coords)
        if not self.board.placeOnBoard(ship_coords, ship_obj, True):
            print('\nthe space you chose to put your {} is already occupied, '
                  'choose another'.format(ship_obj.getName()))
            self.setUpShip(ship_obj)

    def getUserShipInput(self, ship_obj):
        '''Used to get user input such as starting coordinates and direction of ship.
        Args:
            ship_obj: used to get ship length
        Returns:
            ship_coords: returns ship coordinates if they were input
        '''
        start_coord = input('\nwhich coordinate would you like to place your {} '
                            '(example A1, D5, or J9)? '.format(ship_obj.getName()))
        direction = input('\nwould you like to place your ship vertically (down)'
                          ' or horizontally (to the right) of your initial coordinate?'
                          ' [v/h] ')
        trans_coord = self.board.checkCoord(start_coord)
        if len(trans_coord) == 2:
            ship_coords = ship_obj.checkDir(trans_coord, direction)
            if len(ship_coords) > 0:  # check length of ship coordinates
                return ship_coords
        else:
            return self.getUserShipInput(ship_obj)

    def getAttack(self):
        '''Get attack coordinates from user'''
        at = self.getUserAttackInput()
        print('attack coord', at.getCoords())
        return at

    def getUserAttackInput(self):
        '''Handles user input'''
        attack_type = input('Provide which type of attack you''d like to use ('
                            'enter ''c'' for coordinate attack, '
                            'enter ''s'' for sonar or enter ''l'' for the space laser): ')
        if attack_type == 'c':
            attack_input = input('Provide the coordinate for the attack: ')
            coord = self.board.checkCoord(attack_input)
            if len(coord) == 2:
                a = attack()
                at = a.createAttack('c', coord)
            else:
                print('\nTry again with valid attack coordinates')
                return self.getUserAttackInput()
            return at
        elif attack_type == 's' or attack_type == 'S':
            if self.sonarUnlocked:
                sonar_attack = input('Provide the coordinate for the sonar attack: ')
                coord = self.board.checkCoord(sonar_attack)
                if len(coord) == 2:
                    a = attack()
                    at = a.createAttack('s', coord)
                    self.sonarRemaining -= 1
                    return at
                else:
                    print('\nTry again with valid attack coordinates')
                    return self.getUserAttackInput()
            else:
                print('You must sink a ship before unlocking sonar. \n')
                return self.getUserAttackInput()
        elif attack_type == 'l' or attack_type == 'L':
            if self.numShipsSunk > 0:
                laser_attack = input('Provide the coordinate for the laser attack: ')
                coord = self.board.checkCoord(laser_attack)
                if len(coord) == 2:
                    a = attack()
                    at = a.createAttack('l', coord)
                    return at
                else:
                    print('\nTry again with valid attack coordinates')
                    return self.getUserAttackInput()
            else:
                print('You must sink a ship before unlocking sonar. \n')
                return self.getUserAttackInput()
        else:
            print('Please enter valid option.')
            self.getUserAttackInput()

class notAIBot(player):
    def __init__(self, ships):
        '''Initializes bot class.
        Creates attack LUT for bot
        '''
        super().__init__(ships)
        self.attack_LUT = LUT.get_Attack_LUT()

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
            attack_coord: AI bot attack coordinate
        '''
        attack_coord = random.choice(self.attack_LUT)
        self.remove_attack_coord(attack_coord)
        a = attack()
        at = a.createAttack('c', attack_coord)
        return at

    # def setUpBoard(self):
    #     for s in self.ships:
    #         self.setUpShip(s)

    def setUpShip(self, ship_obj):
        coords = self.place_ship(ship_obj)
        if not self.board.placeOnBoard(coords, ship_obj, True):
            print('\nthe space you chose to put your {} is already occupied, '
                  'choose another'.format(ship_obj.getName()))
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
            init_coord = random.choice(ship_obj.getHorizontalLUT())
            coords = []
            for idx in range(ship_obj.getLength()):
                next_coord = (init_coord[0], chr(ord(init_coord[1]) + idx))
                coords.append(next_coord)
        else:
            init_coord = random.choice(ship_obj.getVerticalLUT())
            coords = []
            for idx in range(ship_obj.getLength()):
                next_coord = (str(int(init_coord[0]) + idx), init_coord[1])
                coords.append(next_coord)
        return coords
