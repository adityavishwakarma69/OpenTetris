#Aditya Vishwakarma, hereby disclaims all copyright interest in this program (which deconstructs trees) written by Aditya Vishwakarma.

#signature of Aditya Vishwakarma


import pygame
from srcs.settings import *

## The grid class 
class Grid:
    def __init__(self, rows, cols, cellsize, cellcolors, margin = 1):
        self.rows = rows
        self.cols = cols
        self.cellsize = cellsize
        self.margin = margin

        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.surface = pygame.Surface((self.cols * self.cellsize, self.rows * self.cellsize))

        self.settings = Settings()
        self.colors = cellcolors 

    ## Stdout the grid for debuging purpose
    def print(self):
        for row in self.grid:
            print(*row, sep = ' ') 

    ## The draws the grid components on the grid surface
    def draw(self):
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.grid[row][col]
                cell_rect = pygame.Rect(col * self.cellsize + self.margin, row * self.cellsize + self.margin, self.cellsize - self.margin, self.cellsize - self.margin)
                cell_color = self.colors[cell]
                pygame.draw.rect(self.surface, cell_color, cell_rect)

    ## Checks if the given row and column exists in the row
    def isInside(self, row, col):
        return row >= 0 and row < self.rows and col >=0 and col < self.cols 

    ## Checks if the row and column is tile of a block or not
    def isCollide(self, row, col):
        if self.grid[row][col] != 0:
            return True
        return False

    ## Checks if a row is filled
    def isRowFull(self, row):
        row = self.grid[row]
        for n in row:
            if n == 0:
                return False
        return True

    ## clears a row
    def clearRow(self, row):
        for col in range(self.cols):
            self.grid[row][col] = 0

    ## Moves a row down
    def moveRow(self, row, num):
        for col in range(self.cols):
            self.grid[row + num][col] = self.grid[row][col]
            self.grid[row][col] = 0

    ## clears all the filled rows and moves the remaning down
    def clean(self):
        cleared = 0
        for row in range(self.rows - 1, -1, -1):
            if self.isRowFull(row):
                self.clearRow(row)
                cleared += 1
            elif cleared > 0:
                self.moveRow(row, cleared)
        
        return cleared
