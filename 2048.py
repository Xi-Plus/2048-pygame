# 程式名稱：animation-01.py
import pygame
import os
from game import Game

pygame.init()

WIN_WIDTH, WIN_HEIGHT = 490, 600
FRAME_PER_SECONDS = 20

win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('2048')

screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
screen.fill((250, 248, 239))

clock = pygame.time.Clock()

BLOCK_COLOR = {
    '': (201, 191, 180),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (237, 224, 200),
    16: (237, 224, 200),
    32: (237, 224, 200),
    64: (237, 224, 200),
    128: (237, 224, 200),
    256: (237, 224, 200),
    512: (237, 224, 200),
    1024: (237, 224, 200),
}

run = True

game = Game()
game.random_lay()
game.random_lay()

while run:
    clock.tick(FRAME_PER_SECONDS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            moved = False
            if event.key == pygame.K_LEFT:
                moved = game.move_left()
            if event.key == pygame.K_RIGHT:
                moved = game.move_right()
            if event.key == pygame.K_UP:
                moved = game.move_up()
            if event.key == pygame.K_DOWN:
                moved = game.move_down()
            if moved:
                game.random_lay()

    myfont = pygame.font.Font(None, 60)
    textImage1 = myfont.render('2048', True, (119, 110, 101))
    screen.blit(textImage1, (50, 20))

    font2 = pygame.font.Font('fonts/msjh.ttf', 24)
    textImage2 = font2.render('使用上下左右鍵控制', True, (119, 110, 101))
    screen.blit(textImage2, (50, 60))

    # score
    pygame.draw.rect(screen, (187, 173, 160), (300, 30, 70, 50), 0)

    myfont = pygame.font.Font(None, 24)
    textImage1 = myfont.render('SCORE', True, (255, 255, 255))
    screen.blit(textImage1, (305, 32))

    pygame.draw.rect(screen, (187, 173, 160), (20, 100, 450, 450), 0)

    for i in range(4):
        for j in range(4):
            if game.board[i, j] is None:
                pygame.draw.rect(screen, BLOCK_COLOR[''], (30 + j * 110, 110 + i * 110, 100, 100), 0)
            else:
                pygame.draw.rect(screen, BLOCK_COLOR[game.board[i, j].val], (30 + j * 110, 110 + i * 110, 100, 100), 0)

                myfont = pygame.font.Font(None, 96)
                textImage1 = myfont.render(str(game.board[i, j].val), True, (119, 110, 101))
                screen.blit(textImage1, (
                    30 + j * 110 + textImage1.get_width() // 2,
                    110 + i * 110 + textImage1.get_height() // 2,
                    100, 100))
    pygame.display.update()

pygame.quit()
