#!/usr/bin/env python

from Ship import Ship

def main():
    # testing:
    tugboat = Ship()
    tugboat.setName('Theodore')
    print(tugboat.getName())
    tugboat.show()

if __name__ == "__main__":
    main()
