# 2021.03.16
# Ryan Balachandran
# Matt Bonanno
# Copyright (c) 2021

# Define some colors
from __future__ import annotations

from typing import Tuple, List

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (10, 10, 255)
GRAY = (110, 110, 110)

# This sets the WIDTH and HEIGHT of each grid location
width, height = 60, 60

# This sets the margin between each tile
margin = 4

# Set the Width and Height of the screen [width, height]
size1 = [(width * 10) + (margin * 10) + margin + 50,
         (height * 10) + (margin * 10) + margin + 50]

# Set the Width and Height of the screen [width, height]
size2 = [((width * 10) + (margin * 10) + margin) * 2 + 150,
         (height * 10) + (margin * 10) + margin + 50]

# List[Tuple[str,int]] has name and size of ships
ALL_SHIPS: List[Tuple[str, int]] = [("Carrier", 5), ("Battleship", 4),
                                    ("Destroyer", 3), ("Submarine", 3), ("PTBoat", 2)]

CARRIER = ALL_SHIPS[0]
BATTLESHIP = ALL_SHIPS[1]
DESTROYER = ALL_SHIPS[2]
SUBMARINE = ALL_SHIPS[3]
PTBOAT = ALL_SHIPS[4]


# from stackoverflow https://stackoverflow.com/a/48677124/13283504
# modified for our project
def get_adjacent_cells(x_coord, y_coord):
    grid = []
    for row in range(10):
        grid.append([])  # Add an empty array that will hold each Tile
        for column in range(10):
            grid[row].append(True)
    for x, y in [(x_coord + i, y_coord + j) for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0]:
        if x < 0 or y < 0:
            continue
        else:
            if grid[x][y]:
                print("Values: {0}, {1}".format(x, y))
