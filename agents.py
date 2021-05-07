# 2021.03.16
# Mit Bailey
# Ryan Balachandran
# Matt Bonanno
# Copyright (c) 2021

# This file contains the AI agents.

from __future__ import annotations

import random
from typing import Tuple, List

import constants
from constants import BATTLESHIP, CARRIER, DESTROYER, PTBOAT, SUBMARINE
import actions
import algorithms


class HuntParity:
    def __init__(self, board, fleet):
        self.board = board
        self.fleet = fleet
        self.shipsAlive = fleet.numShips
        self.prevShot = -1, -1
        self.huntList: List[Tuple[int, int]] = []

    # Determines whether this player has any ships left.
    def evaluate(self):
        self.shipsAlive = 0

        # Count number of living ships.
        # for ship in self.shipSet:
        #     if ship.isAlive():
        #         self.shipsAlive += 1
        #
        # if self.shipsAlive == 0:
        #     return

    # Are there still ships alive on the grid?
    def checkShipsAlive(self):
        self.shipsAlive = 0

        # # Count number of living ships.
        # for ship in self.shipSet:
        #     if ship.isAlive():
        #         self.shipsAlive += 1
        #         return True
        #
        # if self.shipsAlive == 0:
        #     return False

    # Called when the game is ready for this AI to take their turn.
    def takeTurn(self):
        print("Hunt taking turn")
        shot_pos = self.findRandomShotP()
        if len(self.huntList) == 0:
            shot_pos = self.findRandomShotP()
            result = actions.fire(self.board, shot_pos)
            if result:
                self.huntList.extend(constants.get_adjacent_cells(self.board, shot_pos[0], shot_pos[1]))
        else:
            result = actions.fire(self.board, self.huntList.pop())
            if result:
                self.huntList.extend(constants.get_adjacent_cells(self.board, shot_pos[0], shot_pos[1]))

    def findRandomShotP(self):
        # The Random algorithm works by firing at random tiles
        x: int = 0
        y: int = 0
        # Randomly shoot within grid parameters
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if not self.board.grid[x][y].shot:
                if x % 2 == 0 and y % 2 == 0:
                    return x, y


class Random_AI:
    def __init__(self, board):
        self.board = board
        self.shipsAlive = 5
        self.prevShot = -1, -1
        self.shipSet = []
        self.shipSet.append(algorithms.placeShip(self.board, CARRIER))
        self.shipSet.append(algorithms.placeShip(self.board, BATTLESHIP))
        self.shipSet.append(algorithms.placeShip(self.board, DESTROYER))
        self.shipSet.append(algorithms.placeShip(self.board, SUBMARINE))
        self.shipSet.append(algorithms.placeShip(self.board, PTBOAT))

        for ship in self.shipSet:
            print("Ship  " + ship)

    # Determines whether this player has any ships left.
    def evaluate(self):
        self.shipsAlive = 0

        # Count number of living ships.
        for ship in self.shipSet:
            if ship.isAlive():
                self.shipsAlive += 1

        if self.shipsAlive == 0:
            return

    # Called when the game is ready for this AI to take their turn.
    def takeTurn(self):
        shotCoord = algorithms.Random_findShot(self.board, self.prevShot)
        self.prevShot = shotCoord
        actions.fire(self.board, shotCoord)
        self.board.add_turns()


class Hunt:
    def __init__(self, board, fleet):
        self.board = board
        self.fleet = fleet
        self.shipsAlive = fleet.numShips
        self.prevShot = -1, -1
        self.huntSet: Set[Tuple[int, int]] = []

    # Determines whether this player has any ships left.
    def evaluate(self):
        self.shipsAlive = 0

        # Count number of living ships.
        # for ship in self.shipSet:
        #     if ship.isAlive():
        #         self.shipsAlive += 1
        #
        # if self.shipsAlive == 0:
        #     return

    # Are there still ships alive on the grid?
    def checkShipsAlive(self):
        self.shipsAlive = 0

        # # Count number of living ships.
        # for ship in self.shipSet:
        #     if ship.isAlive():
        #         self.shipsAlive += 1
        #         return True
        #
        # if self.shipsAlive == 0:
        #     return False

    # Called when the game is ready for this AI to take their turn.
    def takeTurn(self):
        print("Hunt taking turn")
        shot_pos = self.findRandomShot()
        if len(self.huntSet) == 0:
            shot_pos = self.findRandomShot()
            result = actions.fire(self.board, shot_pos)
            if result:
                self.huntSet.extend(constants.get_adjacent_cells(self.board, shot_pos[0], shot_pos[1]))
        else:
            result = actions.fire(self.board, self.huntSet.pop())
            if result:
                self.huntSet.extend(constants.get_adjacent_cells(self.board, shot_pos[0], shot_pos[1]))

    def findRandomShot(self):
        # The Random algorithm works by firing at random tiles
        x: int = 0
        y: int = 0
        alreadyShot = False
        # Randomly shoot within grid parameters
        while not alreadyShot:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if not self.board.grid[x][y].shot:
                return x, y

        return x, y
