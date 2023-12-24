import pygame
from srcs.blocks import *


def getTextSurf(text, size, color, bgcolor = None, fontname = None, aal = True):
    font = pygame.font.Font(fontname, size)
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
    def __init__(self, game, bgcolor = (40, 40, 40), fgcolor = (255, 255, 255), scorecolor = (255, 255, 255)): 
        self.bgcolor = bgcolor
        self.scorecolor = scorecolor
        self.fgcolor = fgcolor
        self.surface = pygame.Surface((160, 80))
        self.text_surf = getTextSurf("Score", 40, self.fgcolor)
        self.game = game 
    
    def draw(self, surface):
        self.surface.fill(self.bgcolor)
        self.score_surf = getTextSurf(str(self.game.score), 40, self.scorecolor)
        score_rect = self.score_surf.get_rect()
        text_rect = self.text_surf.get_rect()
        text_rect.center = (80, 20)
        score_rect.center = (80, 60)
        self.surface.blit(self.text_surf, text_rect)
        self.surface.blit(self.score_surf, score_rect)
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
        self.text_surf = getTextSurf("Next", 40, self.fgcolor) 
        self.game = game

    def draw(self, surface):
        self.surface.fill(self.bgcolor)
        text_rect = self.text_surf.get_rect()
        text_rect.center = (80, 30)
        self.surface.blit(self.text_surf, text_rect)
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
        self.text_surf = getTextSurf("Saved", 40, self.fgcolor)
        self.game = game

    def draw(self, surface):
        self.surface.fill(self.bgcolor)
        text_rect = self.text_surf.get_rect()
        text_rect.center = (80, 30)
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
