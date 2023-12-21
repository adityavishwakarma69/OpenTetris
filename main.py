from srcs import *
import pygame
from pygame.locals import *

pygame.init()
pygame.mixer.init()

def main():
    settings = Settings()
    cellcolors = settings.getCellColors()
    margin = settings.margin()

    game = Game(cellcolors,
                margin = margin,
                placesound = settings.placesound(),
                spinsound = settings.spinsound(),
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

    pygame.mixer.music.load(settings.bgmusic()) 

    screen = pygame.display.set_mode((700, 840))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    fps = 60
    dt = 0 

    event_handle = EventHandler()

    while not event_handle.shouldquit:
        event_handle.getEvents()
        if game.gameover:

            pygame.mixer.music.stop()

            if event_handle.keydown == K_RETURN:
                game = game.reset()
                scoreboard = scoreboard.reset(game)
                nextboard = nextboard.reset(game)
                savedboard = savedboard.reset(game) 
                diff = Diff(settings.getdiffs(), settings.getdiffthold())

            screen.fill((40, 40, 40))
            screen.blit(game_over, (240, 400))
            screen.blit(scoreboard.score_surf, (330, 450))
            pygame.display.flip()
            clock.tick(fps)
        else:
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
            dt = clock.tick(fps)


if __name__ == "__main__":
    main()
