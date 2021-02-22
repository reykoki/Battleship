from Ship import Battleship
from battlefield import battlefield
from UserInput import InputCoordinate
from UserInput import InitialInputCoordinate
from UserInput import AttackInputCoordinate
from player2 import player2


class game:
    '''Game object used to play game. Runs main game loop.
    Attributes:
        ships: list of ships used in game
        p1bf: player1's battlefield
        p2bf: player2's battlefield
        p2: player2 class for AI bot
    '''

    def __init__(self):
        '''Initializes game class.
        Initialized list of ships to start game. Each player gets one Minesweeper,
        one Destroyer and one Battleship
        Initializes player 1 and player 2's battlefields
        Initializes player2 as AI bot
        '''
        self.ships = {'Minesweeper': Battleship('Minesweeper', 2)}
        #self.ships = {'Minesweeper': Battleship('Minesweeper', 2),
        #              'Destroyer': Battleship('Destroyer', 3),
        #              'Battleship': Battleship()}
        # player 1
        self.p1bf = battlefield()
        # player 2
        self.p2bf = battlefield()
        self.p2 = player2()

    def player1_move(self):
        '''Processes player 1's moves.
        Calls AttackInputCoordinate to receive player1's desired attack coordinates
        Gives attack coordinates to player2's battlefield for attack results
        Returns:
            False: if player1 won the game
            True: if game should continue
        '''
        attack_coord = AttackInputCoordinate.get_user_input()
        outcome = self.p2bf.attack(attack_coord)
        self.p1bf.modifyBoardAttacks(attack_coord, outcome)
        print(outcome)
        if 'YOU WIN' in outcome:
            return False
        return True

    def player2_move(self):
        '''Processes player 2's moves.
        Randomly chooses player2's attack coordinates
        Gives attack coordinates to player1's battlefield for attack results
        Returns:
            False: if player2 won the game
            True: if game should continue
        '''
        attack_coord = self.p2.get_attack_coord()
        outcome = self.p1bf.attack(attack_coord)
        self.p2bf.modifyBoardAttacks(attack_coord, outcome)
        if 'YOU WIN' in outcome:
            print('ALL YOUR SHIPS ARE SUNK, you lose')
            return False
        return True

    def play_game(self):
        '''Main game loop'''
        play = True
        while play:
            play = self.player1_move()
            play = self.player2_move()

    def AI_SetUpShips(self, ship_obj):
        '''Set up AI bot ships on player2's game board.
        Args:
            ship_obj: used to place ship on player2's game board
        '''
        coords, ship_name = self.p2.place_ship(ship_obj)
        if not self.p2bf.place_on_board(coords, ship_name):
            self.AI_SetUpShips(ship_obj)

    def SetUpShips(self, ship_obj):
        '''Sets up ships for player1.
        Takes in player1 input for where should be placed
        Args:
            ship_obj: used to place ship on player1's game board
        '''
        InitialInputCoordinate.get_user_input(ship_obj)
        if not self.p1bf.place_on_board(ship_obj.coordinates, ship_obj.getName()):
            print('\nthe space you chose to put your {} is already occupied, '
                  'choose another'.format(ship_obj.getName()))
            self.SetUpShips(ship_obj)
        else:
            self.p1bf.modifyBoardShips(ship_obj)
            self.p1bf.printBoard()

    def SetUpBoard(self):
        '''Sets up game board for player1 and player2.
        Sets up ships for player1 using input and randomly for player2
        Calls main game loop after setup
        '''
        self.p1bf.printBoard()
        for shipname in self.ships.keys():
            # print(self.ships[shipname].__dict__)
            ship_obj = self.ships[shipname]
            self.SetUpShips(ship_obj)
            self.AI_SetUpShips(ship_obj)

        self.play_game()
