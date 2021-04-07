import pygame
from constants import *


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

shootTile: shoot the given tile and perform the appropriate cleanup
single_board: displays one grid to screen when testing algorithms
double_board: displays two grids to screen when comparing algorithms
"""
class Board(object):
    def __init__(self, result = 0, turns = 0):
        self.result = result
        self.turns = turns
        self.grid = []  # Used for making the gameboard
        self.ships = []

        # Create a 2D array
        for row in range(10):
            self.grid.append([])  # Add an empty array that will hold each Tile
            for column in range(10):
                self.grid[row].append([Tile.shot, Tile.ship])

    # shoot the given tile and perform the appropriate cleanup
    def shootTile(self, coord):
        print(coord)
        # self.grid[coord[0]][coord[1]].shot = True
        # self.grid[coord[0]][coord[1]].shot = [True, False]
        self.grid[coord[0]][coord[1]] = [True, False]

    # Returns the amount of turns taken to main so that it can be used in the scoreboard
    def get_turns(self):
        return self.turns

    def single_board(self):
        screen = pygame.display.set_mode(size1)
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
            screen.fill(WHITE)

            # Fills all of the grid spaces with white
            for row in range(10):
                for column in range(10):
                    color = BLUE
                    if self.grid[row][column] == 1:  # Miss
                        color = BLACK
                    if self.grid[row][column] == 2:  # Hit
                        color = RED

                    pygame.draw.rect(screen, color, [(margin + width) * column + margin,
                                                     (margin + height) * row + margin,
                                                     width, height])

            # Updates the screen with what has been drawn.
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()

    def double_board(self):
        screen = pygame.display.set_mode(size2)
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
            screen.fill(WHITE)

            pygame.draw.rect(screen, BLACK, pygame.Rect(1288 / 2, 0, 40, 644))

            # Fills all of the grid spaces with white
            for row in range(10):
                for column in range(20):
                    color = BLUE

                    # TODO: implement if statement for grid hit/miss as in single_board

                    if column > 9:
                        pygame.draw.rect(screen, color,
                                         [(margin + width) * column + 44 + margin,
                                          (margin + height) * row + margin, width,
                                          height])

                    if column < 10:
                        pygame.draw.rect(screen, color,
                                         [(margin + width) * column + margin,
                                          (margin + height) * row + margin, width,
                                          height])

            # Updates the screen with what has been drawn.
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()

    def print_board(self, choice):
        # Initialize pygame
        pygame.init()

        if choice == 1:
            self.single_board()
        elif choice == 2:
            self.double_board()
