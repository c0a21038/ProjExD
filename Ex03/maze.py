import tkinter as tk

def key_down(event):
    global key
    key = event.keysym
    
    
def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy
    if key == "Up":
        cy -= 20
    if key == "Down":
        cy += 20
    if key == "Left":
        cx -= 20
    if key == "Right":
        cx += 20
    canvas.coords("koukaton", cx, cy)
    maze.after(100, main_proc)
    

if __name__ == "__main__":
    maze = tk.Tk()
    maze.title("迷えるこうかとん")
    #maze.geometry("1500x900")
    canvas = tk.Canvas(maze,
                      width = 1500,
                      height = 900,
                      bg = "black")
    canvas.pack()
    koukaton = tk.PhotoImage(file = "fig/4.png")
    cx, cy = 300, 400
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