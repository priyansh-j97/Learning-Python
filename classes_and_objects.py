class Enemy:
    life = 3
    def attack(self,name): #define an arguement like "self" as the first arguement of the function, here self is the official parameter of the class, used to access variables and other elements of the class
        print(str(name)+" has been attacked!")
        self.life -=1 #this is the way of accessing the variable inside the class
    
    def checkLife(self,name):
        if(self.life<=0):
            print("----------\n"+name+" knocked out!")
        else:
            print("----------\n"+"Life(s) left for "+name+": "+str(self.life))

e1=Enemy() #creating an object of the class, this is Enemy 1
e2=Enemy() #creating another object of the class, this is Enemy 2

e1.attack("Enemy 1") #calling the functions inside the object's class
e1.attack("Enemy 1")
e1.attack("Enemy 1")
e2.attack("Enemy 2")

e1.checkLife("Enemy 1")
e2.checkLife("Enemy 2")