import tkinter as tk
import maze_maker as mm

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
    maze.after(120, main_proc)
    

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