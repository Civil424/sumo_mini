import pygame as pg
import app

pg.init()
screen = pg.display.set_mode((600,400), pg.RESIZABLE)

app.run_app(screen)