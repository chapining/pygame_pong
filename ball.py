import pygame as pg 

class Ball:
    def __init__(self, screen):
        print("создан игрок")
        self.image = pg.Surface((10, 10))
        self.image.fill((255, 255, 255))
        self.screen = screen
        self.rect = self.image.get_rect()
        self.screen_rect = screen. get_rect()
        self.rect.centerx = self.screen_rect.centerx #hardcod , рассчитать от ширины окна
        self.rect.centery = self.screen_rect.centery

    def draw(self):
        self.screen.blit(self.image, self.rect)

