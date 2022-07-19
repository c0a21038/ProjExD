import random
import tkinter as tk
import pygame as pg
import sys

deck = [[1,2,3,4,5,6,7,8,9,10,11,12,13],
        [1,2,3,4,5,6,7,8,9,10,11,12,13],
        [1,2,3,4,5,6,7,8,9,10,11,12,13],
        [1,2,3,4,5,6,7,8,9,10,11,12,13]]

class Screen:
    def __init__(self, title, wh, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)     # Surface
        self.rct = self.sfc.get_rect()         # Rect
        self.bgi_sfc = pg.image.load(image)    # Surface
        self.bgi_rct = self.bgi_sfc.get_rect() # Rect

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)

class Card:
    def __init__(self, dh, hito):
        self.sfc1 = pg.image.load(f"./fig/トランプ/{dh[0][0]}/{dh[0][1]}.png")
        self.sfc1 = pg.transform.rotozoom(self.sfc1, 0, 0.15)                      
        self.rct1 = self.sfc1.get_rect()                       # Rect
        self.y = 0
        l = 0
        if hito == "P":
            self.y = 700
        else:
            self.y = 100
            l = 1
        self.rct1.center = (725, self.y)
        if l == 1:
            self.sfc2 = pg.image.load(f"./fig/トランプ/card_back.png")
            self.sfc2 = pg.transform.rotozoom(self.sfc2, 0, 0.27)
        else:
            self.sfc2 = pg.image.load(f"./fig/トランプ/{dh[1][0]}/{dh[1][1]}.png")
            self.sfc2 = pg.transform.rotozoom(self.sfc2, 0, 0.15)
        self.rct2 = self.sfc2.get_rect()
        self.rct2.center = (875,self.y)
        

    def blit(self, scr: Screen): # : Screenで型を設定することでscr以下が白くなくなる
        scr.sfc.blit(scr.sfc, scr.rct)
    
    def update(self,scr:Screen):
        scr.sfc.blit(self.sfc1,self.rct1)
        scr.sfc.blit(self.sfc2,self.rct2)
        self.blit(scr)


class ura:
    def __init__(self,image):
        self.sfc=pg.image.load(image)
        self.sfc=pg.transform.rotozoom(self.sfc, 0, 0.27)
        self.rct=self.sfc.get_rect()
        self.rct.center=(1400,450)
    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)


def main():
    global deck
    clock=pg.time.Clock()
    scr=Screen("black Jack",(1600,900),"./fig/トランプ/bg.jpg")
    dealer_hand = deal()
    player_hand = deal()
    ur=ura("./fig/トランプ/card_back.png")
    kkt1 = Card(player_hand, "P")
    kkt2 = Card(dealer_hand, "D")
    m=0
    while True:
        scr.blit()
        ur.blit(scr)
        for event in pg.event.get():
            if event.type==pg.QUIT:
                return
            if event.type==pg.KEYDOWN and event.key==pg.K_SPACE:
                m=1
        if m==1:
            kkt1.update(scr)
            kkt2.update(scr)
        
        pg.display.update()
        clock.tick(1000)




def deal():
    hand = []
    for i in range(2):
        for j in range(4):
            random.shuffle(deck[j])
        soot = random.randint(0,3)
        number = deck[soot].pop()
        hand.append([soot,number])
    return hand


def hit(hand):
    for j in range(4):
        random.shuffle(deck[j])
    soot = random.randint(0,3)
    number = deck[soot].pop()
    hand.append([soot,number])
    return hand
        

if __name__=="__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()