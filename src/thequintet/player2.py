
class player2:
    def __init__(self):
        self.previous_attacks = []

    def random_idx():
        col = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        row = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        idx = random.choice(col) + random.choice(row)
        return idx


    def place_ship(self, ship_obj):
        coord = self.random_idx()
        direction = random.choice(['v', 'h'])
        ship_coords = InitialInputCoordinate.check_users_input(ship_obj, coord, direction)
        if len(ship_coords) == 0:
            self.initialize_board(ship_obj)
        else:
            return(ship_coords, ship_obj.getName())

    def attacked_previously(self, attack):
        if attack in previous_attacks:
            return True
        else:
            self.previous_attacks.append(attack)
            return False

    def get_attack_coord(self):
        attack_coord = self.random_idx()
        if self.attacked_previously(attack):
            self.attack()
        else:
            return attack_coord
