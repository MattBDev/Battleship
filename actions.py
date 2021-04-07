# This file contains actions to be employed by the various AIs.

def fire(board, coord):
    print("Firing at tile (", coord[0], ", ", coord[1], ").")
    board.shootTile(coord)
