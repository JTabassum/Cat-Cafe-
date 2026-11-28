import tkinter as tk
from tkinter import ttk

def create(root, next):
    root.title("Choose Your Character!")
    root.geometry("280x343")

    label = tk.Label(
        root,
        text="Choose your character:",
        font=("Times New Roman", 15),
    )

    def choose_animal(animal):
        label.config(text="Are you sure?")

        cal_button.grid_remove()
        sia_button.grid_remove()
        gin_button.grid_remove()

        def char_name():
            y.grid_remove()
            n.grid_remove()

            label.config(text=f"Name your {animal}!")

            name = ttk.Entry(root, width=25)
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

        def go_back():
            y.grid_remove()
            n.grid_remove()
            label.config(text="Choose your character:")
            cal_button.grid()
            sia_button.grid()
            gin_button.grid()

        y = tk.Button(root, text="Yes", command=char_name)
        n = tk.Button(root, text="No", command=go_back)

        y.grid(row=3, column=0)
        n.grid(row=3, column=1)

    cal_button = tk.Button(root, text="Calico",command=lambda: choose_animal("Calico"))
    sia_button = tk.Button(root, text="Siamese",command=lambda: choose_animal("Siamese"))
    gin_button = tk.Button(root, text="Ginger",command=lambda: choose_animal("Ginger"))
    enter = tk.Button(root, text="Enter")
    label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    cal_button.grid(row=2, column=0, pady=20)
    sia_button.grid(row=2, column=1, pady=20)
    gin_button.grid(row=2, column=2, pady=20)