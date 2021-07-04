from operator import attrgetter

class user:
    def __init__(self,x,y): #this is for initialization
        self.name=x
        self.id=y
    def __repr__(self): #this is for representation
        return self.name + " -> " + str(self.id)

stud=[ #this is a list of elements calling the class "user"
    user('Priyansh',54),
    user('Alex',57),
    user('Timmothy',57),
    user('Tiffany',4),
    user('Joel',74),
    user('Alice',8)
]

for u in stud:
    print(u) 

print("-----")

for i in sorted(stud,key=attrgetter('name')):
    print(i)

for r in sorted(stud,key=attrgetter("id")):
    print(r)