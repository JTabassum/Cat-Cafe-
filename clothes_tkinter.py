import tkinter as tk


def clothes(root):
    root.title("Choose Your Clothes!")

    label = tk.Label(root, text="Choose your Top: ", font=("Times New Roman", 20))

    def sure_ag():
        label.config(text="Are you sure?")
        hoodie_button.grid_remove()
        shirt_button.grid_remove()
        apron_button.grid_remove()
        yes_to_top.grid_remove()
        no_to_top.grid_remove()
        yes_to_bot.grid(row=2, column=0)
        no_to_bot.grid(row=2, column=1)
        jeans_button.grid_remove()
        shorts_button.grid_remove()
        skirt_button.grid_remove()
        

    jeans_button = tk.Button(root, text="Jeans", command = sure_ag)
    shorts_button = tk.Button(root, text="Shorts",command = sure_ag)
    skirt_button = tk.Button(root, text="Skirt",command = sure_ag)

    def choose_bot():
        label.config(text="Choose your Bottoms: ")
        yes_to_top.grid_remove()
        no_to_top.grid_remove()
        jeans_button.grid(row=2, column=0)
        shorts_button.grid(row=2, column=1)
        skirt_button.grid(row=2, column=2)
    
    def go_to_bot():
    
        choose_bot()

    def sure():
        label.config(text="Are you sure?")
        hoodie_button.grid_remove()
        shirt_button.grid_remove()
        apron_button.grid_remove()
        yes_to_top.grid(row=2, column=0)
        no_to_top.grid(row=2, column=1)
    
    yes_to_top = tk.Button(root, text="Yes to top", command=go_to_bot)
    no_to_top = tk.Button(root, text="No to top")
    hoodie_button = tk.Button(root, text="Hoodie", command=sure)
    apron_button = tk.Button(root, text="Apron", command=sure)
    shirt_button = tk.Button(root, text="T-Shirt", command=sure)
    yes_to_bot= tk.Button(root, text="Yes to top")
    no_to_bot= tk.Button(root, text="No to top")

    label.grid(row=0, column=0, columnspan=3, pady=10)
    hoodie_button.grid(row=2, column=0)
    apron_button.grid(row=2, column=1)
    shirt_button.grid(row=2, column=2)
    

    