import pygame
from srcs.settings import *

## POSITIONING CLASS FOR GRID
class Pos:
    def __init__(self, row, col):
        self.row = row
        self.col = col

## BLOCK CLASS
class Block:
    def __init__(self, id, cellsize, cellcolors, margin = 1):
        self.id = id
        self.cells = []
        self.cellsize = cellsize
        self.cellcolors = cellcolors
        self.rotation_state = 0
        self.settings = Settings()
        self.colors = self.settings.getCellColors()
        self.margin = margin
        self.offset = Pos(0, 3)
        self.ispreview = False

    def move(self, rows, cols):     ##Moving the block by rows and columns
        self.offset.row += rows
        self.offset.col += cols

    def rotate(self, clockwise = True): ##Rotating
        if clockwise:
            if self.rotation_state == len(self.cells) - 1:
                self.rotation_state = 0
            else:
                self.rotation_state += 1
        else:
            if self.rotation_state == 0:
                self.rotation_state = len(self.cells) - 1
            else:
                self.rotation_state -= 1

    def new(self):      ## Returs a new block of same type with default position
        return type(self)(self.cellsize, self.cellcolors, margin = self.margin)

    def getcellpos(self):   ## Returns the positions of all tiles in the block
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for pos in tiles:
            pos = Pos(pos.row + self.offset.row, pos.col + self.offset.col)
            moved_tiles.append(pos)

        return moved_tiles


    def draw(self, surface):    ## Draws it self on a surface
        tiles = self.getcellpos()
        for tile in tiles:
            cell_rect = pygame.Rect(tile.col * self.cellsize + self.margin, tile.row * self.cellsize + self.margin, self.cellsize - self.margin, self.cellsize - self.margin)

            cell_color = self.colors[self.id]
            if not self.ispreview:
                pygame.draw.rect(surface, cell_color, cell_rect)
            else:
                pygame.draw.rect(surface, cell_color, cell_rect, 1)


## Child Blocks
class LBlock(Block):
    def __init__(self, cellsize, cellcolors, margin = 1):
        super().__init__(1, cellsize, cellcolors, margin = margin)
        ## Rotations
        self.cells = [
                [Pos(0, 2), Pos(1, 0), Pos(1, 1), Pos(1, 2)],
                [Pos(0, 1), Pos(1, 1), Pos(2, 1), Pos(2, 2)],
                [Pos(1, 0), Pos(1, 1), Pos(1, 2), Pos(2, 0)],
                [Pos(0, 0), Pos(0, 1), Pos(1, 1), Pos(2, 1)]
                ]

# SAME TREND
class JBlock(Block):
    def __init__(self, cellsize, cellcolors, margin = 1):
        super().__init__(2, cellsize, cellcolors, margin = margin)
        self.cells = [
                [Pos(0, 0), Pos(1, 0), Pos(1, 1), Pos(1, 2)],
                [Pos(0, 1), Pos(0, 2), Pos(1, 1), Pos(2, 1)],
                [Pos(1, 0), Pos(1, 1), Pos(1, 2), Pos(2, 2)],
                [Pos(0, 1), Pos(1, 1), Pos(2, 0), Pos(2, 1)]
                ]

class IBlock(Block):
    def __init__(self, cellsize, cellcolors, margin = 1):
        super().__init__(3, cellsize, cellcolors, margin = margin)
        self.cells = [
                [Pos(1, 0), Pos(1, 1), Pos(1, 2), Pos(1, 3)],
                [Pos(0, 2), Pos(1, 2), Pos(2, 2), Pos(3, 2)],
                [Pos(2, 0), Pos(2, 1), Pos(2, 2), Pos(2, 3)],
                [Pos(0, 1), Pos(1, 1), Pos(2, 1), Pos(3, 1)]
                ]
        self.offset = Pos(-1, 3)

class OBlock(Block):
    def __init__(self, cellsize, cellcolors, margin = 1):
        super().__init__(4, cellsize, cellcolors, margin = margin)
        self.cells = [
                [Pos(0, 0), Pos(0, 1), Pos(1, 0), Pos(1, 1)],
                [Pos(0, 0), Pos(0, 1), Pos(1, 0), Pos(1, 1)],
                [Pos(0, 0), Pos(0, 1), Pos(1, 0), Pos(1, 1)],
                [Pos(0, 0), Pos(0, 1), Pos(1, 0), Pos(1, 1)]
                ]
        self.offset = Pos(0, 4)

class SBlock(Block):
    def __init__(self, cellsize, cellcolors, margin = 1):
        super().__init__(5, cellsize, cellcolors, margin = margin)
        self.cells = [
                [Pos(0, 1), Pos(0, 2), Pos(1, 0), Pos(1, 1)],
                [Pos(0, 1), Pos(1, 1), Pos(1, 2), Pos(2, 2)],
                [Pos(1, 1), Pos(1, 2), Pos(2, 0), Pos(2, 1)],
                [Pos(0, 0), Pos(1, 0), Pos(1, 1), Pos(2, 1)]
                ]

class TBlock(Block):
    def __init__(self, cellsize, cellcolors, margin = 1):
        super().__init__(6, cellsize, cellcolors, margin = margin)
        self.cells = [
                [Pos(0, 1), Pos(1, 0), Pos(1, 1), Pos(1, 2)],
                [Pos(0, 1), Pos(1, 1), Pos(1, 2), Pos(2, 1)],
                [Pos(1, 0), Pos(1, 1), Pos(1, 2), Pos(2, 1)],
                [Pos(0, 1), Pos(1, 0), Pos(1, 1), Pos(2, 1)]
                ]

class ZBlock(Block):
    def __init__(self, cellsize, cellcolors, margin = 1):
        super().__init__(7, cellsize, cellcolors, margin = margin)
        self.cells = [
                [Pos(0, 0), Pos(0, 1), Pos(1, 1), Pos(1, 2)],
                [Pos(0, 2), Pos(1, 1), Pos(1, 2), Pos(2, 1)],
                [Pos(1, 0), Pos(1, 1), Pos(2, 1), Pos(2, 2)],
                [Pos(0, 1), Pos(1, 0), Pos(1, 1), Pos(2, 0)]
                ]
