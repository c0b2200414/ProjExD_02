import pygame as pg
import sys

pg.init()

size = (640, 480)
screen = pg.display.set_mode(size)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pg.mouse.get_pos()
                pg.draw.circle(screen, (0, 255, 0), pos, 10)
    pg.display.flip()