import random
from LUT import LUT


class player2:
    '''Player class for AI bot to use.
    Attributes:
        attack_LUT: player2's attack LUT
    '''

    def __init__(self):
        '''Initializes player 2 class.
        Creates attack LUT for bot
        '''
        self.attack_LUT = LUT.get_Attack_LUT()

    def remove_attack_coord(self, attack):
        '''Ensures bot doesn't attack same place twice.
        Args:
            attack: attack coordinate
        '''
        self.attack_LUT = [x for x in self.attack_LUT if x != attack]

    def get_attack_coord(self):
        '''Gets random attack coordinate from attack LUT.
        Calls remove_attack_coord to verify attack coordinate hasn't already
        been used
        Returns:
            attack_coord: AI bot attack coordinate
        '''
        attack_coord = random.choice(self.attack_LUT)
        self.remove_attack_coord(attack_coord)
        return attack_coord

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
        return coords, ship_obj.getName()

