import pygame as pg
import sys
import random

delta = {
        pg.K_UP: (0, -1),   # 上キーを押した時の反応
        pg.K_DOWN: (0, +1), # 下キーを押した時の反応
        pg.K_LEFT: (-1, 0), # 左キーを押した時の反応
        pg.K_RIGHT: (+1, 0) # 右キーを押した時の反応
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
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = False
    return yoko, tate



def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")    
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)

    kk_img_ks = pg.transform.flip(kk_img, True, True)
    kk_mk = {
            (0, -1):pg.transform.rotozoom(kk_img, 0,  1),
            (-1,-1):pg.transform.rotozoom(kk_img, 45, 1),
            (-1, 0):pg.transform.rotozoom(kk_img, 90, 1),
            (-1,+1):pg.transform.rotozoom(kk_img, 135,1),
            (0, +1):pg.transform.rotozoom(kk_img,180, 1),
            (+1,+1):pg.transform.rotozoom(kk_img,180,1),
            (+1,0):pg.transform.rotozoom(kk_img,225,1),
            (+1,-1):pg.transform.rotozoom(kk_img,270,1),
            } # 演習課題未完
    

    bb_img = pg.Surface((20, 20))
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400 # kk_imageの最初に現れる座標
    pg.draw.circle(bb_img, (255, 0, 0), (10,10), 10)
    x, y = random.randint(0, 1600), random.randint(0, 900) # x座標、y座標をランダムに表示させるためのコード
    screen.blit(bb_img, [x, y]) # bb_imageをランダムに開始するコード
    bb_img.set_colorkey((0, 0, 0))
    bb_rct = bb_img.get_rect()
    bb_rct.center = x, y
    vx, vy = +1, +1 # こうかとんの移動速度
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0
            
        tmr += 1
        key_lst = pg.key.get_pressed()
        for k, mv in delta.items():
            if key_lst[k]:
                kk_rct.move_ip(mv)   # 移動キーを押したときの移動      

        if check_bound(screen.get_rect(), kk_rct) != (True, True):
            for k, mv in delta.items():
                if key_lst[k]:
                    kk_rct.move_ip(-mv[0], -mv[1]) # こうかとんが範囲外に出ないようにする

        
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)
        bb_rct.move_ip(vx, vy)
        yoko, tate = check_bound(screen.get_rect(), bb_rct)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1
        screen.blit(bb_img, bb_rct)

        if kk_rct.colliderect(bb_rct): 
            return
        

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()