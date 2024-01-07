#!/usr/bin/env python3

#Aditya Vishwakarma, hereby disclaims all copyright interest in this program (which deconstructs trees) written by Aditya Vishwakarma.

#signature of Aditya Vishwakarma

from srcs import *
import pygame
from pygame.locals import *
import platform
import sys

## Detecting Os for scaling purposes
kernalof = platform.system()
print("Kernal/OS -", kernalof)
if kernalof == 'Windows':   ## Making the process DPI Aware if Kernal is Win32
    import ctypes
    ctypes.windll.user32.SetProcessDPIAware()


## Reads the scores file and finds the highscore
## (TO DO) implement Cache
def getHighscore():
    try:
        with open("data/scores.txt", 'r') as file:
            scores = file.readlines()
            scores = [int(score) for score in scores] 

    except : return 0

    return max(scores)

pygame.init()
pygame.mixer.init()

settings = Settings()   ## Creating Settings object (TO DO : implement Calls methods)

infoObject = pygame.display.Info()  ## Detecting Resolution for scaling purposes
print(f"resolution: {infoObject.current_w}x{infoObject.current_h}") ## Stdout Detected Resolution
## Finding the scaling factors
print("scaletype :", settings.scaletype())
try:
        i = sys.argv.index('-r')
        scalex = scaley = float(sys.argv[i + 1])
except:
    if settings.scaletype() == 'auto':
        scalex = infoObject.current_w/1920
        scaley = infoObject.current_h/1080

    else:scalex = scaley = settings.scalefactor()


## Stdout scaling
if scaley == scalex and scalex == 1:
    print("Scaling is disabled")
else:
    print(f"Scaling is enabled (Logical) {round(scalex, 2)}i+{round(scaley, 2)}j")

screen = pygame.display.set_mode((int(700 * scalex), int(840 * scaley)))# Display Window
pygame.display.set_caption("Tetris")                                    #

event_handle = EventHandler()   ## Event object (TO DO : implement global mouse positioning)
pygame.mixer.music.load(settings.bgmusic()) ## Loading BG music in mixer

## gameplay loop ## game surface
def game():
    cellcolors = settings.getCellColors()
    margin = settings.margin()

    ## UI ELEMENTS
    game = Game(cellcolors,
                int(40 * scaley),
                margin = margin,
                placesound = settings.placesound(),
                spinsound = settings.spinsound(),
                bgcolor = settings.color('bg'),
                )
    
    
    scoreboard = ScoreBoard(game,
                            int(40 * scalex),
                            (int(160 * scalex), int(80 * scaley)),
                            (int(500 * scalex), int(20 * scaley)),
                            bgcolor = settings.color('scorebg'),
                            fgcolor = settings.color('scorefg'),
                            scorecolor = settings.color('score'),
                            )
    nextboard = NextBoard(game,
                          cellcolors,
                          int(30 * scalex),
                          int(40 * scalex),
                          (int(160 * scalex), int(240 * scaley)),
                          (int(500 * scalex), int(120 * scaley)),
                          margin = margin,
                          bgcolor = settings.color('nextbg'),
                          fgcolor = settings.color('nextfg'),
                          )
    savedboard = SavedBoard(game,
                            cellcolors,
                            int(30 * scalex),
                            int(40 * scalex),
                            (int(160 * scalex), int(240 * scaley)),
                            (int(500 * scalex), int(320 * scaley)),
                            margin = margin,
                            bgcolor = settings.color('savedbg'),
                            fgcolor = settings.color('savedfg'),
                           )

    diff = Diff(settings.getdiffs(), settings.getdiffthold())

    clock = pygame.time.Clock()
    fps = 60
    dt = 0 
    cont = -1  ## For pause menu (-1 : last frame was game , 0 : last frame was pause, 1: exit)
    ## getting keys
    keys = {
            'rotate' : globals()[settings.key('rotate')],
            'place' : globals()[settings.key('place')],
            'save' : globals()[settings.key('saveblock')],
            'pause' : globals()[settings.key('pause')],
            'right' : globals()[settings.key('moveright')],
            'left' : globals()[settings.key('moveleft')],
            'down' : globals()[settings.key('rotate')],
            }

    ## GAME LOOP STARTS
    while not (game.gameover or event_handle.shouldquit):
        event_handle.getEvents()    ##Getting Events

        
        if not pygame.mixer.music.get_busy():   ##Playing bgmusic <=> nothing is playing in mixer
            print("play")
            pygame.mixer.music.play(-1) 

        ## Checking for game events
        if event_handle.keydown == keys['rotate']:
            game.rotate()
        elif event_handle.keydown == keys['down']:
            game.moveDown()
        elif event_handle.keydown == keys['place']:
            game.dashDown()
        elif event_handle.keydown == keys['save']:
            game.swap()
        elif event_handle.keydown == keys['right']:
            game.moveRight()
        elif event_handle.keydown == keys['left']:
            game.moveLeft()
        elif event_handle.keydown == keys['pause']:
            cont = pause()


        udate = diff.update(game, dt)   ## falling of block 
        game.preview()                  ## preview block

        #drawing surfaces
        game.draw(screen)
        scoreboard.draw(screen)
        nextboard.draw(screen)
        savedboard.draw(screen)

        pygame.display.flip()   #Update screen

        ## Clock update based on pause menu
        if cont == 0:
            cont = -1
            dt = 0
            clock.tick(fps)
        elif cont == 1:
            return
        elif cont == -1:
            dt = clock.tick(fps)

## Menu loop
def menu():
    ## Buttons and Text surfaces
    title = TextButton("Tetris", int(120 * scalex), ((193, 139, 180), None))
    buttons = [
            TextButton("Play", int(80 * scalex), sec_colors = ((255, 180, 180), None)),
            TextButton("Options", int(80 * scalex), sec_colors = ((255, 180, 180), None)),
            TextButton("Quit", int(80 * scalex), sec_colors = ((255, 180, 180), None)),
            ]
    hover = 0
    highscore_text = getTextSurf("HIGHSCORE : " + str(getHighscore()), int(30 * scalex), (255, 255, 255))

    ## Main loop starts
    while not event_handle.shouldquit:
        event_handle.getEvents()    ## Updating Events
        if pygame.mixer.music.get_busy: ## Stoping the mixer if music is playing
            pygame.mixer.music.stop()

        ## Events and buttons
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

        #Drawing surfaces
        screen.fill(settings.color('bg'))

        for i in range(len(buttons)):
            if hover == i:buttons[i].hover = True
            else:buttons[i].hover = False
            buttons[i].draw(screen, (int(350 * scalex), int((i * 100 + 400) * scaley)))

        title.draw(screen, (int(350 * scalex), int(100 * scaley)))
        screen.blit(highscore_text, (0, 0))

        pygame.display.flip()   ##Updating the screen

def pause():    ## Same trend as menu
    title = TextButton("Tetris", int(120 * scalex), ((193, 139, 180), None))
    buttons = [
            TextButton("Continue", int(80 * scalex), sec_colors = ((255, 180, 180), None)),
            TextButton("Menu", int(80 * scalex), sec_colors = ((255, 180, 180), None)),
            TextButton("Quit", int(80 * scalex), sec_colors = ((255, 180, 180), None)),
            ]
    hover = 0
    pygame.mixer.music.pause()
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
            buttons[i].draw(screen, (int(350 * scalex), int((i * 100 + 400) * scaley)))

        title.draw(screen, (int(350 * scalex), int(100 * scaley)))

        pygame.display.flip()


if __name__ == "__main__":
    menu()  ## Menu the the parent loop
