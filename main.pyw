#!/usr/bin/env python3

from srcs import *
import pygame
from pygame.locals import *

def getHighscore():
    try:
        with open("data/scores.txt", 'r') as file:
            scores = file.readlines()
            scores = [int(score) for score in scores] 

    except : return 0

    return max(scores)

pygame.init()
pygame.mixer.init()
settings = Settings()
screen = pygame.display.set_mode((700, 840), pygame.SCALED)
pygame.display.set_caption("Tetris")
event_handle = EventHandler()
pygame.mixer.music.load(settings.bgmusic())
def game():
    cellcolors = settings.getCellColors()
    margin = settings.margin()

    game = Game(cellcolors,
                margin = margin,
                placesound = settings.placesound(),
                spinsound = settings.spinsound(),
                bgcolor = settings.color('bg'),
                )
    
    font = pygame.font.Font(None, 60)
    game_over = font.render("GAMEOVER!", True, (255, 168, 184))
    
    scoreboard = ScoreBoard(game,
                            bgcolor = settings.color('scorebg'),
                            fgcolor = settings.color('scorefg'),
                            scorecolor = settings.color('score'),
                            )
    nextboard = NextBoard(game,
                          cellcolors,
                          margin = margin,
                          bgcolor = settings.color('nextbg'),
                          fgcolor = settings.color('nextfg'),
                          )
    savedboard = SavedBoard(game,
                           cellcolors,
                           margin = margin,
                           bgcolor = settings.color('savedbg'),
                           fgcolor = settings.color('savedfg'),
                           )

    diff = Diff(settings.getdiffs(), settings.getdiffthold())

 
    clock = pygame.time.Clock()
    fps = 60
    dt = 0 
    cont = -1
    while not (game.gameover or event_handle.shouldquit):
        event_handle.getEvents()

        
        if not pygame.mixer.music.get_busy():
            print("play")
            pygame.mixer.music.play(-1) 

        
        if event_handle.keydown == K_UP:
            game.rotate()
        elif event_handle.keydown == K_DOWN:
            game.moveDown()
        elif event_handle.keydown == K_RETURN:
            game.dashDown()
        elif event_handle.keydown == K_c:
            game.swap()
        elif event_handle.keydown == K_RIGHT:
            game.moveRight()
        elif event_handle.keydown == K_LEFT:
            game.moveLeft()
        elif event_handle.keydown == K_ESCAPE:
            cont = pause()
        

        if K_z in event_handle.pressed:
            game.moveLeft()
        if K_x in event_handle.pressed:
            game.moveRight() 

        diff.update(game, dt)
        
        #draw
        game.draw(screen)
        scoreboard.draw(screen)
        nextboard.draw(screen)
        savedboard.draw(screen)
        

        pygame.display.flip()
        if cont == 0:
            cont = -1
            dt = 0
            clock.tick(fps)
        elif cont == 1:
            return
        elif cont == -1:
            dt = clock.tick(fps)

def menu():
    title = TextButton("Tetris", 120, ((193, 139, 180), None))
    buttons = [
            TextButton("Play", 80, sec_colors = ((255, 180, 180), None)),
            TextButton("Options", 80, sec_colors = ((255, 180, 180), None)),
            TextButton("Quit", 80, sec_colors = ((255, 180, 180), None)),
            ]
    hover = 0
    highscore_text = getTextSurf("HIGHSCORE : " + str(getHighscore()), 30, (255, 255, 255))
    while not event_handle.shouldquit:
        event_handle.getEvents()
        if pygame.mixer.music.get_busy:
            pygame.mixer.music.stop()
        if event_handle.keydown == K_DOWN:
            hover += 1
            if hover == len(buttons):
                hover = 0
        elif event_handle.keydown == K_UP:
            hover -= 1
            if hover < 0:
                hover = len(buttons) - 1
        elif event_handle.keydown == K_RETURN:
            if hover == 0:
                game()
            elif hover == 1:
                print("Not Implemented")
            elif hover == 2:
                event_handle.shouldquit = True

        screen.fill(settings.color('bg'))

        for i in range(len(buttons)):
            if hover == i:buttons[i].hover = True
            else:buttons[i].hover = False
            buttons[i].draw(screen, (350, i * 100 + 400))

        title.draw(screen, (350, 100))
        screen.blit(highscore_text, (0, 0))

        pygame.display.flip()

def pause():
    title = TextButton("Tetris", 120, ((193, 139, 180), None))
    buttons = [
            TextButton("Continue", 80, sec_colors = ((255, 180, 180), None)),
            TextButton("Menu", 80, sec_colors = ((255, 180, 180), None)),
            TextButton("Quit", 80, sec_colors = ((255, 180, 180), None)),
            ]
    hover = 0
    while not event_handle.shouldquit:
        event_handle.getEvents()
        if event_handle.keydown == K_DOWN:
            hover += 1
            if hover == len(buttons):
                hover = 0
        elif event_handle.keydown == K_UP:
            hover -= 1
            if hover < 0:
                hover = len(buttons) - 1
        elif event_handle.keydown == K_RETURN:
            if hover == 0:
                return 0
            elif hover == 1:
                return 1
            elif hover == 2:
                pygame.quit()
                exit()

        screen.fill(settings.color('bg'))

        for i in range(len(buttons)):
            if hover == i:buttons[i].hover = True
            else:buttons[i].hover = False
            buttons[i].draw(screen, (350, i * 100 + 400))

        title.draw(screen, (350, 100))

        pygame.display.flip()


if __name__ == "__main__":
    menu()
