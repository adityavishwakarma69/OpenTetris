#Aditya Vishwakarma, hereby disclaims all copyright interest in this program (which deconstructs trees) written by Aditya Vishwakarma.

#signature of Aditya Vishwakarma


import pygame
from srcs.blocks import *


def getTextSurf(text, size, color, bgcolor = None, fontname = None, aal = True):
    font = pygame.font.SysFont(fontname, size)
    surf = font.render(text, aal, color, bgcolor)
    return surf

class TextButton:
    def __init__(self, text, size,
                 pri_colors = ((255, 255, 255), None),
                 sec_colors = ((100, 100, 100), None)):
        
        self.hover = False
        self.text = text
        self.size = size
        self.pcolor = pri_colors
        self.scolor = sec_colors
    
    def draw(self, surface, pos = (0, 0)):
        if self.hover:
            self.text_surf = getTextSurf(self.text,
                                         self.size,
                                         self.scolor[0],
                                         self.scolor[1])
        else:
            self.text_surf = getTextSurf(self.text,
                                         self.size,
                                         self.pcolor[0],
                                         self.pcolor[1])

        text_rect = self.text_surf.get_rect()
        text_rect.center = pos

        surface.blit(self.text_surf, text_rect)

    def toggle_select(self):
        self.hover = True

class ScoreBoard:
    def __init__(self, game, font_size, size, pos, bgcolor = (40, 40, 40), fgcolor = (255, 255, 255), scorecolor = (255, 255, 255)): 
        self.bgcolor = bgcolor
        self.scorecolor = scorecolor
        self.fgcolor = fgcolor
        self.size = size
        self.pos = pos
        self.surface = pygame.Surface(self.size)
        self.font_size = font_size
        self.text_surf = getTextSurf("Score", self.font_size, self.fgcolor)
        self.game = game
    
    def draw(self, surface):
        self.surface.fill(self.bgcolor)
        self.score_surf = getTextSurf(str(self.game.score), self.font_size, self.scorecolor)
        score_rect = self.score_surf.get_rect()
        text_rect = self.text_surf.get_rect()
        text_rect.center = (self.size[0]//2, self.size[1]//4)
        score_rect.center = (self.size[0]//2, 3 * (self.size[1]//4))
        self.surface.blit(self.text_surf, text_rect)
        self.surface.blit(self.score_surf, score_rect)
        surface.blit(self.surface, self.pos)

    def reset(self, game):
        return type(self)(
                game,
                bgcolor = self.bgcolor,
                fgcolor = self.fgcolor,
                scorecolor = self.scorecolor,
                )

class NextBoard:
    def __init__(self, game, cellcolors, cellsize, font_size, size, pos, margin = 1, bgcolor = (40, 40, 40), fgcolor = (255, 255, 255)):
        self.font_size = font_size
        self.size = size 
        self.pos = pos
        self.bgcolor = bgcolor
        self.fgcolor = fgcolor
        self.cellsize = cellsize
        self.margin = margin
        self.cellcolors = cellcolors
        self.surface = pygame.Surface(self.size)
        self.text_surf = getTextSurf("Next", self.font_size, self.fgcolor) 
        self.game = game

    def draw(self, surface):
        self.surface.fill(self.bgcolor)
        text_rect = self.text_surf.get_rect()
        text_rect.center = (self.size[0] / 2, self.size[1] / 8)
        self.surface.blit(self.text_surf, text_rect)
        next_block = type(self.game.next_block)(self.cellsize, self.cellcolors, margin = self.margin)
        if next_block.id == 4:
            next_block.offset = Pos(3, 1.5)
        elif next_block.id == 3:
            next_block.offset = Pos(3, 0.5)
        else:
            next_block.offset = Pos(3, 1)
        next_block.draw(self.surface)
        surface.blit(self.surface, self.pos)

    def reset(self, game):
        return type(self)(
                game,
                cellcolors = self.cellcolors,
                margin = self.margin,
                bgcolor = self.bgcolor,
                fgcolor = self.fgcolor,
                )

class SavedBoard:
    def __init__(self, game, cellcolors, cellsize, font_size, size, pos, margin = 1, bgcolor = (40, 40, 40), fgcolor = (255, 255, 255)): 
        self.font_size = font_size
        self.size = size 
        self.pos = pos
        self.cellsize = cellsize
        self.bgcolor = bgcolor
        self.fgcolor = fgcolor
        self.cellcolors = cellcolors
        self.margin = margin
        self.surface = pygame.Surface(self.size)
        self.text_surf = getTextSurf("Saved", self.font_size, self.fgcolor)
        self.game = game

    def draw(self, surface):
        self.surface.fill(self.bgcolor)
        text_rect = self.text_surf.get_rect()
        text_rect.center = (self.size[0] / 2, self.size[1] / 8)
        self.surface.blit(self.text_surf, text_rect)
        if self.game.saved_block != None:
            saved_block = type(self.game.saved_block)(self.cellsize, self.cellcolors, margin = self.margin)
            if saved_block.id == 4:
                saved_block.offset = Pos(3, 1.5)
            elif saved_block.id == 3:
                saved_block.offset = Pos(3, 0.5)
            else:
                saved_block.offset = Pos(3, 1)
            saved_block.draw(self.surface)
        surface.blit(self.surface, self.pos)
    def reset(self, game):
        return type(self)(
                game,
                cellcolors = self.cellcolors,
                margin = self.margin,
                bgcolor = self.bgcolor,
                fgcolor = self.fgcolor,
                )
