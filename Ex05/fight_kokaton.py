import pygame as pg
import sys
import random
import tkinter as tk
import tkinter.messagebox as tkm
import math 


class Screen:
    def __init__(self, title, wh, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)     # Surface
        self.rct = self.sfc.get_rect()         # Rect
        self.bgi_sfc = pg.image.load(image)    # Surface
        self.bgi_rct = self.bgi_sfc.get_rect() # Rect

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:
    def __init__(self, image, size, xy):
        self.sfc = pg.image.load(image)                      # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()                       # Rect
        self.rct.center = xy

    def blit(self, scr: Screen): # : Screenで型を設定することでscr以下が白くなくなる
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr: Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]: 
            self.rct.centery -= 1
        if key_states[pg.K_DOWN]:
            self.rct.centery += 1
        if key_states[pg.K_LEFT]:
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT]:
            self.rct.centerx += 1
        # 練習7
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]:
                self.rct.centery += 1
            if key_states[pg.K_DOWN]:
                self.rct.centery -= 1
            if key_states[pg.K_LEFT]:
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT]:
                self.rct.centerx -= 1
        self.blit(scr)


class Bomb:
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy # 練習6
    
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        # 練習6
        self.rct.move_ip(self.vx, self.vy)
        # 練習7
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        # 練習5
        self.blit(scr)


class Time:
    def __init__(self, size, color, xy):
        self.time = math.floor(pg.time.get_ticks()/1000)               # pygame.initが実行されてからの経過時間 
        self.fonto = pg.font.Font(None, size)                          # フォント設定用のオブジェクト
        self.sfc = self.fonto.render(f"time:{self.time}", True, color) # 黒色で経過時間を書いたSurfaceを生成
        self.rct = self.sfc.get_rect()                                 # Rect
        self.rct.center = xy
    
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct) # 経過時間を書いたSurfaceを画面Surfaceに張り付ける

    def gameover(self):
        self.root = tk.Tk()  
        self.root.withdraw()
        tkm.showinfo("GAMEOVER", f"{self.time}秒生存！") #経過した時間をウィンドウで表示

class NewBomb: # 時間ごとに爆弾が増える機能（実装途中)
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy # 練習6
    
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen, t: Time):
        # 練習6
        self.rct.move_ip(self.vx, self.vy)
        # 練習7
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        # 練習5
        self.blit(scr)


class Beam: # こうかとんからビームを出す（実装途中）
    def __init__(self, color, size, chr: Bird):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = chr.rct.centerx
        self.rct.centery = chr.rct.centery
    
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr: Screen):
        self.rct.centerx += 10
        self.blit(scr)


def main():
    clock = pg.time.Clock()
    scr = Screen("逃げろ！こうかとん", (1600, 900), "fig/pg_bg.jpg")
    kkt = Bird("fig/6.png", 2.0, (900, 400))
    bkd = Bomb((255, 0, 0), 10, (+1, +1), scr)
    nbkd = NewBomb((255, 255, 0), 10, (+1, +1), scr)
    beam = None
    while True:
        scr.blit()
        time = Time(80, (0 ,0 , 0), (100, 100))
        time.blit(scr)
        # 練習2
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                beam = Beam((255, 0, 255), 20, kkt)
        kkt.update(scr)
        bkd.update(scr)
        nbkd.update(scr, time)
        if beam:
            beam.update(scr)
        if kkt.rct.colliderect(bkd.rct) or kkt.rct.colliderect(nbkd.rct):
            time.gameover()
            return
        pg.display.update()
        clock.tick(1000)



def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()