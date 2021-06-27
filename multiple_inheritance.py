class Action():
    def move(self):
        print("Mario is moving...")

class Mushroom():
    def eat(self):
        print("Mario ate a mushroom!")

class Mario(Action,Mushroom): #this is how we can inherit from multiple classes
    pass

m=Mario()

m.move()
m.eat()