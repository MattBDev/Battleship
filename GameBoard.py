import pygame

from constants import BLACK, WHITE, RED, BLUE, width, height, margin, size

"""
The Tile class composes the basic makeup of the Battleship board.

shot: Has this tile been shot at?
ship: Is a ship segment present?
"""
class Tile:
    shot = False
    ship = False



"""
Board class contains the Ships and Tiles for one player

__init__(self): This default constructor initializes empty lists for ships and the
                grid before appending 10 empty lists and 10 Tiles to each new list.

self.grid: Contains the game grid.
self.ships: Contains references to all of this board's ships.

TODO:
    1. add width and height to init?
    2. add Tile to append
"""
class Board(object):
    def __init__(self, result = 0, turns = 0):
        self.result = result
        self.turns = turns
        self.grid = []  # Used for making the gameboard
        self.ships = []

        # Create a 2D array
        for row in range(9):
            self.grid.append([])  # Add an empty array that will hold each Tile
            for column in range(9):
                self.grid[row].append(Tile)

    # Shoot the given tile and perform the appropriate cleanup.
    def shootTile(self, coord):
        self.grid[coord[0]][coord[1]].shot = True

    # Returns the amount of turns taken to main so that it can be used in the scoreboard
    def get_turns(self):
        return self.turns

    def print_board(self):
        # Initialize pygame
        pygame.init()

        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Battleship")

        AllShipsSunk = False  # Loop until the user clicks the close button
        clock = pygame.time.Clock()  # Used to manage how fast the screen updates

        while not AllShipsSunk:
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    AllShipsSunk = True  # Flag that we are done so we exit this loop

            # --- Game logic should go here

            # --- Screen-clearing code goes here

            # Drawing the display
            screen.fill(BLACK)

            # Fills all of the grid spaces with white
            for row in range(10):
                for column in range(10):
                    color = BLUE
                    if self.grid[row][column] == 1:  # Miss
                        color = WHITE
                    if self.grid[row][column] == 2:  # Hit
                        color = RED

                    pygame.draw.rect(screen, color, [(margin + width) * column + margin,
                                                     (margin + height) * row + margin,
                                                     width, height])

            # Updates the screen with what has been drawn.
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()
