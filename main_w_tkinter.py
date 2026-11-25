import tkinter as tk
from cyc_tkinter import create
from clothes_tkinter import clothes
from motion_tkinter import move

root = tk.Tk()
root.title("Main")
    
def show():
    clothes(root, lambda finalcat: move(root, finalcat))

create(root, show)

root.mainloop()