class Character:
    def __init__(self, breed, name, top, bottoms, x = 0, y = 0):
        self.breed = breed
        self.name = name
        self.top = top
        self.bottoms = bottoms
        self.x = x
        self.y = y

class Motion:
    def __init__(self, character):
        self.character = character
        
    def reset(self, character):
            self.character.x = 0
            self.character.y = 0
    
    def left(self):
        self.character.x -= 1
    
    def right(self):
        self.character.x += 1
    
    def jump(self):
        self.character.y += 5
        print("Jumping! Current position: x={}, y={}".format(self.character.x, self.character.y))
        self.reset(self.character)
        
    def crouch(self):
        self.character.y -= 5
        print("Crouching! Current position: x={}, y={}".format(self.character.x, self.character.y))
        self.reset(self.character)
        
