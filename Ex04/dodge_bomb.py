import pygame as pg
import sys
import random
import tkinter as tk
import tkinter.messagebox as tkm
import math 

def main():
    clock = pg.time.Clock()

    # 経過時間のウィンドウを表示する際に生成される空のウィンドウを削除
    root = tk.Tk()  
    root.withdraw()
    count = 0
    

    # 練習１
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600, 900)) # Surface
    screen_rct = screen_sfc.get_rect()            # Rect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")    # Surface
    bgimg_rct = bgimg_sfc.get_rect()              # Rect
    screen_sfc.blit(bgimg_sfc, bgimg_rct)

    # 練習３
    kkimg_sfc = pg.image.load("fig/6.png")               # Surface
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0) # Surface
    kkimg_rct = kkimg_sfc.get_rect()                     # Rect
    kkimg_rct.center = 900, 400

    # 練習５
    bmimg_sfc = pg.Surface((20, 20)) # Surface
    bmimg_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bmimg_sfc, (255, 0, 0), (10, 10), 10)
    bmimg_rct = bmimg_sfc.get_rect() # Rect
    bmimg_rct.centerx = random.randint(0, screen_rct.width)
    bmimg_rct.centery = random.randint(0, screen_rct.height)
    
    # 練習６
    vx, vy = +1, +1
    
    
    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct)
        
        time = math.floor(pg.time.get_ticks()/1000)          # pygame.initが実行されてからの経過時間 
        fonto = pg.font.Font(None, 80)                       # フォント設定用のオブジェクト
        txt = fonto.render(f"time:{time}", True, (0 , 0, 0)) # 黒色で経過時間を書いたSurfaceを生成
        screen_sfc.blit(txt, (100, 100))                     # 経過時間を書いたSurfaceを画面Surfaceに張り付ける

        # 練習２
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        # 練習４
        '''
        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP] == True: kkimg_rct.centery -= 1
        if key_states[pg.K_DOWN] == True: kkimg_rct.centery += 1
        if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx += 1
        if key_states[pg.K_LEFT] == True: kkimg_rct.centerx -= 1
        
        if check_bound(kkimg_rct, screen_rct) != (1, 1): #領域外だったら
            if key_states[pg.K_UP] == True: kkimg_rct.centery += 1
            if key_states[pg.K_DOWN] == True: kkimg_rct.centery -= 1
            if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx -= 1
            if key_states[pg.K_LEFT] == True: kkimg_rct.centerx += 1
        '''
        # マウスカーソルに合わせてこうかとんが動く
        kx, ky = pg.mouse.get_pos()
        kkimg_rct.centery = ky
        kkimg_rct.centerx = kx
        
        
        screen_sfc.blit(kkimg_sfc, kkimg_rct)
        

        # 練習６
        bmimg_rct.move_ip(vx, vy)
        # 練習５
        screen_sfc.blit(bmimg_sfc, bmimg_rct)
        # 練習７
        yoko, tate = check_bound(bmimg_rct, screen_rct)
        vx *= yoko
        vy *= tate

        count += 1
        if count%1500 == 0:
            if vx < 5.0:
                vx *= 1.3
                vy *= 1.3

                

        # 練習８
        if kkimg_rct.colliderect(bmimg_rct):
            tkm.showinfo("GAMEOVER", f"{time}秒生存！") #経過した時間をウィンドウで表示
            return

        pg.display.update()
        clock.tick(1000)

# 練習７
def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right < rct.right: yoko = -1 # 領域外
    if rct.top < scr_rct.top or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate
    

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
    