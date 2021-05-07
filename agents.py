# 2021.03.16
# Mit Bailey
# Ryan Balachandran
# Matt Bonanno
# Copyright (c) 2021

# This file contains the AI agents.

from __future__ import annotations

import random
from typing import Tuple, List

import GameBoard
import actions
import constants


class Random_AI:
    def __init__(self, board, fleet, stats: GameBoard.Statistics):
        self.stats = stats
        self.board = board
        self.fleet = fleet
        self.shipsAlive = fleet.numShips
        self.prevShot = -1, -1
        self.huntList: List[Tuple[int, int]] = []

    # Called when the game is ready for this AI to take their turn.
    def takeTurn(self):
        print(self.__class__, " taking turn")
        shot_pos = self.findRandomShot()
        result = actions.fire(self.board, shot_pos)
        if result:
            self.stats.add_hits()
            self.fleet.getShipAtCoord(shot_pos[0], shot_pos[1]).addDamage()
        else:
            self.stats.add_misses()

    def findRandomShot(self):
        while True:
            x = random.randint(0, 10)
            y = random.randint(0, 10)
            if not self.board.grid[x][y].shot:
                return x, y


class Hunt:
    def __init__(self, board, fleet, stats: GameBoard.Statistics):
        self.stats = stats
        self.board = board
        self.fleet = fleet
        self.shipsAlive = fleet.numShips
        self.prevShot = -1, -1
        self.huntList: List[Tuple[int, int]] = []

    # Called when the game is ready for this AI to take their turn.
    def takeTurn(self):
        print(self.__class__, " taking turn")
        if len(self.huntList) == 0:
            shot_pos = self.findRandomShot()
            result = actions.fire(self.board, shot_pos)
            if result:
                self.stats.add_hits()
                self.fleet.getShipAtCoord(shot_pos[0], shot_pos[1]).addDamage()
                for adj_cells in constants.get_adjacent_cells(self.board, shot_pos[0], shot_pos[1]):
                    if adj_cells not in self.huntList and not self.board.grid[adj_cells[0]][adj_cells[1]].shot:
                        self.huntList.append(adj_cells)
            else:
                self.stats.add_misses()
        else:
            pop = self.huntList.pop()
            result = actions.fire(self.board, pop)
            if result:
                self.stats.add_hits()
                self.fleet.getShipAtCoord(pop[0], pop[1]).addDamage()
                for adj_cells in constants.get_adjacent_cells(self.board, pop[0], pop[1]):
                    if adj_cells not in self.huntList and not self.board.grid[adj_cells[0]][adj_cells[1]].shot:
                        self.huntList.append(adj_cells)
            else:
                self.stats.add_misses()

    def findRandomShot(self):
        while True:
            x = random.randint(0, 10)
            y = random.randint(0, 10)
            if not self.board.grid[x][y].shot:
                return x, y


class HuntParity(Hunt):
    def __init__(self, board, fleet, stats):
        super().__init__(board, fleet, stats)
        self.parity_coords = set()

    def findRandomShot(self):

        # The Random algorithm works by firing at random tiles
        # Randomly shoot within grid parameters
        while True:
            if len(self.parity_coords) < 24:
                x = random.randrange(0, 10, 2)
                y = random.randrange(0, 10, 2)
            else:
                print("ignoring parity")
                x = random.randint(0, 9)
                y = random.randint(0, 9)
            print(x, ",", y)
            if not self.board.grid[x][y].shot:
                if len(self.parity_coords) < 24:
                    if x % 2 == 0 or y % 2 == 0:
                        self.parity_coords.add((x, y))
                        return x, y
                else:
                    return x, y


