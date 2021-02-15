

from Ship import Battleship
from battlefield import battlefield
from UserInput import InitialInputCoordinate
from UserInput import AttackInputCoordinate


class game:

    def __init__(self):
        self.ships = {'Minesweeper': Battleship('Minesweeper', 2),
                      'Destroyer': Battleship('Destroyer', 3),
                      'Battleship': Battleship()}
        self.battlefield = battlefield()

    def end_game(self):
        pass

    def play_game(self):
        attack_coord = AttackInputCoordinate.get_user_input()
        outcome = battlefield.attack(attack_coord)
        print(outcome)
        if 'YOU WIN' in outcome:
            end_game()

    # TODO: Put this all in the user input object
    def get_user_input(ship_obj):
        start_coord = input('\nwhich coordinate would you like to place your {}? '.format(ship_obj.getName()))
        direction = input('\nwould you like to place your ship vertically (down) or horizontally (to the right) of your initial coordinate? [v/h] ')
        input_coord = InitialInputCoordinate(start_coord, direction, ship_obj.getLength())
        ship_coords = input_coord.check_input()
        if len(ship_coords) > 0:
            ship_obj.setCoordinates(ship_coords)
        else:
            print('BAD USER INPUT: Try again!')
            game.get_user_input(ship_obj)

    def SetUpShips(self, ship_obj):
        InitialInputCoordinate.get_user_input(ship_obj)
        if not self.battlefield.place_on_board(ship_obj):
            print('\nthe space you chose to put your {} is already occupied, choose another'.format(ship_obj.getName()))
            game.SetUpShips(self, ship_obj)

    def SetUpBoard(self):
        for shipname in self.ships.keys():
            ship_obj = self.ships[shipname]
            game.SetUpShips(self, ship_obj)
        game.play_game(self)

