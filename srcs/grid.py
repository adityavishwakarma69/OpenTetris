import pygame
from srcs.settings import *

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

    def print(self):
        for row in self.grid:
            print(*row, sep = ' ') 

    def draw(self):
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.grid[row][col]
                cell_rect = pygame.Rect(col * self.cellsize + self.margin, row * self.cellsize + self.margin, self.cellsize - self.margin, self.cellsize - self.margin)
                cell_color = self.colors[cell]
                pygame.draw.rect(self.surface, cell_color, cell_rect)

    def isInside(self, row, col):
        return row >= 0 and row < self.rows and col >=0 and col < self.cols

    def isCollide(self, row, col):
        if self.grid[row][col] != 0:
            return True
        return False

    def isRowFull(self, row):
        row = self.grid[row]
        for n in row:
            if n == 0:
                return False
        return True

    def clearRow(self, row):
        for col in range(self.cols):
            self.grid[row][col] = 0

    def moveRow(self, row, num):
        for col in range(self.cols):
            self.grid[row + num][col] = self.grid[row][col]
            self.grid[row][col] = 0

    def clean(self):
        cleared = 0
        for row in range(self.rows - 1, -1, -1):
            if self.isRowFull(row):
                self.clearRow(row)
                cleared += 1
            elif cleared > 0:
                self.moveRow(row, cleared)
        
        return cleared
