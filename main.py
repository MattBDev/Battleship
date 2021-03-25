# 2021.03.16
# Mit Bailey
# Copyright (c) 2021

"""
This is the main.py file of the Artificial Intelligence for Battleship using Genetic Programming.

How does it work?
The AI begins with a finite population of programs. These programs then play Battleship, with the highest
performing programs being selected to produce the subsequent generation of programs. The next generation
replaces the old programs that were not selected. This continues until performance plateaus.

The board will be represented by a list of lists of Tiles. List X will contain 10 lists which in turn each
contain a Tile. Note that the entire game consists of two boards (one for each player).

  0 1 2 3 4 5 6 7 8 9
  x x x x x x x x x x
0 y y y y y y y y y y
1 y y y y y y y y y y
2 y y y y y y y y y y
3 y y y y y y y y y y
4 y y y y y y y y y y
5 y y y y y y y y y y
6 y y y y y y y y y y
7 y y y y y y y y y y
8 y y y y y y y y y y
9 y y y y y y y y y y

"""

# Imports
import GameBoard


# TEMPORARY CLASS DEFINITIONS (these should be moved to the relevant .py files)


# The Ship class is used to generate one of each type of Battleship ship.
# onTiles: References to the Tile objects on top of which this ship resides.
class Ship:
    onTiles = []


def main():
    print("Hello, world!")

    # Example of how to create an instance of a class type and access a tile.
    myBoard = GameBoard.Board()
    myBoard.print_board()


# This snippet of code calls main(). Without this, main() will not run.
# The if statement is true only when run as a program.
if __name__ == "__main__":
    main()
