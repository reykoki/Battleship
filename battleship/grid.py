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

        self.grid = self.create_grid()
        self.display = self.create_grid()
        self.shipinfo = {}
        self.shipinfo_history = []
        self.shipinfo_redo = []

    def create_grid(self):
        return pd.DataFrame('-', index=[str(i) for i in range(1, 11)],
                             columns=[chr(i) for i in range(ord('A'), ord('J') + 1)])

    def activate_subs(self):
        shipinfo_local = self.shipinfo.copy()
        for key in shipinfo_local.keys():
            if key.islower():
                coords = self.shipinfo.pop(key)
                self.shipinfo[key.upper()] = coords

    def redo_move(self):
        try:
            self.shipinfo = self.shipinfo_redo.pop()
            self.grid = self.create_grid()
        except:
            print('cannot redo board')

    def undo_move(self):
        try:
            self.shipinfo_redo.append(self.shipinfo)
            self.shipinfo = self.shipinfo_history.pop()
            self.grid = self.create_grid()
        except:
            self.shipinfo_redo.pop()
            print('cannot undo board: board is already at oldest known configuration')

    def get_rc_for_move(self, direction):
        row_diff = 0
        col_diff = 0
        if direction == 'N':
            row_diff = -1
        elif direction == 'S':
            row_diff = 1
        elif direction == 'W':
            col_diff = -1
        elif direction == 'E':
            col_diff = 1
        elif direction == 'R':
            self.redo_move()
        elif direction == 'U':
            self.undo_move()
        return row_diff, col_diff

    # coord format ('1', 'A')
    def onBoard(self, coord, print_error = False):
        if coord[0] in self.grid.index and coord[1] in self.grid.columns:
            return True
        elif print_error:
            print('Coordinate is not on the board, try again')
        return False

    def move_ships(self, direction):
        rd, cd = self.get_rc_for_move(direction)
        shipinfo_local = self.shipinfo.copy()
        if rd != 0 or cd != 0:
            self.shipinfo_history.append(self.shipinfo)
            self.grid = self.create_grid()
            self.shipinfo = {}
        for shipname, ship_coords in shipinfo_local.items():
            new_coords = []
            for coord in ship_coords:
                if isinstance(coord, tuple):
                    row = str(int(coord[0]) + rd)
                    col = chr(ord(coord[1]) + cd)
                    # check that new coords are on board and unoccupied
                    if not self.onBoard((row, col)) or not self.getGridSpace(row, col)=='-':
                        new_coords = ship_coords
                        break
                    new_coords.append((row, col))
            if len(new_coords) > 0:
                self.placeOnBoard(new_coords, shipname)


    def checkCoord(self, input_coord):
        '''Verifies coordinates are inside the game board.
        Converts input coordinates from game board coordinates to grid
        coordinates

        Returns:
            trans_coord: transformed coordinates if valid coordinate
            False: if invalid coordinate
        '''
        trans_coord = ()
        # convert letter to number with index 0
        try:
            col = input_coord[0].upper()
            row = input_coord[1:]
        except:
            return ()

        if col not in self.grid.columns:
            print('\nInvalid column choice: choose a letter A-J')
        elif row not in self.grid.index:
            print('\nInvalid row choice: choose a number 1-10')
        else:
            # transformed coord
            trans_coord = (row, col)
            print('trans coord', trans_coord)
            return trans_coord
        return ()

    def printBoard(self):
        '''Prints game board to the terminal.'''
        board = self.grid.apply(lambda x: x.str.slice(0, 1))
        for idx in board.index:
            for col in board.columns:
                if board[col][idx] == '-':
                    board[col][idx] = self.display[col][idx]
        print('\n ========= YOUR BOARD =========\n')
        print(board, '\n')
        print(self.shipinfo)

    def printBoardForOpponent(self):
        '''Print opponent board to the terminal.'''
        print('\n ======= OPPONENTS BOARD ======\n')
        board = self.display
        board = board.replace("\\?.*", "?", regex=True)
        for shipname in self.shipinfo.keys():
            board = board.replace(shipname, '-')
        print(board, '\n')

    def setGridSpace(self, row, col, val, update_display = True):
        '''Set grid space value.
        Args:
            row: row value
            col: column value
            val: value for (row,col) coordinate
        '''
        self.grid[col][row] = val
        if update_display:
            self.setDisplay(row, col, val)

    def setDisplay(self, row, col, val):
        self.display[col][row] = val[0]

    def getGridSpace(self, row, col):
        '''Get grid space value.
        Args:
            row: row value
            col: column value
        '''
        return self.grid[col][row]

    def notOccupied(self, coord, print_error=False):
        row = coord[0]
        col = coord[1]
        if self.grid[col][row] == '-':
            return True
        else:
            if print_error:
                print('The coordinates given overlap with your {}'.format(self.grid[col][row]))
            return False

    def placeOnBoard(self, ship_coords, shipname, print_board=False):
        '''Places ship on board given ship coordinates.
        Args:
            ship_coords: list of ship coordinates
            shipname: ship name for game board
            print_board: False by default
            submerged: if ship is submerged
        Returns:
            True: if the shp was successfully placed on the board
            False: if ship wasn't successfully placed on board
                   due to space already being occupied
        '''

        for coord in ship_coords:
            row = coord[0]
            col = coord[1]
            if self.notOccupied(coord):
                self.setGridSpace(row, col, shipname, False)
            else:
                return False

        self.shipinfo[shipname] = ship_coords

        if print_board:
            self.printBoard()
        return True

    def CQ_sink(self, shipname):
        coords = self.shipinfo.pop(shipname)
        for coord in coords:
            if isinstance(coord, tuple):
                self.setGridSpace(coord[0], coord[1], 'X')

    def result_of_hit(self, shipname):
        '''Finds result of hit.
        Board is all zeros
        This only works if there is only one of each ship
        It checks if there are any other grid spaces with that ship name
        Args:
            shipname: ship name
        Returns:
            outcome: string detailing results of hit
            outcome_p2: string detailing results of hit from player2 attack
        '''
        # search the board for other instances of the ship
        print('this should be true if there are any instances of the ship left: ')
        print(shipname in self.shipinfo.keys())
        if shipname in self.shipinfo.keys():
            outcome = 'You have hit one of your opponents ships!'
            outcome_p2 = 'Your opponent has hit your {}'.format(shipname)
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
                outcome = 'You have sunk your opponents {}'.format(shipname)
                outcome_p2 = 'Your opponent has sunk your {}'.format(shipname)
        return outcome, outcome_p2

    def coordinate_attack(self, attack_coord, p2_attack=False):
        # index of ship coordinate that was hit
        hit = None
        if len(attack_coord) == 2:
            row = attack_coord[0]
            col = attack_coord[1]
            val = self.grid[col][row]
            if '?' in val:
                val = val.split('?')[1]
            if val == '-' or val == '#' or val.islower():
                outcome = 'YOU MISSED'
                outcome_p2 = 'YOUR OPPONENT MISSED'
                self.setGridSpace(row, col, 'O')
            else:
                for key, value in self.shipinfo.items():
                    if (row, col) in value and key.isupper():
                        idx = value.index((row,col))
                        self.shipinfo[key][idx] = '-'
                        hit = [key.lower(), idx+1]
                self.setGridSpace(row, col, 'X')
                outcome, outcome_p2 = self.result_of_hit(val)
            if p2_attack:
                return [outcome_p2, hit]
            else:
                return [outcome, hit]

    def replace_val_sonar(self, row, col, val):
        if val == '-':
            self.setGridSpace(row, col, '#')
            print('empty grid space', self.getGridSpace(row, col))
        elif isinstance(val, list):
            self.setGridSpace(row, col, '?' + val)
            print('occupied grid space', self.getGridSpace(row, col))

    def sonar_attack(self, attack_coord):
        row = attack_coord[0]
        col = attack_coord[1]

        for r in range(-2, 3):
            new_col = chr(ord(col) + r)
            if new_col in self.grid:
                self.replace_val_sonar(row, new_col, self.grid[new_col][row])

        for c in range(-2, 3):
            new_row = str(int(row) + c)
            if new_row in self.grid[col]:
                self.replace_val_sonar(new_row, col, self.grid[col][new_row])

        for i in [-1, 1]:
            new_col = chr(ord(col) + i)
            for j in [-1, 1]:
                new_row = str(int(row) + j)
                if new_col in self.grid and new_row in self.grid[new_col]:
                    self.replace_val_sonar(new_row, new_col, self.grid[new_col][new_row])

