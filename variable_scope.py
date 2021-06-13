b=8 #this is a global variable

def corn():
    a=5
    print(a)
    print(b)

def wheat():
    print(b) #a cannot be printed here as it is not defined in the scope of the wheat function

corn()
wheat()