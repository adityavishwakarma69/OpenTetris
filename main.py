from srcs import *
import pygame
from pygame.locals import *

pygame.init()
pygame.mixer.init()

def main():
    settings = Settings()
    cellcolors = settings.getCellColors()
    margin = settings.margin()

    game = Game(cellcolors, margin = margin)
    
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

    pygame.mixer.music.load('sounds/bg.mp3') 

    screen = pygame.display.set_mode((700, 840))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    fps = 60
    dt = 0
    timer = Timer(500)

    while True:
        if game.gameover:
            pygame.mixer.music.stop()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        game = game.reset()
                        scoreboard = scoreboard.reset(game)
                        nextboard = nextboard.reset(game)
                        savedboard = savedboard.reset(game)

            screen.fill((40, 40, 40))
            screen.blit(game_over, (240, 400))
            screen.blit(scoreboard.score_surf, (330, 450))
            pygame.display.flip()
            clock.tick(fps)
        else:
            if not pygame.mixer.music.get_busy():
                print("play")
                pygame.mixer.music.play(-1)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

                elif event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        game.moveLeft()
                    elif event.key == K_RIGHT:
                        game.moveRight()
                    elif event.key == K_DOWN:
                        game.moveDown()
                    elif event.key == K_UP:
                        game.rotate()
                    elif event.key == K_RETURN:
                        game.dashDown()
                    elif event.key == K_c:
                        game.swap()



            if timer.timeout(dt):
                game.moveDown()

            timer.threshold = 50 + 500 / (game.placed/40 + 1)

            #draw
            game.draw(screen)
            scoreboard.draw(screen)
            nextboard.draw(screen)
            savedboard.draw(screen)
            

            pygame.display.flip()
            dt = clock.tick(fps)


if __name__ == "__main__":
    main()
