import tkinter as tk
from cyc_tkinter import create
from clothes_tkinter import clothes
from display_tkinter import display

root = tk.Tk()
root.title("Main")
root.geometry("280x343")

def show(animal, character_name):
    def show_outfit(outfit):
        display(root, animal, character_name, outfit)

    clothes(root, show_outfit)

create(root, show)

root.mainloop()