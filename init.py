class Enemy:
    def __init__(self,x): #this is just like a constructor and hence it gets called as soon as an object is created
        self.energy = x #the variable energy is define here
        print("This is an \"init\" function")

    def EnemyEnergy(self,name):
        print("----------\n"+str(name)+" Energy: "+str(self.energy))

yeti = Enemy(5)
bigfoot = Enemy(20)

yeti.EnemyEnergy("Yeti")
bigfoot.EnemyEnergy("Bigfoot")