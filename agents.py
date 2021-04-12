# 2021.03.16
# Mit Bailey
# Ryan Balachandran
# Copyright (c) 2021

# This file contains the AI agents.

import actions
import algorithms
import GameBoard


class HP_AI:
    def __init__(self, board):
        self.board = board
        self.shipsAlive = 5
        self.prevShot = -1, -1
        self.shipSet = []
        self.shipSet.append(algorithms.HP_placeShip(self.board, "Carrier"))
        self.shipSet.append(algorithms.HP_placeShip(self.board, "Battleship"))
        self.shipSet.append(algorithms.HP_placeShip(self.board, "Destroyer"))
        self.shipSet.append(algorithms.HP_placeShip(self.board, "Submarine"))
        self.shipSet.append(algorithms.HP_placeShip(self.board, "PTBoat"))

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
        GameBoard.Statistics.add_turns()


# TODO: add random AI class
