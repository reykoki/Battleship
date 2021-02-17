

from Ship import Battleship
from battlefield import battlefield
from UserInput import InputCoordinate
from UserInput import InitialInputCoordinate
from UserInput import AttackInputCoordinate


class game:

    #TODO: add 2nd player
    #TODO: add visual for players/opponents board
    #TODO: parallelize board set up so player 2 doesnt need to wait for player 1 to finish

    def __init__(self):
        self.ships = {'Minesweeper': Battleship('Minesweeper', 2),
                      'Destroyer': Battleship('Destroyer', 3),
                      'Battleship': Battleship()}
        # player 1
        self.p1bf = battlefield()
        # player 2
        self.p2bf = battlefield()

    def end_game(self):
        pass

    def play_game(self):
        attack_coord = AttackInputCoordinate.get_user_input()
        outcome = self.p1bf.attack(attack_coord)
        print(outcome)
        if 'YOU WIN' in outcome:
            self.end_game()
        else:
            self.play_game()

    def SetUpShips(self, ship_obj):
        InitialInputCoordinate.get_user_input(ship_obj)
        if not self.p1bf.place_on_board(ship_obj.coordinates, ship_obj.getName()):
            print('\nthe space you chose to put your {} is already occupied, choose another'.format(ship_obj.getName()))
            game.SetUpShips(self, ship_obj)

    def SetUpBoard(self):
        for shipname in self.ships.keys():
            ship_obj = self.ships[shipname]
            game.SetUpShips(self, ship_obj)
        game.play_game(self)

