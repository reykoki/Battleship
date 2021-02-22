from itertools import chain


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
        self.grid = [[0] * 10 for _ in range(10)]
        self.game_board = []
        self.board_size = 10
        self.number_coordinates = ['1','2','3','4','5','6','7','8','9','10']
        self.letter_coordinates = [' ','A','B','C','D','E','F','G','H','I','J']
        self.buildBoard()

    def set_grid_space(self, row, col, val):
        '''Set grid space value.
        Args:
            row: row value
            col: column value
            val: value for (row,col) coordinate
        '''
        self.grid[row][col] = val

    def place_on_board(self, ship_coords, ship_name):
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
            if self.grid[row][col] == 0:
                self.set_grid_space(row, col, ship_name)
            else:
                return False
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
        if ship_name in chain(*self.grid):
            outcome = 'You have hit your opponents {}'.format(ship_name)
        else:
            if all(row == [0]*10 for row in self.grid):
                # if all rows are empty then you've sunk all the ships
                outcome = 'You have sunk your opponents last ship, YOU WIN!'
            else:
                outcome = 'You have sunk your opponents {}'.format(ship_name)
        return outcome

    def attack(self, attack_coord):
        '''Finds result of attack.
        Args:
            attack_coord: attack coordinate in grid coordinates
        Returns:
            outcome: string detailing results of attack
        '''
        row = attack_coord[0]
        col = attack_coord[1]
        val = self.grid[row][col]
        if self.grid[row][col] == 0:
            outcome = 'MISS'
        else:
            self.set_grid_space(row, col, 0)
            outcome = self.result_of_hit(val)
        # update visualization
        #self.modifyBoardAttacks(attack_coord, outcome)
        return outcome

    def buildBoard(self):
        '''Builds game board for display to players.
        Initializes board with '-' character denoting empty space on game board
        '''
        self.game_board.append(self.letter_coordinates)

        for number in self.number_coordinates:
            row = []
            row.append(number)
            row.extend(['-'] * self.board_size)
            self.game_board.append(row)

    def printBoard(self):
        '''Prints game board to the terminal.'''
        print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                         for row in self.game_board]))

    def modifyBoardAttacks(self, attack_coord, outcome):
        '''Modifies game board given success of attack.
        If miss then attack is labeled as 'O'
        If good then attack labeled as 'X'
        Prints board after attack
        Args:
            attack_coord: attack coordinates in terms of game board coordinates
            outcome: string detailing result of attack
        '''
        row_coord = attack_coord[0]
        col_coord = attack_coord[1]

        if outcome == 'MISS':
            self.game_board[row_coord+1][col_coord+1] = 'O'
        else:
            self.game_board[row_coord+1][col_coord+1] = 'X'
        self.printBoard()

    def modifyBoardShips(self, ship_obj):
        '''Adds '&' character to denote a ship is occupying that space.
        Args:
            ship_obj: ship object. Needed for coordinates
        '''
        for coordinate in ship_obj.coordinates:
            row_coord = coordinate[0]
            col_coord = coordinate[1]
            self.game_board[row_coord+1][col_coord+1] = '&'
