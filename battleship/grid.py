import numpy as np
import pandas as pd

class grid:
    '''Grid object. Used to manipulate grid and game board.
    Attributes:

    '''

    def __init__(self):
        '''Initializes battlefield object. Creates grid, initializes empty ship
        names list, empty ship info dictionary, sonar status and sonar
        remaining uses left.
        '''
        self.grid = pd.DataFrame('-', index=[str(i) for i in range(1, 11)],
                                 columns=[chr(i) for i in range(ord('A'), ord('J') + 1)])
        self.shipinfo = {}
        self.CQ = {}

    def addCaptainsQuarters(self, ship_obj, ship_coords):
        '''Add string value to grid to represent captain's quarters
        and store captain's quarters.
        Args:
            ship_coords: coordinates of captain's quarters
        '''
        CQ_row = ship_coords[-2][0]
        CQ_col = ship_coords[-2][1]
        self.grid[CQ_col][CQ_row] = self.grid[CQ_col][CQ_row] + 'CQ' + str(len(ship_coords))
        self.CQ[(CQ_col, CQ_row)] = ship_coords

    def checkCoord(self, input_coord):
        '''Verifies coordinates are inside the game board.
        Converts input coordinates from game board coordinates to grid
        coordinates

        Returns:
            trans_coord: transformed coordinates if valid coordinate
            False: if invalid coordinate
        '''
        valid_cols = [chr(i) for i in range(ord('A'), ord('J') + 1)]
        valid_rows = [str(i) for i in range(1, 11)]
        trans_coord = ()
        good_coords = True
        # convert letter to number with index 0
        try:
            col = input_coord[0].upper()
            row = input_coord[1:]
        except:
            return

        if col not in valid_cols:
            print('\nInvalid column choice: choose a letter A-J')
            good_coords = False
        if row not in valid_rows:
            print('\nInvalid row choice: choose a number 1-10')
            good_coords = False
        if good_coords:
            # transformed return with index 0
            trans_coord = (row, col)
            print('trans coord', trans_coord)
            return trans_coord
        return good_coords

    def printBoard(self):
        '''Prints game board to the terminal.'''
        print('\n ========= YOUR BOARD =========\n')
        board = self.grid.apply(lambda x: x.str.slice(0, 1))
        print(board, '\n')

    def printBoardForOpponent(self):
        '''Print opponent board to the terminal.'''
        print('\n ======= OPPONENTS BOARD ======\n')
        board = self.grid
        board = board.replace("\\?.*", "?", regex=True)
        board = board.replace(".*CQ.*", "-", regex=True)
        for shipname in set(self.shipinfo.values()):
            board = board.replace(shipname, '-')
        print(board, '\n')

    def setGridSpace(self, row, col, val):
        '''Set grid space value.
        Args:
            row: row value
            col: column value
            val: value for (row,col) coordinate
        '''
        self.grid[col][row] = val

    def getGridSpace(self, row, col):
        '''Get grid space value.
        Args:
            row: row value
            col: column value
        '''
        return self.grid[col][row]

    def placeOnBoard(self, ship_coords, ship_obj, print_board=False):
        '''Places ship on board given ship coordinates.
        Args:
            ship_coords: list of ship coordinates
            ship_name: ship name for game board
            print_board: False by default
            submerged: if ship is submerged
        Returns:
            True: if the shp was successfully placed on the board
            False: if ship wasn't successfully placed on board
                   due to space already being occupied
        '''
        count = 0
        for coord in ship_coords:
            row = coord[0]
            col = coord[1]
            if self.grid[col][row] == '-':
                count += 1
            else:
                return False
        if count == ship_obj.getLength():
            for coord in ship_coords:
                print('Coord: ', coord)
                row = coord[0]
                col = coord[1]
                self.setGridSpace(row, col, ship_obj.getName())
                self.shipinfo[(row, col)] = ship_obj.getName()
        self.addCaptainsQuarters(ship_obj, ship_coords)
        if print_board:
            self.printBoard()
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
                print(self.printBoard())
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
                self.setGridSpace(row, col, 'X')
                self.shipinfo.pop((row, col), None)
            outcome, outcome_p2 = self.result_of_hit(val[:-3])
            outcome = 'You hit the captain quarters of your opponents ship. \n' + outcome
            outcome_p2 = 'Your opponent has hit your captains quarters.\n' + outcome_p2
        return outcome, outcome_p2

    def replace_val(self, row, col, val):
        if val == '-':
            self.setGridSpace(row, col, '#')
            print('empty grid space', self.getGridSpace(row, col))
        elif len(val) > 1:
            self.setGridSpace(row, col, '?' + val)
            print('occupied grid space', self.getGridSpace(row, col))

    def attack(self, attack, p2_attack=False):
        '''Finds result of attack.
        Args:
            attack_coord: attack coordinate in grid coordinates
            p2_attack: If true, get results for player 2 attack,
                       else get player 1 results.
        Returns:
            outcome: string detailing results of attack
        '''
        if attack.getName() == 'c':
            attack_coord = attack.getCoords()
            if len(attack_coord) == 2:
                print('attack coord', attack_coord)
                row = attack_coord[0]
                col = attack_coord[1]
                val = self.grid[col][row]
                if '?' in val:
                    val = val.split('?')[1]
                if val == '-' or val == '#':
                    outcome = 'YOU MISSED'
                    outcome_p2 = 'YOUR OPPONENT MISSED'
                    self.setGridSpace(row, col, 'O')
                elif 'CQ' in val:
                    outcome, outcome_p2 = self.CQ_hit(val, row, col)
                elif (row, col) in self.shipinfo.keys():
                    self.setGridSpace(row, col, 'X')
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
        elif attack.getName() == 's':
            attack_coord = attack.getCoords()
            print('sonar attack coord', attack_coord)
            row = attack_coord[0]
            col = attack_coord[1]

            for r in range(-2, 3):
                new_col = chr(ord(col) + r)
                print('new col', new_col)
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
            outcome = 'USED SONAR AT COORDINATE GIVEN'
            return outcome
