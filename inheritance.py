class Parent():
    def last_name(self):
        print("Jain")

    def middle_name(self):
        print("Java")

class Child(Parent):
    def first_name(self):
        print("Priyansh")

    def middle_name(self): #this method is also available in the "Parent" class, but still we can over-write it by defining it here again
        print("Python")

name=Child()

name.first_name()
name.middle_name()
name.last_name()