import pygame
import sys
from draw import Draw, CELL_SIZE, CELL_NUMBER, WINDOW
from game import Game
from score import save_score

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW, WINDOW))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    draw = Draw(screen)

    screen_update = pygame.USEREVENT
    pygame.time.set_timer(screen_update, 100)

    game = Game(CELL_NUMBER, CELL_SIZE)
    state = "menu"

    while True:
        start_game = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_score(game.score)
                pygame.quit()
                sys.exit()

            if state in ("menu", "game over"):
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        start_game = True
                        state = "play"
                    elif event.key == pygame.K_ESCAPE:
                        state = "menu"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    start_game = True
                    state = "play"

            if state == "play":
                if event.type == screen_update:
                    game.update()
                    if game.game_over:
                        state = "game over"
                elif event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_UP, pygame.K_w):
                        game.snake.turn((0, -1))
                    elif event.key in (pygame.K_DOWN, pygame.K_s):
                        game.snake.turn((0, 1))
                    elif event.key in (pygame.K_LEFT, pygame.K_a):
                        game.snake.turn((-1, 0))
                    elif event.key in (pygame.K_RIGHT, pygame.K_d):
                        game.snake.turn((1, 0))


        if start_game:
            game = Game(CELL_NUMBER, CELL_SIZE)
            state = "play"
        if state == "menu":
            draw.start_screen()
        else:
            draw.game_board()
            game.draw(screen)
            draw.score(game.current_score, game.score)
            if state == "game over":
                draw.game_over_screen(game.current_score, game.score)
        pygame.display.update()
        clock.tick(60)


main()