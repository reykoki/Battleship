import sys
import numpy as np
import os
import string
sys.path.append('../battleship')
from battlefield import battlefield
from Ship import Battleship

def buildSampleBoard():
    bf = battlefield()
    numbers = []
    for i in range(1,11):
        numbers.append(str(i))
    letters = []
    letters.extend(' ')
    letters.extend(map(chr, range(ord('A'), ord('J')+1)))
    game_board = []
    game_board.append(letters)
    for number in numbers:
            row = []
            row.append(number)
            row.extend(['-'] * 10)
            game_board.append(row)
    return game_board

# TODO: check size of grid
def test_GridSize():
    bf = battlefield()
    grid = np.array(bf.grid)
    assert (grid.shape[0]) == 10
    assert (grid.shape[1]) == 10
#TODO: check size of game board
def test_GameBoardSize():
    bf = battlefield()
    assert len(bf.number_coordinates) == 10
    assert len(bf.letter_coordinates) == 11
#TODO: check arrangement of game board
def test_GameBoardArrange():
    bf = battlefield()
    game_board = buildSampleBoard()
    assert (bf.game_board) == game_board

#TODO: check manipulation of game board
def test_GameBoardManipulation(board_miss):
    bf = battlefield()
    bf.modifyBoardAttacks((4,3), 'MISS')
    assert(bf.game_board) == board_miss

# TODO: check if ships are placed in correct coordinates
def test_CorrectShips(board_ship, ship_test):
    bf = battlefield()
    bf.modifyBoardShips(ship_test)
    assert (bf.game_board) == board_ship

#TODO: check that if a ship is hit, it is reported
def test_AttackShip(board_ship, ship_test):
    bf = battlefield()
    bf.modifyBoardShips(ship_test)
    outcome = bf.attack([0,0])
    assert (outcome) == 'MISS'

old_stdout = sys.stdout # backup current stdout
sys.stdout = open(os.devnull, "w")

board_miss = [[' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], ['1', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['2', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['3', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['4', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['5', '-', '-', '-', 'O', '-', '-', '-', '-', '-', '-'], ['6', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['7', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['8', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['9', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['10', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]
board_ship = [[' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], ['1', '&', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['2', '&', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['3', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['4', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['5', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['6', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['7', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['8', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['9', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['10', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]
ship_test = Battleship(length = 2, coordinates = [[0,0],[1,0]])
test_GridSize()
test_GameBoardSize()
test_GameBoardArrange()
test_GameBoardManipulation(board_miss)
test_CorrectShips(board_ship, ship_test)
test_AttackShip(board_ship, ship_test)

sys.stdout = old_stdout # reset old stdout
