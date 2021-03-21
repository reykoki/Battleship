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
        Initializes player2 as bot opponent
        Sets up ships for player and bot classes.
        '''
        self.ships = ships
        self.p1 = player(ships)
        self.p2 = notAIBot(ships)
        for idx, s in enumerate(ships):
            self.p1.setUpShip(s)
            self.p2.setUpShip(s)

    def checkCaptiansQuarters(self, outcome, opponent):
        '''Check whether captain's quarters were hit.
        Args:
            outcome: outcome of hit
            opponent: opponent object (player or notAIBot)
        Returns:
            outcome: return outcome of captain's quarters hit.
        '''
        result = outcome[0]
        idx = outcome[1][1]
        print(outcome)
        for ship in opponent.ships:
            if ship.getName().lower() == outcome[1][0].lower():
                if ship.checkCQ(idx):
                    opponent.board.CQ_sink(ship.getName().upper())
                    outcome[0] += ' The {}''s captains quarters were destroyed, ' \
                                  'this hit resulted in the ship being sunk'\
                                  .format(ship.getName().lower())
        print(outcome)
        return outcome

    def play_game(self):
        '''Main game loop. Gets and handles player 1 and bot attacks. '''
        p1_attack = self.p1.getAttack()
        if p1_attack.getName() == 'l' or p1_attack.getName() == 'c':
            outcome_p1 = self.p2.board.coordinate_attack(p1_attack.getCoords())
            if 'hit' in outcome_p1[0]:
                outcome_p1 = self.checkCaptiansQuarters(outcome_p1, self.p2)
            self.p1.processResult(outcome_p1[0])
        if p1_attack.getName() == 's':
            self.p2.board.sonar_attack(p1_attack.getCoords())
        if p1_attack.getName() == 'm':
            self.p1.board.move_ships(p1_attack.direction)

        p2_attack = self.p2.get_attack()
        outcome_p2 = self.p1.board.coordinate_attack(p2_attack.getCoords(), True)
        if 'hit' in outcome_p2[0]:
            outcome_p2 = self.checkCaptiansQuarters(outcome_p2, self.p1)
        self.p2.processResult(outcome_p2[0])
        self.p1.board.printBoard()
        self.p2.board.printBoardForOpponent()
        self.play_game()
