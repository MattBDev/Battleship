# 2021.03.16
# Mit Bailey
# Ryan Balachandran
# Matt Bonanno
# Copyright (c) 2021

# This file contains algorithms to be employed by the various AIs.

"""
The ship class is used to generate one of each type of ship.

self.length: number of tiles ship occupies
self.aliveSections: what tiles of the ship have not been hit
self.sections: array representing tile sections the ship is on
"""
from __future__ import annotations

import random
from random import randint
from typing import Tuple

import GameBoard
from GameBoard import Board
from direction import Orientation
from ship import Ship


def HP_findShot(board, prevShot):
    # TODO: Add code to actually find a good shot.

    # The Hunt-Parity algorithm works by
    # PARITY
    # - Not firing at squarely adjacent tiles.
    # HUNT
    # - Once a hit is achieved, search the nearby tiles.
    x = 0
    y = 0


    if board.grid[prevShot[0]][prevShot[1]].shot is True and board.grid[prevShot[0]][prevShot[1]].ship is True:
        pass   # TODO: Find an appropriate shot near the hit
    else:
        if board.grid[0][0].shot is True:
            # We shot (0,0) first.
            while board.grid[x][y].shot is True and y <= 10:
                x = (x + 2) % 11
                y += 1
        elif board.grid[0][1].shot is True:
            # We shot (0,1) first.
            x = (x + 2) % 11
            y += 1
        else:
            # We have not yet shot.
            x = random.randint(0, 1)
            y = 0

    return x, y


def Random_findShot(board, prevShot):
    # The Random algorithm works by firing at random tiles
    x = 0
    y = 0

    # Randomly shoot within grid parameters
    # TODO: make sure tile is not shot at twice
    while not board.grid[prevShot[0]][prevShot[1]].shot:
        x = random.randint(0, 9)
        y = random.randint(0, 9)

    return x, y

def Hunt_findShot(agent, board: GameBoard, prevShot) -> Tuple[int, int]:

    # TODO: Add code to actually find a good shot.

    # The Hunt-Parity algorithm works by
    # HUNT
    # - Once a hit is achieved, search the nearby tiles.
    x = 0
    y = 0

    if board.grid[prevShot[0]][prevShot[1]].shot is True and board.grid[prevShot[0]][prevShot[1]].ship is True:
        if not agent.huntSet:
            pop: Tuple[int, int] = agent.huntSet.pop()
            while pop in agent.prevShotList:
                pop = agent.huntSet.pop()
            return pop
        else:
            print("either ship was sunk or an error occured")
    else:
        if board.grid[0][0].shot is True:
            # We shot (0,0) first.
            while board.grid[x][y].shot is True and y <= 10:
                x = (x + 2) % 11
                y += 1
        elif board.grid[0][1].shot is True:
            # We shot (0,1) first.
            x = (x + 2) % 11
            y += 1
        else:
            # We have not yet shot.
            x = random.randint(0, 1)
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
                    board.grid[x+j][y] = 'now there should be a ship here'  # TODO
                else:
                    board.grid[x][y + j] = 'now there should be a ship here'  # TODO
