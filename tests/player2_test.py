import sys
sys.path.append('../src/thequintet')
from player2 import player2

p2 = player2()

def test_attack_coord():
    # when player2 chooses an attack coordinate, that coordinate is removed from the LUT
    orig_len = len(p2.attack_LUT)
    coord = p2.get_attack_coord()
    red_len = len(p2.attack_LUT)

    # make sure the used attack coordinate is not in the LUT
    assert coord not in p2.attack_LUT
    # make sure it is removed without leaving any artifacts
    assert orig_len == red_len + 1

test_attack_coord()
