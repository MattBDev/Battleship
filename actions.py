# 2021.04.04
# Mit Bailey
# Copyright (c) 2021

# This file contains actions to be employed by the various AIs.

def fire(board, coord):
    print("Firing at tile ( ", coord[0], ", ", coord[1], ").")
    board.shootTile(coord)
