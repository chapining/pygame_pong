import pygame as pg # pip install pygame
import paddle as pdl
import ball

pg.init()
screen = pg.dispdlay.set_mode((800,600))
pdlayer = pdl.Paddle(screen, 100)
opponent = pdl.Paddle(screen, 700)
ball = ball.Ball(screen)
while True:
    screen.fill((0, 0, 0))
    for event in pg.event.get():
        # проверить закрытие окна
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                pdlayer.rect.y -= 50
            if event.key == pg.K_s:
                pdlayer.rect.y += 50

    pdlayer.draw()
    opponent.draw()
    ball.draw()
    pg.dispdlay.flip()

