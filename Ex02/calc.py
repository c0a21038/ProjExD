import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo("", f"[{num}]ボタンが押されました")
    if num == "=":
        eqn = entry.get()
        if "÷" in eqn:
            eqn = eqn.replace("÷", "/")
        if "×" in eqn:
            eqn = eqn.replace("×", "*")
        if "%" in eqn:
            eqn = eqn.replace("%", "/100")
        ans = eval(eqn)
        entry.delete(0,tk.END)
        entry.insert(tk.END, ans)
    elif num == "C":
        entry.delete(0,tk.END)
    elif num == "B":
        eqn = entry.get()
        eqn = eqn[:-1]
        entry.delete(0,tk.END)
        entry.insert(tk.END, eqn)
    else:
        entry.insert(tk.END, num)



if __name__ == "__main__":
    root = tk.Tk()
    root.title("電卓")
    #root.geometry("300x600")

    entry = tk.Entry(root, 
                    justify="right", 
                    width=10, 
                    font=("Times New Roman", 40)
                    )
    entry.grid(row=0, column=0, columnspan=3)  # 横方向に3マス結合
    
    r,c = 1,0  # r:行番号 c:列番号
    for i, num in enumerate(["C", "%", "B", "÷", 7, 8, 9, "×", 4, 5, 6, "-" , 1, 2, 3, "+", "00", 0, ".", "="]):
        if num == "=":
            btn = tk.Button(root,
                            text=f"{num}", 
                            bg="#6495ED",
                            width=4, 
                            height=1, 
                            font=("Times New Roman", 30)
                            )
        else:
            btn = tk.Button(root,
                            text=f"{num}", 
                            width=4, 
                            height=1, 
                            font=("Times New Roman", 30)
                            )
        btn.bind("<1>", button_click)
        btn.grid(row=r, column=c)

        c += 1
        if(i+1)%4 == 0:
            r += 1
            c = 0
    
    

    root.mainloop()
