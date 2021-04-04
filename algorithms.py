# 2021.04.04
# Mit Bailey
# Copyright (c) 2021

# This file contains algorithms to be employed by the various AIs.

# The Ship class is used to generate one of each type of Battleship ship.
# onTiles: References to the Tile objects on top of which this ship resides.
class Ship:
    def __init__(self, origin, direction, length): # origin = origin coordinate
        self.length = length
        self.aliveSections = length # this is variable

        self.sections = []
        # Sections take the form ((xCoord, yCoord), Alive?)
        for index in range(self.length):
            if direction is "North":
                self.sections.append(((origin[0], origin[1] + index), True))
            elif direction is "South":
                self.sections.append(((origin[0], origin[1] - index), True))
            elif direction is "East":
                self.sections.append(((origin[0] + index, origin[1]), True))
            elif direction is "West":
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

    return (x, y)

# TODO: This function.
def HP_placeShip(board, type):
    if type is "Carrier":
        return Ship((0, 0), "North", 5)
    elif type is "Battleship":
        return Ship((0, 0), "North", 4)
    elif type is "Destroyer":
        return Ship((0, 0), "North", 3)
    elif type is "Submarine":
        return Ship((0, 0), "North", 3)
    elif type is "PTBoat":
        return Ship((0, 0), "North", 2)