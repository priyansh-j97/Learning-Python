class Girl():

    gender = 'female' #this is a class variable: remains the same always

    def __init__(self,name):
        self.name=name #this is an instance variable

    def calling(self):
        print("Name: "+self.name)

r=Girl("Rachel")
s=Girl("Scarlett")

print(r.gender)
print(s.gender)

r.calling()
s.calling()