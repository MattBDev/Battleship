# 2021.03.16
# Mit Bailey
# Copyright (c) 2021

'''
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

'''

# Imports
import init

# TEMPORARY CLASS DEFINITIONS (these should be moved to the relevant .py files)

# The Tile class composes the basic makeup of the Battleship board.
# shot: Has this tile been shot at?
# ship: Is a ship segment present?
class Tile:
    shot = False
    ship = False

# The Ship class is used to generate one of each type of Battleship ship.
# onTiles: References to the Tile objects on top of which this ship resides.
class Ship:
    onTiles = []

# The Board class contains the Ships and Tiles for one player.
# __init__(self): This default constructor initializes empty lists for ships and the
#                 grid before appending 10 empty lists and 10 Tiles to each new list.
# self.grid: Contains the game grid.
# self.ships: Contains references to all of this board's ships.
class Board:
    def __init__(self):
        self.grid = []
        self.ships = []

        i = 0
        while i < 10:
            ii = 0
            grid.append([])
            while ii < 10:
                grid[i].append(Tile)
                ii += 1
            i += 1

    
    

def main():
    print("Hello, world!")
    
    # Example of how to create an instance of a class type and access a tile.
    # myBoard = Board()
    # myBoard.grid
    # myBoard.grid[1][6]


# This snippet of code calls main(). Without this, main() will not run.
# The if statement is true only when run as a program.
if __name__ == "__main__":
    main()