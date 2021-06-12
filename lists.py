numbers=[1,2,3,4,5,6] #this is a list
print(numbers[2])
print(numbers[:3])

numbers.append(7) #the append function only takes in 1 arguement

l=len(numbers)
print(l)

print(numbers[:l]) #this is same as numbers[:]

print(numbers+[55,66,77])

numbers[:3]=[0,0,0]
print(numbers[:l])

numbers[:2]=[]
print(numbers[:])

numbers[:]=[]
print(numbers[:])