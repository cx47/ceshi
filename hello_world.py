print("hello world")

def hello_world(name):
    return f"Hello,{name}. This is your Python world"

name = "Chen Xi"
print(hello_world(name=name))


class Game():
    def __init__(self):
        self.name = "Monster Hunter"
        
    def hobby(self):
        return "I like play {}".format(self.name)


game = Game()
print(game.hobby())