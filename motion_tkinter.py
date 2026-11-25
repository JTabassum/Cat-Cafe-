import tkinter as tk


def move(root, next):
    root.title("Move Your Character!")

    label = tk.Label(root, text = "Move your Character! ", font = ("Times New Roman", 20))

    
    def up():
        # Move up
        pass

    def down():
        # Move down
        pass

    def left():
        # Move left
        pass

    def right():
        # Move right
        pass

    u = tk.Button(root, text="↑", command=up)
    d = tk.Button(root, text="↓", command=down)
    l = tk.Button(root, text="←", command=left)
    r = tk.Button(root, text="→", command=right)

    label.grid(row=0, column=0, columnspan=3, pady=10)
    u.grid(row=1, column=1)
    l.grid(row=2, column=0)
    d.grid(row=2, column=1)
    r.grid(row=2, column=2)
