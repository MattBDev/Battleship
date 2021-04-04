# 2021.04.04
# Mit Bailey
# Copyright (c) 2021

# This file contains the AI agents.

import algorithms
import actions

class HP_AI:
    def __init__(self, board):
        self.board = board
        self.shipsAlive = 5
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

        if self.shipsAlive is 0:
            return

    # Called when the game is ready for this AI to take their turn.
    def takeTurn(self):
        shotCoord = algorithms.HP_findShot(self.board)
        actions.fire(self.board, shotCoord)

