# 2021.04.04
# Mit Bailey
# Copyright (c) 2021

# This file contains algorithms to be employed by the various AIs.

"""
The ship class is used to generate one of each type of ship.

onTiles: References to the Tile objects on top of which this ship resides

self.length: number of tiles ship occupies
self.aliveSections: what tiles of the ship have not been hit
self.sections: array representing tile sections the ship is on
"""
class Ship:
    def __init__(self, origin, direction, length):  # origin = origin coordinate
        self.length = length
        self.aliveSections = length

        self.sections = []

        # Sections take the form [(xCoord, yCoord), Alive?]
        for index in range(self.length):
            if direction == "North":
                self.sections.append(((origin[0], origin[1] + index), True))
            elif direction == "South":
                self.sections.append(((origin[0], origin[1] - index), True))
            elif direction == "East":
                self.sections.append(((origin[0] + index, origin[1]), True))
            elif direction == "West":
                self.sections.append(((origin[0] - index, origin[1]), True))

    def hit(self, coord):
        self.sections[self.sections.index(((coord[0], coord[1]), True))][2] = False
        self.aliveSections -= 1

    def isAlive(self):
        if self.aliveSections <= 0:
            return False
        return True

def HP_findShot(board):
    # TODO: Add code to actually find a good shot.
    x = 0
    y = 0

    return x, y

# TODO: This function.
def HP_placeShip(board, vessel):
    if vessel == "Carrier":
        return Ship((0, 0), "North", 5)
    elif vessel == "Battleship":
        return Ship((0, 0), "North", 4)
    elif vessel == "Destroyer":
        return Ship((0, 0), "North", 3)
    elif vessel == "Submarine":
        return Ship((0, 0), "North", 3)
    elif vessel == "PTBoat":
        return Ship((0, 0), "North", 2)
