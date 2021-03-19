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
        self.sonarRemaining = 2
        self.validAttack = {'c': 'coordinate attack'}

    @staticmethod
    def addShips(ships):
        fleet = []
        for s in ships:
            fleet.append(s)
        return fleet

    def processResult(self, result):
        print(result)
        self.board.printBoard()
        if 'sunk' in result and 'c' in self.validAttack:
            self.validAttack.pop('c')
            self.validAttack.update({'s': 'sonar attack'})
            self.validAttack.update({'l': 'laser attack'})
            print('you have activated your space laser! This will replace your bomb attacks and allow you to reach submerged submarines')
        if 'last' in result:
            print('GAME OVER: you won!')
            exit()

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

    def getAttackCoordinate(self, attack_type):
        input_coord = input('Provide the coordinate for your {} attack: '.format(attack_type))
        coord = self.board.checkCoord(input_coord)
        if len(coord) == 2:
            a = attack()
            at = a.createAttack(attack_type[0], coord)
            return at
        else:
            print('\nTry again with valid attack coordinates')
            return self.getAttackCoordinate()

    def getAttack(self):
        '''Get attack coordinates from user'''
        if len(self.validAttack) > 1:
            print('Attack Options:')
            for key, value in self.validAttack.items():
                print('enter', key, 'for ', value)
            attack_type = input('\nProvide which type of attack you''d like to use: ').lower()
            if attack_type not in self.validAttack:
                print('Invalid input, try again')
                self.getAttackOption()
            attack= self.getAttackCoordinate(self.validAttack[attack_type])

            if attack_type == 's':
                if self.sonarRemaining > 1:
                    self.sonarRemaining -= 1
                else:
                    self.validAttack.pop(attack_type)
        else:
            attack_type = str(next(iter(self.validAttack)))
            attack = self.getAttackCoordinate(self.validAttack[attack_type])

        return attack

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

    def processResult(self, result):
        print(result)
        if 'last' in result:
            print('GAME OVER: you lose!')
            exit()
        self.board.printBoardForOpponent()

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
