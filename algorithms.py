# This file contains algorithms to be employed by the various AIs.

"""
The ship class is used to generate one of each type of ship.

onTiles: References to the Tile objects on top of which this ship resides

self.length: number of tiles ship occupies
self.aliveSections: what tiles of the ship have not been hit
self.sections: array representing tile sections the ship is on
"""
from __future__ import annotations
from os import stat
from random import randint
from typing import Tuple

from GameBoard import Board
from direction import Direction, Orientation


class Ship:
    # origin = origin coordinate
    def __init__(self, origin, direction, length):
        self.length = length
        self.aliveSections = length

        self.sections = []

        # Sections take the form [(xCoord, yCoord), Alive?]
        for index in range(self.length):
            if direction == Direction.NORTH:
                v1 = ((origin[0], origin[1] + index), True)
                self.sections.append(v1)
            elif direction == Direction.SOUTH:
                self.sections.append(((origin[0], origin[1] - index), True))
            elif direction == Direction.EAST:
                self.sections.append(((origin[0] + index, origin[1]), True))
            elif direction == Direction.WEST:
                self.sections.append(((origin[0] - index, origin[1]), True))

    def hit(self, coord: Tuple[int, int]):
        self.sections[self.sections.index(
            ((coord[0], coord[1]), True))][2] = False
        self.aliveSections -= 1

    def isAlive(self):
        if self.aliveSections <= 0:
            return False
        return True

    @staticmethod
    def isInGrid( x, y, orientation, ship_length) -> bool:
        if orientation == Orientation.VERTICAL:
            return x + ship_length <= 10
        else:
            return y + ship_length <= 10


def HP_findShot(board):
    # TODO: Add code to actually find a good shot.
    x = 0
    y = 0

    return x, y

def isLegal(board: Board, x, y, orientation, ship_length):
    if Ship.isInGrid(x, y, orientation, ship_length):
        i = 0
        while i < ship_length:
            if orientation == Orientation.VERTICAL:
                if board.grid[x + i][y] == 'TODO: Contains ship check':
                    return False
            else:
                if board.grid[x][y + i] == 'TODO: Contains ship check':
                    return False
            i += 1
        return True
    else:
        return False

def placeShip(board: Board, vessel: tuple[str, int]):
    validPosition = False
    while not validPosition:
        x = randint(0, 9)
        y = randint(0, 9)
        orientation = randint(0, 1)
        # TODO fix this section
        # if vessel == "Carrier":
        #     ship = Ship((0, 0), Direction.NORTH, 5)
        # elif vessel == "Battleship":
        #     ship = Ship((0, 0), Direction.NORTH, 4)
        # elif vessel == "Destroyer":
        #     ship = Ship((0, 0), Direction.NORTH, 3)
        # elif vessel == "Submarine":
        #     ship = Ship((0, 0), Direction.NORTH, 3)
        # elif vessel == "PTBoat":
        #     ship = Ship((0, 0), Direction.NORTH, 2)
        if isLegal(board, x, y, orientation, vessel[1]):
            j = 0
            while j < vessel[1]:
                if orientation == Orientation.VERTICAL:
                    board.grid[x+j][y] = 'now there should be a ship here'  #TODO
                else:
                    board.grid[x][y + j] = 'now there should be a ship here'  #TODO