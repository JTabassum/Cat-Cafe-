import tkinter as tk

def create(root, next):
    root.title("Choose Your Charcater!")

    label = tk.Label(root, text = "Choose your character: ", font = ("Times New Roman", 20))


    def sure_then_clothes():
        label.config(text="Are you sure?")
        
        def go_to_clothes():
            y.grid_remove()
            n.grid_remove()
            next()
        
        y = tk.Button(root, text="Yes to cat", command=go_to_clothes)
        n = tk.Button(root, text="No to cat")
        
        y.grid(row=3, column=0)
        n.grid(row=3, column=1)
        
        cal_button.grid_remove()
        sia_button.grid_remove()
        munch_button.grid_remove()
        
    cal_button = tk.Button(root, text="Calico", command=sure_then_clothes)
    sia_button = tk.Button(root, text="Siamese", command=sure_then_clothes)
    munch_button = tk.Button(root, text="Munchkin", command=sure_then_clothes)

    label.grid(row=0, column=0, columnspan=3, pady=10)
    cal_button.grid(row=2, column=0)
    sia_button.grid(row=2, column=1)
    munch_button.grid(row=2, column=2) 
