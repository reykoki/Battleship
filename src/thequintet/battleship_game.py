


from battlefeild import battlefield

class battleship_game:

    def __init__(self):
        self.ships = {'Minesweeper': {'length': 2, 'coordinates': [], 'status': []},
                      'Destroyer': {'length': 3, 'coordinates': [], 'status': []},
                      'Battleship': {'length': 4, 'coordinates': [], 'status': []},
                      }


    def get_coordinates(self):
        for shipname in self.ships.keys():
            good_input = False
            while good_input is False:
                start_coord  = input('which coordinate would you like to place your {}?'.format(shipname))
                direction = input('would you like to place your ship vertically (down) or horizontally (to the right) of your initial coordinate? [v/h]')
                ship_coords = check_input(start_coord, direction, self.ships[shipname]['length'])
                if ship_coords > 0:
                    ship_coords = ships[shipname]['coordinates']
                    good_input = True
                else:
                    print('Try again!')

self.ships[shipname]['coordinates'][0]
