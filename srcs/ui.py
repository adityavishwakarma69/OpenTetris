import pygame
from srcs.blocks import *

class ScoreBoard:
    def __init__(self, game, bgcolor = (40, 40, 40), fgcolor = (255, 255, 255), scorecolor = (255, 255, 255)): 
        self.bgcolor = bgcolor
        self.scorecolor = scorecolor
        self.fgcolor = fgcolor
        self.surface = pygame.Surface((160, 80))
        self.font = pygame.font.Font(None, 40)
        self.text_surf = self.font.render("Score", True, self.fgcolor) 
        self.game = game 
        self.score_surf = self.font.render(str(self.game.score), True, self.scorecolor)
    def draw(self, surface):
        self.surface.fill(self.bgcolor)
        self.score_surf = self.font.render(str(self.game.score), True, self.scorecolor)
        textrect = self.surface.get_rect()
        self.surface.blit(self.text_surf, (33, 10))
        self.surface.blit(self.score_surf, (33, 40))
        surface.blit(self.surface, (500, 20))

    def reset(self, game):
        return type(self)(
                game,
                bgcolor = self.bgcolor,
                fgcolor = self.fgcolor,
                scorecolor = self.scorecolor,
                )

class NextBoard:
    def __init__(self, game, cellcolors, margin = 1, bgcolor = (40, 40, 40), fgcolor = (255, 255, 255)):
        self.bgcolor = bgcolor
        self.fgcolor = fgcolor
        self.margin = margin
        self.cellcolors = cellcolors
        self.surface = pygame.Surface((160, 240))
        self.font = pygame.font.Font(None, 40)
        self.text_surf = self.font.render("Next", True, self.fgcolor)
        self.game = game

    def draw(self, surface):
        self.surface.fill(self.bgcolor)
        self.surface.blit(self.text_surf, (45, 20))
        next_block = type(self.game.next_block)(30, self.cellcolors, margin = self.margin)
        if next_block.id == 4:
            next_block.offset = Pos(3, 1.5)
        elif next_block.id == 3:
            next_block.offset = Pos(3, 0.5)
        else:
            next_block.offset = Pos(3, 1)
        next_block.draw(self.surface)
        surface.blit(self.surface, (500, 120))

    def reset(self, game):
        return type(self)(
                game,
                cellcolors = self.cellcolors,
                margin = self.margin,
                bgcolor = self.bgcolor,
                fgcolor = self.fgcolor,
                )

class SavedBoard:
    def __init__(self, game, cellcolors, margin = 1, bgcolor = (40, 40, 40), fgcolor = (255, 255, 255)):
        self.bgcolor = bgcolor
        self.fgcolor = fgcolor
        self.cellcolors = cellcolors
        self.margin = margin
        self.surface = pygame.Surface((160, 240))
        self.font = pygame.font.Font(None, 40)
        self.text_surf = self.font.render("Saved", True, self.fgcolor)
        self.game = game

    def draw(self, surface):
        self.surface.fill(self.bgcolor)
        self.surface.blit(self.text_surf, (35, 20))
        if self.game.saved_block != None:
            saved_block = type(self.game.saved_block)(30, self.cellcolors, margin = self.margin)
            if saved_block.id == 4:
                saved_block.offset = Pos(3, 1.5)
            elif saved_block.id == 3:
                saved_block.offset = Pos(3, 0.5)
            else:
                saved_block.offset = Pos(3, 1)
            saved_block.draw(self.surface)
        surface.blit(self.surface, (500, 300))
    def reset(self, game):
        return type(self)(
                game,
                cellcolors = self.cellcolors,
                margin = self.margin,
                bgcolor = self.bgcolor,
                fgcolor = self.fgcolor,
                )

