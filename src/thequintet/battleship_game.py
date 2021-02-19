

from Ship import Battleship
from battlefield import battlefield
from UserInput import InputCoordinate
from UserInput import InitialInputCoordinate
from UserInput import AttackInputCoordinate
from player2 import player2



class game:

    #TODO: add 2nd player
    #TODO: add visual for players/opponents board
    #TODO: parallelize board set up so player 2 doesnt need to wait for player 1 to finish

    def __init__(self):
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
        attack_coord = AttackInputCoordinate.get_user_input()
        outcome = self.p2bf.attack(attack_coord)
        print(outcome)
        if 'YOU WIN' in outcome:
            return False
        return True

    def player2_move(self):
        attack_coord = self.p2.get_attack_coord()
        outcome = self.p1bf.attack(attack_coord)
        if 'YOU WIN' in outcome:
            print('ALL YOUR SHIPS ARE SUNK, you lose')
            return False
        return True

    def play_game(self):
        play = True
        while play == True:
            play = self.player1_move()
            play = self.player2_move()


    def AI_SetUpShips(self, ship_obj):
        coords, ship_name = self.p2.place_ship(ship_obj)
        if not self.p2bf.place_on_board(coords, ship_name):
            self.AI_SetUpShips(ship_obj)


    def SetUpShips(self, ship_obj):
        InitialInputCoordinate.get_user_input(ship_obj)
        if not self.p1bf.place_on_board(ship_obj.coordinates, ship_obj.getName()):
            print('\nthe space you chose to put your {} is already occupied, choose another'.format(ship_obj.getName()))
            self.SetUpShips(ship_obj)
        else:
            self.p1bf.modifyBoardShips(ship_obj)
            self.p1bf.printBoard()

    def SetUpBoard(self):
        # self.p1bf.buildBoard()
        self.p1bf.printBoard()
        for shipname in self.ships.keys():
            # print(self.ships[shipname].__dict__)
            ship_obj = self.ships[shipname]
            self.SetUpShips(ship_obj)
            self.AI_SetUpShips(ship_obj)

        self.play_game()

