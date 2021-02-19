# TODO: test LUT size

# TODO: test Ship LUT size
# if you give it a ship of len 3, vertical direction give a 8x10 grid.. etc
import sys
sys.path.append('../src/thequintet')
from LUT import LUT
from LUT import Ship_LUT


def test_Attack_LUT_size():

    # the default is 10x10 board
    assert len(LUT.get_Attack_LUT()) == 100

    # even if row/col are not equal, you get the correct length of legal inputs
    for row in range(5,8):
        for col in range(5,8):
            assert len(LUT.get_Attack_LUT(row, col)) == row * col

def test_Ship_LUT():

    for shiplength in range(2,8):
        # number of board positions that are allowed for a ship of length 'shiplength'
        num_legal_pos = (10 - shiplength + 1) * 10
        assert len(Ship_LUT.get_Ship_LUT('v', shiplength)) == num_legal_pos
        assert len(Ship_LUT.get_Ship_LUT('h', shiplength)) == num_legal_pos

test_Attack_LUT_size()
test_Ship_LUT()

