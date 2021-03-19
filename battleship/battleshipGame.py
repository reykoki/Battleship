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

    def play_game(self):
        '''Main game loop'''

        p1_attack = self.p1.getAttack()
        outcome_p1 = self.p2.board.attack(p1_attack)
        if outcome_p1 is not None:  # sonar
            self.p1.processResult(outcome_p1)

        p2_attack = self.p2.get_attack()
        outcome_p2 = self.p1.board.attack(p2_attack, True)
        self.p2.processResult(outcome_p2)

        self.play_game()

