import tkinter as tk

def move(root, animal, chracter_name):
    root.title("Move Your Character!")
    label = tk.Label(root, text = "Move your Character! ", font = ("Times New Roman", 20))
    photo = tk.PhotoImage()
    
    def up():
        # Move up
        label.config(text="You moved up!")

    def down():
        # Move down
        label.config(text="You moved down!")

    u = tk.Button(root, text="↑", command=up)
    d = tk.Button(root, text="↓", command=down)

    label.grid(row=0, column=0, columnspan=3, pady=10)
    u.grid(row=1, column=1)
    d.grid(row=2, column=1)




'''
    if animal == "Cat":
        photo = tk.PhotoImage(file="ginger.png")

    elif animal == "Dog":
        photo = tk.PhotoImage(file="dog.png")

    elif animal == "Bird":
        photo = tk.PhotoImage(file="bird.png")
        
    character = tk.Label(root, image=photo)
    character.image = photo

    character.place(x=200, y=100)
'''