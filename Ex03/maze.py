import tkinter as tk

if __name__ == "__main__":
    maze = tk.Tk()
    maze.title("迷えるこうかとん")
    #maze.geometry("1500x900")
    canvas = tk.Canvas(maze,
                      width = 1500,
                      height = 900,
                      bg = "black")
    canvas.pack()
    maze.mainloop()