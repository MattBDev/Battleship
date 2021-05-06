from typing import Tuple

from direction import Direction, Orientation


class Ship:
    # origin = origin coordinate
    def __init__(self, origin, direction, length):
        self.sunk = False
        self.length = length
        self.maxDamage = length
        self.damage = 0
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
        self.sections[self.sections.index(((coord[0], coord[1]), True))][2] = False
        self.aliveSections -= 1

        # TODO: add hit and miss function from GameBoard

    def isAlive(self):
        if self.aliveSections <= 0:
            return False
        return True

    def checkSunk(self) -> bool:
        return self.damage >= self.maxDamage

    @staticmethod
    def isInGrid(x, y, orientation, ship_length) -> bool:
        if orientation == Orientation.VERTICAL:
            return x + ship_length <= 10
        else:
            return y + ship_length <= 10