from itertools import chain
import numpy as np
import pandas as pd

class battlefield:
    '''Battlefield object. Used to manipulate grid and game board.
    Attributes:
        grid: Keeps track of attacks
        shipinfo: dictionary to track important information regarding battleships
        CQ: dictionary to store captain's quarters coordinates
        sonar_unlocked: status of sonar
        sonar_remaining: gives number of sonar uses remaining
    '''

    def __init__(self):
        '''Initializes battlefield object. Creates grid, initializes empty ship
        names list, empty ship info dictionary, sonar status and sonar
        remaining uses left.
        '''
        self.grid = pd.DataFrame('-', index=[str(i) for i in range(1, 11)],
                                 columns=[chr(i) for i in range(ord('A'),ord('J')+1)])
        self.shipinfo = {}
        self.CQ = {}
        self.sonar_unlocked = False
        self.sonar_remaining = 2

    def addCaptainsQuarters(self, ship_coords):
        '''Add string value to grid to represent captain's quarters
        and store captain's quarters.
        Args:
            ship_coords: coordinates of captain's quarters
        '''
        CQ_row = ship_coords[-2][0]
        CQ_col = ship_coords[-2][1]
        self.grid[CQ_col][CQ_row] = self.grid[CQ_col][CQ_row] + 'CQ' + str(len(ship_coords))
        self.CQ[(CQ_col, CQ_row)] = ship_coords

    def printBoardForOpponent(self):
        '''Print opponent board to the terminal.'''
        print('\n ======= OPPONENTS BOARD ======\n')
        board = self.grid
        board = board.replace("\\?.*", "?", regex=True)
        board = board.replace(".*CQ.*", "-", regex=True)
        for shipname in set(self.shipinfo.values()):
            board = board.replace(shipname, '-')
        print(board, '\n')

    def printYourBoard(self):
        '''Prints game board to the terminal.'''
        print('\n ========= YOUR BOARD =========\n')
        board = self.grid.apply(lambda x: x.str.slice(0, 1))
        print(board, '\n')

    def set_grid_space(self, row, col, val):
        '''Set grid space value.
        Args:
            row: row value
            col: column value
            val: value for (row,col) coordinate
        '''
        self.grid[col][row] = val

    def place_on_board(self, ship_coords, ship_name, print_board=False):
        '''Places ship on board given ship coordinates.
        Args:
            ship_coords: list of ship coordinates
            ship_name: ship name for game board
            print_board: False by default
        Returns:
            True: if the shp was successfully placed on the board
            False: if ship wasn't successfully placed on board
                   due to space already being occupied
        '''
        for coord in ship_coords:
            row = coord[0]
            col = coord[1]
            if self.grid[col][row] == '-':
                self.set_grid_space(row, col, ship_name)
                self.shipinfo[(row, col)] = ship_name
            else:
                return False
        self.addCaptainsQuarters(ship_coords)
        if print_board:
            self.printYourBoard()
        return True

    def result_of_hit(self, ship_name):
        '''Finds result of hit.
        Board is all zeros
        This only works if there is only one of each ship
        It checks if there are any other grid spaces with that ship name
        Args:
            ship_name: ship name
        Returns:
            outcome: string detailing results of hit
            outcome_p2: string detailing results of hit from player2 attack
        '''
        # search the board for other instances of the ship
        print('this should be true if there are any instances of the ship left: ')
        print(ship_name in self.shipinfo.values())
        if ship_name in self.shipinfo.values():
            outcome = 'You have hit one of your opponents ships!'
            outcome_p2 = 'Your opponent has hit your {}'.format(ship_name)
        else:
            print('this should be 1 if there are no more ships on the board')
            print(max(np.vectorize(len)(self.grid.values.astype(str)).max(axis=0)))
            # if the max length of your grid values is 1, there are no more ships
            if max(np.vectorize(len)(self.grid.values.astype(str)).max(axis=0)) == 1:
                # if all rows are empty then you've sunk all the ships
                print(self.printYourBoard())
                outcome = 'You have sunk your opponents last ship, YOU WIN!'
                outcome_p2 = 'Your opponent has sunk your last ship, YOU LOSE'
            else:
                outcome = 'You have sunk your opponents {}'.format(ship_name)
                outcome_p2 = 'Your opponent has sunk your {}'.format(ship_name)
        return outcome, outcome_p2

    def CQ_hit(self, val, row, col):
        '''Outcome when captain's quarters are hit.
        Args:
            val: value to set coordinate to
            row: coordinate row
            col: coordinate column
        Returns:
            outcome: string denoting result of hitting captain's quarters
            outcome_p2: string denoting result of hitting captain's quarters
        '''
        if int(val[-1]) > 2:
            self.grid[col][row] = val[:-1] + '1'
            outcome = 'You have damaged a ships captains quarters'
            outcome_p2 = 'Your opponent has damaged your {} captains quarters'\
                         .format(val[:-3])
        else:
            for coord in self.CQ[(col, row)]:
                row = coord[0]
                col = coord[1]
                self.set_grid_space(row, col, 'X')
                self.shipinfo.pop((row, col), None)
            outcome, outcome_p2 = self.result_of_hit(val[:-3])
            outcome = 'You hit the captain quarters of your opponents ship. \n' + outcome
            outcome_p2 = 'Your opponent has hit your captains quarters.\n' + outcome_p2
        return outcome, outcome_p2

    def attack(self, attack_coord, p2_attack=False):
        print(self.shipinfo)
        '''Finds result of attack.
        Args:
            attack_coord: attack coordinate in grid coordinates
        Returns:
            outcome: string detailing results of attack
        '''
        print(attack_coord)
        row = attack_coord[0]
        col = attack_coord[1]
        val = self.grid[col][row]

        if '?' in val:
            val = val.split('?')[1]

        if val == '-' or val == '#':
            outcome = 'YOU MISSED'
            outcome_p2 = 'YOUR OPPONENT MISSED'
            self.set_grid_space(row, col, 'O')
        elif 'CQ' in val:
            outcome, outcome_p2 = self.CQ_hit(val, row, col)
        elif (row, col) in self.shipinfo.keys():
            self.set_grid_space(row, col, 'X')
            val = self.shipinfo[attack_coord]
            self.shipinfo.pop((row, col))
            outcome, outcome_p2 = self.result_of_hit(val)
        elif val == 'O':
            outcome = 'THIS COORDINATE WAS ALREADY ATTACKED AND MISSED'
            outcome_p2 = ''
        else:
            outcome = 'YOU HAVE ALREADY ATTACKED AND HIT A SHIP AT THIS COORDINATE'
            outcome_p2 = ''
        if p2_attack:
            return outcome_p2
        else:
            if "You have sunk" in outcome:
                self.sonar_unlocked = True
            return outcome


    def replace_val(self, row, col, val):
        if val == '-':
            self.set_grid_space(row, col, '#')
        elif len(val)>1:
            self.set_grid_space(row, col, '?' + val)

    def sonar_activated(self, attack_coord):
        '''Activates sonar.
        Args:
            attack_coord: attack coordinates for center of sonar
        '''

        self.sonar_remaining = self.sonar_remaining - 1
        row = attack_coord[0]
        col = attack_coord[1]
        for r in range(-2, 3):
            new_col = chr(ord(col) + r)
            if new_col in self.grid:
                self.replace_val(row, new_col, self.grid[new_col][row])

        for c in range(-2, 3):
            new_row = str(int(row) + c)
            if new_row in self.grid[col]:
                self.replace_val(new_row, col, self.grid[col][new_row])

        for i in [-1, 1]:
            new_col = chr(ord(col) + i)
            for j in [-1, 1]:
                new_row = str(int(row) + j)
                if new_col in self.grid and new_row in self.grid[new_col]:
                    self.replace_val(new_row, new_col, self.grid[new_col][new_row])
