first=['Priyansh','Hello','Alice']
last=['Jain','World','Rogers']

full=zip(first,last) #this creates a list of tuples like [('Priyansh','Jain'),('Hello','World'),('Alice','Rogers')]

print(type(full),'\n') #this is a new class named "zip"

for a,b in full:
    print(a,b)