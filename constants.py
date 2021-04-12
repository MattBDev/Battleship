# 2021.03.16
# Ryan Balachandran
# Matt Bonanno
# Copyright (c) 2021

# Define some colors
from typing import List, Tuple

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
size1 = [(width * 10) + (margin * 10) + margin,
         (height * 10) + (margin * 10) + margin]

# Set the Width and Height of the screen [width, height]
size2 = [((width * 10) + (margin * 10) + margin) * 2 + 40,
         (height * 10) + (margin * 10) + margin]

ALL_SHIPS: List[Tuple[str, int]] = [("Carrier", 5), ("Battleship", 4),
             ("Destroyer", 3), ("Submarine", 3), ("PTBoat", 2)]
CARRIER = ALL_SHIPS[0]
BATTLESHIP = ALL_SHIPS[1]
DESTROYER = ALL_SHIPS[2]
SUBMARINE = ALL_SHIPS[3]
PTBOAT = ALL_SHIPS[4]