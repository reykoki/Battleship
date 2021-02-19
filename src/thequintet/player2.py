import random
from LUT import LUT


class player2:
    def __init__(self):
        self.attack_LUT = LUT.get_Attack_LUT()

    # make sure the computer does not attack the same spot more than once
    def remove_attack_coord(self, attack):
        #removed = filter(lambda x: x != attack, self.attack_LUT)
        #self.attack_LUT = removed
        self.attack_LUT = [x for x in self.attack_LUT if x != attack]

    def get_attack_coord(self):
        attack_coord = random.choice(self.attack_LUT)
        self.remove_attack_coord(attack_coord)
        return attack_coord

    def place_ship(self, ship_obj):
        direction = random.choice(['v', 'h'])
        if direction == 'h':
            init_coord = random.choice(ship_obj.getHorizontalLUT())
            coords = []
            for idx in range(ship_obj.getLength()):
                next_coord = (init_coord[0], init_coord[1] + idx)
                coords.append(next_coord)
        else:
            init_coord = random.choice(ship_obj.getVerticalLUT())
            coords = []
            for idx in range(ship_obj.getLength()):
                next_coord = (init_coord[0] + idx, init_coord[1])
                coords.append(next_coord)

        return(coords, ship_obj.getName())

