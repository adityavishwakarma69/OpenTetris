import random
from srcs.grid import *
from srcs.blocks import *
from srcs.settings import *
    
class Game:
    def __init__(self, cellcolors, bgcolor = (40, 40, 40), margin = 1, placesound = 'sounds/place.mp3', spinsound = 'sounds/spin.mp3'):

        self.bgcolor = bgcolor
        self.margin = margin
        self.cellcolors = cellcolors

        self.grid = Grid(20, 10, 40, self.cellcolors, margin = self.margin)
        self.blocks = [
                IBlock(40, self.cellcolors, self.margin),
                JBlock(40, self.cellcolors, self.margin),
                LBlock(40, self.cellcolors, self.margin),
                OBlock(40, self.cellcolors, self.margin),
                SBlock(40, self.cellcolors, self.margin),
                TBlock(40, self.cellcolors, self.margin),
                ZBlock(40, self.cellcolors, self.margin)
                ]

        self.current_block = self.getRandomBlock()
        self.next_block = self.getRandomBlock()
        self.saved_block = None
        self.gameover = False
        self.canswap = True
        self.score = 0
        self.placed = 0

        self.placesound = pygame.mixer.Sound(placesound)
        self.splinsound = pygame.mixer.Sound(spinsound)

    def getRandomBlock(self):
        if len(self.blocks) == 0:
            self.blocks = [
                IBlock(40, self.cellcolors, self.margin),
                JBlock(40, self.cellcolors, self.margin),
                LBlock(40, self.cellcolors, self.margin),
                OBlock(40, self.cellcolors, self.margin),
                SBlock(40, self.cellcolors, self.margin),
                TBlock(40, self.cellcolors, self.margin),
                ZBlock(40, self.cellcolors, self.margin)
                ]

        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def blockInside(self):
        tiles = self.current_block.getcellpos()
        for tile in tiles:
            if not self.grid.isInside(tile.row, tile.col):
                return False

        return True

    def blockCollide(self):
        tiles = self.current_block.getcellpos()
        for tile in tiles:
            if self.grid.isCollide(tile.row, tile.col):
                return True
        return False
    
    def lockBlock(self):
        tiles = self.current_block.getcellpos()
        for pos in tiles:
            self.grid.grid[pos.row][pos.col] = self.current_block.id

        self.current_block = self.next_block
        self.next_block = self.getRandomBlock()
        if self.blockCollide():
            self.gameover = True
            with open("data/scores.txt", 'a') as file:
                file.write(str(self.score) + '\n')

        cleared = self.grid.clean()
        self.score += cleared**2 * 500 + 500 
        self.canswap = True
        self.placed += 1
        self.placesound.play()

    def moveLeft(self):
        self.current_block.move(0, -1)
        if not self.blockInside() or self.blockCollide():
            self.current_block.move(0, 1)
            return False

        return True

    def moveRight(self):
        self.current_block.move(0, 1)
        if not self.blockInside() or self.blockCollide():
            self.current_block.move(0, -1)
            return False

        return True

    def moveDown(self):
        self.current_block.move(1, 0)
        if (not self.blockInside()) or self.blockCollide():
            self.current_block.move(-1, 0)
            self.lockBlock()
            return False

        return True

    def dashDown(self):
        while self.blockInside() and not self.blockCollide():
            self.current_block.move(1, 0)

        self.current_block.move(-1, 0)
        self.lockBlock()

    def rotate(self):
        self.current_block.rotate()
        if not self.blockInside() or self.blockCollide():
            self.current_block.rotate(clockwise = False)
            if not self.moveLeft():
                self.moveRight()
            self.current_block.rotate()

        self.splinsound.play()

    def swap(self):
        if self.canswap: 
            self.saved_block, self.current_block = self.current_block.new(), self.saved_block
            if self.current_block == None:
                self.current_block = self.next_block
                self.next_block = self.getRandomBlock()

        self.canswap = False

    def draw(self, surface):
        surface.fill(self.bgcolor)
        self.grid.surface.fill(self.bgcolor)
        self.grid.draw()
        self.current_block.draw(self.grid.surface)
        surface.blit(self.grid.surface, (20, 20))

    def reset(self):
        return type(self)(cellcolors = self.cellcolors, bgcolor = self.bgcolor, margin = self.margin)
