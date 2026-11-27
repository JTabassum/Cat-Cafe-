import tkinter as tk
from tkinter import ttk

def create(root, next):
    root.title("Choose Your Character!")

    label = tk.Label(root,text="Choose your character:", font=("Times New Roman", 20))

    def choose_animal(animal):
        label.config(text="Are you sure?")

        cat_button.grid_remove()
        dog_button.grid_remove()
        bird_button.grid_remove()

        def char_name():
            y.grid_remove()
            n.grid_remove()

            label.config(text=f"Name your {animal}!")

            name = ttk.Entry(root, width=30)
            name.grid(row=2, column=0, columnspan=3, pady=10)

            def submit_name():
                character_name = name.get().strip()

                if character_name:
                    label.grid_remove()
                    name.grid_remove()
                    enter.grid_remove()

                    next(animal, character_name)

            enter.configure(command=submit_name)
            enter.grid(row=3, column=2)

        y = tk.Button(root, text="Yes", command=char_name)
        n = tk.Button(root, text="No")

        y.grid(row=3, column=0)
        n.grid(row=3, column=1)

    cat_button = tk.Button(root, text="Cat",command=lambda: choose_animal("Cat"))
    dog_button = tk.Button(root, text="Dog",command=lambda: choose_animal("Dog"))
    bird_button = tk.Button(root, text="Bird",command=lambda: choose_animal("Bird"))
    enter = tk.Button(root, text="Enter")
    label.grid(row=0, column=0, columnspan=3, pady=10)

    cat_button.grid(row=2, column=0)
    dog_button.grid(row=2, column=1)
    bird_button.grid(row=2, column=2)