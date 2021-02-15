#from battleship_game import play_game
from itertools import chain


class battlefield:
    def __init__(self):
        self.grid = [[0] * 10 for _ in range(10)]

    def set_grid_space(self, row, col, val):
        self.grid[row][col] = val

    def place_on_board(self, ship):
        for coord in ship.coordinates:
            row = coord[0]
            col = coord[1]
            if self.grid[row][col] == 0:
                self.set_grid_space(row, col, ship.getName())
            else:
                return False
        return True

    def result_of_hit(self, ship_name):
        # board is all zeros
        print(self.grid)
        # this only works if there is only one of each ship
        # it checks that there are no other grid spots with the ship name in it
        if ship_name in chain(*self.grid):
            outcome = 'You have hit your opponenets {}'.format(ship_name)
        else:
            if all(row == [0]*10 for row in self.grid):
                # if all rows are empty then you've sunk all the ships
                outcome = 'You have sunk your opponents last ship, YOU WIN!'
            else:
                outcome = 'You have sunk your opponents {}'.format(ship_name)
        return outcome

    def attack(self, attack_coord):
        row = attack_coord[0]
        col = attack_coord[1]
        val = self.grid[row][col]
        if self.grid[row][col] == 0:
            outcome = 'MISS'
        else:
            self.set_grid_space(row, col, 0)
            outcome = self.result_of_hit(val)
        return outcome

