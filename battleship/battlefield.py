from itertools import chain
import numpy as np
import pandas as pd

class battlefield:
    '''Battlefield object. Used to manipulate grid and game board.
    Attributes:
        grid: Keeps track of attacks
        game_board: Displayed to the players
        board_size: Default game board size
        number_coordinates: Game board row labels
        letter_coordinates: Game board column labels
    '''

    def __init__(self):
        '''Initializes battlefield object. Creates grid, game_board, sets
        board size, row and column coordinates and creates game_board to
        display to the players.
        '''
        self.grid = pd.DataFrame('-', index=[str(i) for i in range(1, 11)], columns=[chr(i) for i in range(ord('A'),ord('J')+1)])
        self.shipnames = []

    def printBoardForOpponent(self):
        print('\n ======= OPPONENTS BOARD ======\n')
        board = self.grid
        for shipname in self.shipnames:
            board = board.replace(shipname, '-')
        print(board, '\n')

    def printYourBoard(self):
        '''Prints game board to the terminal.'''
        print('\n ========= YOUR BOARD =========\n')
        board = self.grid.apply(lambda x: x.str.slice(0,1))
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
                if ship_name not in self.shipnames:
                    self.shipnames.append(ship_name)
            else:
                return False
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
        '''
        if ((self.grid==ship_name).any()==True).any():
            # TODO: decide if you should be able to see which ship you hit
            outcome = 'You have hit one of your opponents ships!'
            outcome_p2 = 'Your opponent has his your {}'.format(ship_name)
        else:
            if max(np.vectorize(len)(self.grid.values.astype(str)).max(axis=0)) == 1:
                # if all rows are empty then you've sunk all the ships
                outcome = 'You have sunk your opponents last ship, YOU WIN!'
                outcome_p2 = 'Your opponent has sunk your last ship, YOU LOSE'
            else:
                outcome = 'You have sunk your opponents {}'.format(ship_name)
                outcome_p2 = 'Your opponent has sunk your {}'.format(ship_name)
        return outcome, outcome_p2

    def attack(self, attack_coord, p2_attack=False):
        '''Finds result of attack.
        Args:
            attack_coord: attack coordinate in grid coordinates
        Returns:
            outcome: string detailing results of attack
        '''
        row = attack_coord[0]
        col = attack_coord[1]
        val = self.grid[col][row]
        if self.grid[col][row] == '-':
            outcome = 'YOU MISSED'
            outcome_p2 = 'YOUR OPPONENT MISSED'
            self.grid[col][row] = 'O'
        elif self.grid[col][row] in self.shipnames:
            self.set_grid_space(row, col, 'X')
            outcome, outcome_p2 = self.result_of_hit(val)
        elif self.grid[col][row] == 'O':
            outcome = 'THIS COORDINATE WAS ALREADY ATTACKED AND MISSED'
            outcome_p2 = ''
        else:
            outcome = 'YOU HAVE ALREADY ATTACKED AND HIT A SHIP AT THIS COORDINATE'
            outcome_p2 = ''
        if p2_attack:
            return outcome_p2
        else:
            return outcome

