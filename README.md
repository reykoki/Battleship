# Battleship Game
### CSCI-5448
#### Track 2

The Quintet: [Devin Burke](https://github.com/mrburke00), [Rey Koki](https://github.com/reykoki) and [Daniel Torres](https://github.com/danieltorres17)

The agreed upon coding standards are listed in this [style guide](https://google.github.io/styleguide/pyguide.html)

### Description

This repo includes:

- Documentation of our CRC cards that show our brainstorming for the object oriented design for our battlship game
    - located in ./docs/CRC_cards
- A group contract that lays expectations and commitments
    - located in ./docs/
- source code to play our Battleship Game 
    - located in ./src/thequintet/
To Play:


```
python main.py
```

- testing suite
    - located in ./tests/


```
cd tests
python -m unittest -v *
```

- .gitignore to exclude any superfluous files/directories
- requirements.txt to give the user a list of any necessary packages

```
pip install -r requirements.txt
```

## Code Coverage

Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
LUT_test.py                  14      0   100%
UserInput_test.py            28      0   100%
battlefield_test.py          43      0   100%
battleship_game_test.py      76      0   100%
battleship_test.py           18      0   100%
player2_test.py              16      0   100%
-------------------------------------------------------
TOTAL                       195      0   100%





