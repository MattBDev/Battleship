# 2021.03.16
# Mit Bailey
# Copyright (c) 2021

# This file contains actions to be employed by the various AIs.

from __future__ import annotations

def fire(board, coord):
    print("Firing at tile (", coord[0], ", ", coord[1], ").")
    board.shootTile(coord)
    board.Statistics.add_shots()