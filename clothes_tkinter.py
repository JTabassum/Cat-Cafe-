import tkinter as tk

def clothes(root, on_outfit_ready):
    root.title("Choose Your Clothes!")

    selected = {"top": None, "bottom": None}
    label = tk.Label(root, text="Choose your Top: ", font=("Times New Roman", 20))

    def sure_ag():
        label.config(text="Are you sure?")
        hoodie_button.grid_remove()
        shirt_button.grid_remove()
        apron_button.grid_remove()
        yes_to_bot.grid(row=2, column=0)
        no_to_bot.grid(row=2, column=1)
        jeans_button.grid_remove()
        shorts_button.grid_remove()
        skirt_button.grid_remove()

    def select_bottom(item):
        selected["bottom"] = item
        sure_ag()

    jeans_button = tk.Button(root, text="Jeans", command=lambda: select_bottom("Jeans"))
    shorts_button = tk.Button(root, text="Shorts", command=lambda: select_bottom("Shorts"))
    skirt_button = tk.Button(root, text="Skirt", command=lambda: select_bottom("Skirt"))

    def choose_bot():
        label.config(text="Choose your Bottoms: ")
        hoodie_button.grid_remove()
        shirt_button.grid_remove()
        apron_button.grid_remove()
        yes_to_bot.grid_remove()
        no_to_bot.grid_remove()
        jeans_button.grid(row=2, column=0)
        shorts_button.grid(row=2, column=1)
        skirt_button.grid(row=2, column=2)

    def select_top(item):
        selected["top"] = item
        choose_bot()

    def finish_outfit():
        yes_to_bot.grid_remove()
        no_to_bot.grid_remove()
        jeans_button.grid_remove()
        shorts_button.grid_remove()
        skirt_button.grid_remove()
        cat_label = tk.Label(root, text="=^._.^= ∫")
        on_outfit_ready(cat_label)

    hoodie_button = tk.Button(root, text="Hoodie", command=lambda: select_top("Hoodie"))
    apron_button = tk.Button(root, text="Apron", command=lambda: select_top("Apron"))
    shirt_button = tk.Button(root, text="T-Shirt", command=lambda: select_top("T-Shirt"))
    yes_to_bot = tk.Button(root, text="Yes", command=finish_outfit) #bottoms
    no_to_bot = tk.Button(root, text="No", command=choose_bot) #bottoms

    label.grid(row=0, column=0, columnspan=3, pady=10)
    hoodie_button.grid(row=2, column=0)
    apron_button.grid(row=2, column=1)
    shirt_button.grid(row=2, column=2)