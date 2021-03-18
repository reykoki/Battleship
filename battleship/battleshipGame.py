from Ship import *
from grid import grid
from UserInput import *
from player import *

class Game:
    '''Game object used to play game. Runs main game loop.
    Attributes:
        ships: list of ships used in game
        p1: player class initialized with ships
        p2: notAIBot class initialized with ships
    '''

    def __init__(self, ships):
        '''Initializes game class.
        Initializes player 1 and its board
        Initializes player2 as AI bot
        '''
        self.ships = ships
        self.p1 = player(ships)
        self.p2 = notAIBot(ships)
        for s in ships:
            self.p1.setUpShip(s)
            self.p2.setUpShip(s)

    @staticmethod
    def check_outcome(outcome):
        '''Prints outcome.
        Args:
            outcome: string
        '''
        print('\n', outcome, '\n')
        if 'last ship' in outcome:
            print('GAME OVER')
            exit()
        else:
            print(outcome)

    def processP1Input(self, p1_attack):
        '''Process player1's returned values'''
        outcome = self.p2.board.attack(p1_attack)
        if "You have sunk" in outcome:
            self.p1.sonarUnlocked = True
        return outcome

    def play_game(self):
        '''Main game loop'''
        play = True
        while play:
            p1_attack = self.p1.getAttack()
            outcome_p1 = self.processP1Input(p1_attack)
            print('outcome p1', outcome_p1)
            if outcome_p1 is not None:  # sonar
                self.check_outcome(outcome_p1)
            p2_attack = self.p2.get_attack()
            outcome_p2 = self.p1.board.attack(p2_attack, True)
            self.check_outcome(outcome_p2)
            self.p1.board.printBoardForOpponent()
            self.p1.board.printBoard()
            self.play_game()
