import tkinter as tk
import maze_maker as mm
import tkinter.messagebox as tkm
from random import randint as rdi

def key_down(event):
    global key
    key = event.keysym
    
    
def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, mx, my
    if key == "Up" and maze_bg[my-1][mx] == 0:
        my -= 1
    if key == "Down" and maze_bg[my+1][mx] == 0:
        my += 1
    if key == "Left" and maze_bg[my][mx-1] == 0:
        mx -= 1
    if key == "Right" and maze_bg[my][mx+1] == 0:
        mx += 1
    cx, cy = mx*100 + 50, my*100 + 50
    canvas.coords("koukaton", cx, cy)
    
    if mx == gx and my == gy: # ゴールに到達した場合
        tkm.showinfo("ゴール！！！", "おめでとう！！")
        exit() # ゲームを終了
    maze.after(120, main_proc)
    


def make_goal(): #3方向が壁に囲まれた床にゴールを作成する関数
    global gx, gy
    while True: # 3方向が壁に囲まれた床をゴールとするまでの間
        gx = rdi(1,13) # ゴールの場所をランダムに設定
        gy = rdi(1,7)
        
        if maze_bg[gy][gx] == 0: # 設定されたゴールの場所が床であるならば
            if maze_bg[gy+1][gx] == 1 and maze_bg[gy][gx-1] == 1 and maze_bg[gy][gx+1] == 1: # 下以外が壁だったら
                canvas.create_rectangle(gx*100, gy*100, gx*100+100, gy*100+100, 
                                        fill = "orange") # ゴールの場所をオレンジに
                break
            
            elif maze_bg[gy-1][gx] == 1 and maze_bg[gy][gx-1] == 1 and maze_bg[gy][gx+1] == 1: # 上以外が壁だったら
                canvas.create_rectangle(gx*100, gy*100, gx*100+100, gy*100+100, 
                                        fill = "orange") # ゴールの場所をオレンジに
                break
            
            elif maze_bg[gy+1][gx] == 1 and maze_bg[gy-1][gx] == 1 and maze_bg[gy][gx+1] == 1: # 左以外が壁だったら
                canvas.create_rectangle(gx*100, gy*100, gx*100+100, gy*100+100, 
                                        fill = "orange") # ゴールの場所をオレンジに
                break
            
            elif maze_bg[gy+1][gx] == 1 and maze_bg[gy-1][gx] == 1 and maze_bg[gy][gx-1] == 1: # 右以外が壁だったら
                canvas.create_rectangle(gx*100, gy*100, gx*100+100, gy*100+100, 
                                        fill = "orange") # ゴールの場所をオレンジに
                break

            else: # 壁が３方向にない場合
                continue # 最初に戻る    
        

if __name__ == "__main__":
    maze = tk.Tk()
    maze.title("迷えるこうかとん")
    #maze.geometry("1500x900")
    canvas = tk.Canvas(maze,
                      width = 1500,
                      height = 900,
                      bg = "black")
    canvas.pack()
    maze_bg = mm.make_maze(15, 9) # 1:壁/0:床を表す二次元リスト
    mm.show_maze(canvas, maze_bg) # 迷路を描画する
    make_goal()


    koukaton = tk.PhotoImage(file = "fig/4.png")
    mx, my = 1, 1
    cx, cy = mx*100 + 50, my*100 + 50
    canvas.create_image(cx,
                       cy,
                       image = koukaton,
                       tag = "koukaton"
                       )
    
    key = ""
    maze.bind("<KeyPress>", key_down)
    maze.bind("<KeyRelease>", key_up)
    main_proc()

    maze.mainloop()