import pygame as pg
import sys

pg.init()

size = (640, 480)
screen = pg.display.set_mode(size)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                sys.exit()