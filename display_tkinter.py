import tkinter as tk

def display(root, animal, character_name, outfit):
    root.title("Say Hi!")
    root.geometry("280x343")
    
    top = outfit.split(" and ", 1)[0]
    image_files = {
        ("Calico", "Hoodie"): "cal_in_hoodie.png",
        ("Calico", "Apron"): "cal_in_apron.png",
        ("Calico", "T-Shirt"): "cal_in_t.png",
        ("Siamese", "Hoodie"): "sia_in_hoodie.png",
        ("Siamese", "Apron"): "sia_in_apron.png",
        ("Siamese", "T-Shirt"): "sia_in_t.png",
        ("Ginger", "Hoodie"): "ginger_in_hoodie.png",
        ("Ginger", "Apron"): "ginger_in_apron.png",
        ("Ginger", "T-Shirt"): "ginger_in_t.png",
    }

    photo = tk.PhotoImage(file=image_files[(animal, top)])
    label = tk.Label(
        root,
        text=f"This is {character_name}!",
        font=("Times New Roman", 15),
    )
    label.place(x=0, y=10, width=280)

    character = tk.Label(root, image=photo)
    setattr(character, "image", photo)
    character.place(x=(280 - photo.width()) // 2, y=50)
    
    y:int = 50 
    def up(y):
        if y <10:
            y = 10
        y = y - 5
        character.place(y=y)

    def down(y):
        if y > 200:
            y = 200
        y = y + 5
        character.place(y=y)

    u = tk.Button(root, text="", command = lambda: up(y))
    d = tk.Button(root, text="", command = lambda: down(y))

    u.config(text="↑")
    d.config(text="↓") 
    
    u.place(x=115, y=250, width=50, height=30)
    d.place(x=115, y=285, width=50, height=30)
    