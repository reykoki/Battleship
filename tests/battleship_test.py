from Battleship import Battleship

# test that all ships have the appropriate number of coordinates
def ship_length(ship):
    name = ship.getName()
    length = len(ship.getCoordinates())

    if name == 'Minesweeper':
        assert length == 2
    elif name == 'Destroyer':
        assert length == 3
    elif name == 'Battleship':
        assert length == 4
    else:
        print(name, ' has a length of: ', length)





