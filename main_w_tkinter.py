import tkinter as tk
from cyc_tkinter import create
from clothes_tkinter import clothes
from motion_tkinter import move

root = tk.Tk()
root.title("Main")

def show(animal, character_name):
    def show_outfit(outfit):
        move(root, animal, character_name)
        tk.Label(root, text=f"{character_name} is wearing {outfit}.", font=("Times New Roman", 16)).grid(row=3, column=0, columnspan=3, pady=10)

    clothes(root, show_outfit)

create(root, show)

root.mainloop()