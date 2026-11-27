import tkinter as tk
from cyc_tkinter import create
from clothes_tkinter import clothes
from motion_tkinter import move

root = tk.Tk()
root.title("Main")

def show(animal, character_name):
    #display text of what ur wearing
    
    move(root, animal, character_name)

create(root, show)

root.mainloop()