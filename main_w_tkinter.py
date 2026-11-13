import tkinter as tk
from cyc_tkinter import create
from clothes_tkinter import clothes

root = tk.Tk()
root.title("Main")
    
def show():
    clothes(root)

create(root, show)

root.mainloop()