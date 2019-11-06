# 程式名稱：animation-01.py
import pygame
import os
from game import Game

pygame.mixer.pre_init(44100, 16, 2, 2048)
pygame.mixer.init()
pygame.init()

soundObj1 = pygame.mixer.Sound('sounds/sound11.ogg')
soundObj2 = pygame.mixer.Sound('sounds/sound111.ogg')
soundObj3 = pygame.mixer.Sound('sounds/game-over-arcade.ogg')

WIN_WIDTH, WIN_HEIGHT = 490, 600
FRAME_PER_SECONDS = 20

win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('2048')

screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
screen.fill((250, 248, 239))

clock = pygame.time.Clock()


def show_text(text, font, size, color, posX, posY, center=False):
    myfont = pygame.font.Font(None if font is None else 'fonts/{}'.format(font), size)
    TextSurf = myfont.render(text, True, color)
    if center:
        TextRect = TextSurf.get_rect()
        TextRect.center = (posX, posY)
        screen.blit(TextSurf, TextRect)
    else:
        screen.blit(TextSurf, (posX, posY))


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
score = 0
gameover = False

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
                moved, temp_score = game.move_left()
            if event.key == pygame.K_RIGHT:
                moved, temp_score = game.move_right()
            if event.key == pygame.K_UP:
                moved, temp_score = game.move_up()
            if event.key == pygame.K_DOWN:
                moved, temp_score = game.move_down()
            if moved:
                game.random_lay()
                soundObj1.play()
                if temp_score:
                    score += temp_score
                    soundObj2.play()

            if gameover and event.key == pygame.K_RETURN:
                game = Game()
                game.random_lay()
                game.random_lay()
                gameover = False
                score = 0

    if not gameover and game.check_gameover():
        gameover = True
        soundObj3.play()

    show_text('2048', None, 60, (119, 110, 101), 50, 20)

    show_text('使用上下左右鍵控制', 'NotoSansTC-Regular.otf', 24, (119, 110, 101), 50, 60)

    # score
    pygame.draw.rect(screen, (187, 173, 160), (300, 30, 70, 50), 0)

    show_text('SCORE', None, 24, (238, 228, 218), 335, 40, center=True)

    show_text(str(score), None, 32, (255, 255, 255), 335, 65, center=True)

    pygame.draw.rect(screen, (187, 173, 160), (20, 100, 450, 450), 0)

    for i in range(4):
        for j in range(4):
            if game.board[i, j] is None:
                pygame.draw.rect(screen, BLOCK_COLOR[''], (30 + j * 110, 110 + i * 110, 100, 100), 0)
            else:
                pygame.draw.rect(screen, BLOCK_COLOR[game.board[i, j].val], (30 + j * 110, 110 + i * 110, 100, 100), 0)

                show_text(str(game.board[i, j].val), None, 72, (119, 110, 101),
                          30 + j * 110 + 50,
                          110 + i * 110 + 50,
                          center=True)

    if gameover:
        show_text('GAME OVER', None, 80, (255, 0, 0), 245, 240, center=True)

        show_text('按Enter開始新局', 'NotoSansTC-Regular.otf', 48, (255, 0, 0), 245, 300, center=True)

    pygame.display.update()

pygame.quit()
