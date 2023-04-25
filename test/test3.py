import pygame as pg
import sys
import random
import math

delta = {
        pg.K_UP: (0, -1),
        pg.K_DOWN: (0, +1),
        pg.K_LEFT: (-1, 0),
        pg.K_RIGHT: (+1, 0)
        }

def check_bound(scr_rct: pg.Rect, obj_rct: pg.Rect) -> tuple[bool, bool]:
    """
    オブジェクトが画面内か画面外かを判定し、真理値ダブルを返す関数
    引数１：画面surfaceのRect
    引数２：こうかとん、または、爆弾surfaceのRect
    戻り値：横方向、縦方向のはみだし判定結果。
    """
    yoko, tate = True, True
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = False
    if obj_rct.top < scr_rct.top or scr_rct.bottom < scr_rct.bottom:
        tate = False
    return yoko, tate


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)

    bb_img = pg.Surface((20, 20))
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)
    x, y = random.randint(0, 1600), random.randint(0, 900)
    screen.blit(bb_img, [x, y])
    bb_img.set_colorkey((0, 0, 0))
    bb_rct = bb_img.get_rect()
    bb_rct.center = x, y
    vx, vy = +1, +1
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 0

        tmr += 1

        key_lst = pg.key.get_pressed()
        for k, mv in delta.items():
            if key_lst[k]:
                kk_rct.move_ip(mv)
                # 矢印キーに合わせてkk_imgの向きを変更
                angle = math.degrees(math.atan2(mv[1], mv[0])) - 90
                kk_img = pg.transform.rotozoom(pg.image.load("ex02/fig/3.png"), angle, 2.0)

        if check_bound(screen.get_rect(), kk_rct