# TODO: test LUT size

# TODO: test Ship LUT size
# if you give it a ship of len 3, vertical direction give a 8x10 grid.. etc
import sys
sys.path.append('../src/thequintet')
from LUT import LUT


def test_Attack_LUT_size():

    # the default is 10x10 board
    assert len(LUT.get_Attack_LUT()) == 100

    # even if row/col are not equal, you get the correct length of legal inputs
    for row in range(5,8):
        for col in range(5,8):
            assert len(LUT.get_Attack_LUT(row, col)) == row * col

def test_Ship_LUT():

    for shiplength in range(2,8)

        (LUT.get_Ship_LUT('v', shiplength)) ==
        (LUT.get_Ship_LUT('v', shiplength)) ==
test_Attack_LUT_size()

