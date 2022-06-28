import tkinter as tk

if __name__ == "__main__":
    maze = tk.Tk()
    maze.title("迷えるこうかとん")
    #maze.geometry("1500x900")
    canvas = tk.Canvas(maze,
                      width = 1500,
                      height = 900,
                      bg = "black")
    koukaton = tk.PhotoImage(file = "fig/4.png")
    cx, cy = 300, 400
    canvas.create_image(cx,
                       cy,
                       image = koukaton,
                       tag = "koukaton"
                       )
    canvas.pack()
    maze.mainloop()