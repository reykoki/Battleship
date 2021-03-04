from Ship import *
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

    def __init__(self, ships = ['Minesweeper', 'Destroyer', 'Battleship']):
        '''Initializes game class.
        Initialized list of ships to start game. Each player gets one Minesweeper,
        one Destroyer and one Battleship
        Initializes player 1 and player 2's battlefields
        Initializes player2 as AI bot
        '''
        self.ships = ships
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
        #self.p2bf.sonar_unlocked = True
        attack_coord, activated = AttackInputCoordinate.get_user_input(self.p2bf.sonar_unlocked)
        if activated:
            if self.p2bf.sonar_remaining <= 0:
                print("No more sonars remaining")
                return self.player1_move()
            else:
                self.p2bf.sonar_activated(attack_coord)
                return
        else:
            outcome = self.p2bf.attack(attack_coord)
            return outcome

    def player2_move(self):
        '''Processes player 2's moves.
        Randomly chooses player2's attack coordinates
        Gives attack coordinates to player1's battlefield for attack results
        Returns:
            False: if player2 won the game
            True: if game should continue
        '''
        attack_coord = self.p2.get_attack_coord()
        outcome = self.p1bf.attack(attack_coord, True)
        return outcome

    def check_outcome(self, outcome):
        print('\n', outcome, '\n')
        if 'last ship' in outcome:
            return False
        else:
            return True

    def play_game(self):
        '''Main game loop'''
        play = True
        while play:
            outcome_p1 = self.player1_move()
            if outcome_p1 is not None:#sonar
                play = self.check_outcome(outcome_p1)
            outcome_p2 = self.player2_move()
            play = self.check_outcome(outcome_p2)
            self.p2bf.printBoardForOpponent()
            self.p1bf.printYourBoard()


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
        ship_coords = InitialInputCoordinate.get_user_input(ship_obj)
        if not self.p1bf.place_on_board(ship_coords, ship_obj.getName(), True):
            print('\nthe space you chose to put your {} is already occupied, '
                  'choose another'.format(ship_obj.getName()))
            self.SetUpShips(ship_obj)

    def SetUpBoard(self):
        '''Sets up game board for player1 and player2.
        Sets up ships for player1 using input and randomly for player2
        Calls main game loop after setup
        '''
        for shipname in self.ships:
            ship_obj = eval(shipname+'()')
            self.SetUpShips(ship_obj)
            self.AI_SetUpShips(ship_obj)

        self.play_game()
