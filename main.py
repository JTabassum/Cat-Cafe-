from chooseyourcharacter import choose
from motion_class import Motion


def start():
    cat = choose() 
    
    with open("Character.txt", "w") as f:
        f.write(f"you are a {cat.breed} named {cat.name} wearing a {cat.top} and a {cat.bottoms}. slay")       
    
    cat.display()         
    move = Motion(cat)    

    while True:
        action = input("\nWhat do you want to do? (left, right, jump, crouch, quit)\n").strip().lower()

        if action == "left":
            move.left()
        elif action == "right":
            move.right()
        elif action == "jump":
            move.jump()
        elif action == "crouch":
            move.crouch()
        elif action == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid action. Please try again.")

        print(f"Current position: x={cat.x}, y={cat.y}")


if __name__ == "__main__":
    start()