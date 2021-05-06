# 2021.03.16
# Mit Bailey
# Ryan Balachandran
# Matt Bonanno
# Copyright (c) 2021

# This file contains the AI agents.
from typing import Tuple, List

from constants import BATTLESHIP, CARRIER, DESTROYER, PTBOAT, SUBMARINE
import actions
import algorithms


class HP_AI:
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
            print(ship)

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
        shotCoord = algorithms.HP_findShot(self.board, self.prevShot)
        self.prevShot = shotCoord
        actions.fire(self.board, shotCoord)
        self.board.add_turns()  # TODO the statistics object needs to exist before we can actually use this function


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
            print(ship)

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
    def __init__(self, board):
        self.board = board
        self.shipsAlive = 5
        self.prevShot = -1, -1
        self.shipSet = []
        self.huntList: List[Tuple[int, int]] = []
        self.prevShotList: List[Tuple[int, int]] = []
        self.shipSet.append(algorithms.placeShip(self.board, CARRIER))
        self.shipSet.append(algorithms.placeShip(self.board, BATTLESHIP))
        self.shipSet.append(algorithms.placeShip(self.board, DESTROYER))
        self.shipSet.append(algorithms.placeShip(self.board, SUBMARINE))
        self.shipSet.append(algorithms.placeShip(self.board, PTBOAT))

        for ship in self.shipSet:
            print(ship)

    # Determines whether this player has any ships left.
    def evaluate(self):
        self.shipsAlive = 0

        # Count number of living ships.
        for ship in self.shipSet:
            if ship.isAlive():
                self.shipsAlive += 1

        if self.shipsAlive == 0:
            return

    # Are there still ships alive on the grid?
    def checkShipsAlive(self):
        self.shipsAlive = 0

        # Count number of living ships.
        for ship in self.shipSet:
            if ship.isAlive():
                self.shipsAlive += 1
                return True

        if self.shipsAlive == 0:
            return False

    # Called when the game is ready for this AI to take their turn.
    def takeTurn(self):
        if self.checkShipsAlive():
            shotCoord = algorithms.Hunt_findShot(self, self.board, self.prevShot)
            self.prevShot = shotCoord
            actions.fire(self.board, shotCoord)
            self.board.add_turns()  # TODO the statistics object needs to exist before we can actually use this function

