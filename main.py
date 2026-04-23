import pygame as pg
import pygame.event

pg.init()
pg.display.set_mode((600,400))
run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
pygame.quit()