import random
from UserInput import InitialInputCoordinate


class player2:
    def __init__(self):
        self.previous_attacks = []

    def random_idx():
        col = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        row = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        idx = random.choice(col) + random.choice(row)
        return idx

    def attacked_previously(self, attack):
        if attack in previous_attacks:
            return True
        else:
            self.previous_attacks.append(attack)
            return False

    @classmethod
    def get_attack_coord(self):
        attack_coord = self.random_idx()
        if player2.attacked_previously(self, attack_coord):
            player2.get_attack_coord()
        else:
            return attack_coord

    @classmethod
    def place_ship(self, ship_obj):
        coord = self.random_idx()
        direction = random.choice(['v', 'h'])
        ship_coords = InitialInputCoordinate.get_AI_input(ship_obj, coord, direction)
        print('hiiii')
        if len(ship_coords) == 0:
            player2.place_ship(ship_obj)
            print('yoooooo')
        else:
            print(ship_coords)
            return(ship_coords, ship_obj.getName())

        print(ship_coords)
