#from battleship_game import play_game
from itertools import chain


class battlefield:
    def __init__(self):
        self.grid = [[0] * 10 for _ in range(10)]

        self.game_board = []
        self.board_size = 10
        self.number_coordinates = ['1','2','3','4','5','6','7','8','9', '10']
        self.letter_coordinates = [' ','A','B','C','D','E','F','G','H','I','J']

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
        # it checks if there are any other gridspaces with that ship name
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

    def buildBoard(self):
        self.game_board.append(self.letter_coordinates)

        for number in self.number_coordinates:
            row = []
            row.append(number)
            row.extend(['-'] * self.board_size)
            self.game_board.append(row)

    def printBoard(self):
        print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                         for row in self.game_board]))

    def modifyBoard(self, ship_obj):
        for coordinate in ship_obj.coordinates:
            row_coor = coordinate[0]
            col_coor = coordinate[1]
            x = self.letter_coordinates[col_coor+1]
            y = self.number_coordinates[row_coor]
            self.game_board[row_coor+1][col_coor+1] = '&'
        print('-------------------------------------')

