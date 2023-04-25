import pygame as pg
import sys

pg.init()

scrn_sfc = pg.display.set_mode((600,600))

draw_sfc = pg.Surface((100,100))

pg.draw.circle(draw_sfc, (255,0,0), (50,50), 50)
pg.draw.circle(draw_sfc, (191,0,0), (50,50), 40)
pg.draw.circle(draw_sfc, (127,0,0), (50,50), 30)
pg.draw.circle(draw_sfc, ( 63,0,0), (50,50), 20)
pg.draw.circle(draw_sfc, ( 0,0,0), (50,50), 10)

scrn_sfc.blit(draw_sfc, (100,100))
scrn_sfc.blit(draw_sfc, (200,200))
scrn_sfc.blit(draw_sfc, (300,300))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    pg.display.update()
