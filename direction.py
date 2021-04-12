# 2021.03.16
# Matt Bonanno
# Copyright (c) 2021

from enum import Enum
class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4

class Orientation(Enum):
    HORIZONTAL = 1  # When the ship is along the x axis.
    VERTICAL = 0  # when the ship is along the y axis.