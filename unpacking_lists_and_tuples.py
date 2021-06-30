grocery=['milk','coffee','tea','sugar']
nums=(1,2,3,4,5,6,7,8,9)

# Method-1
# Example: unpacking a list
w,x,y,z=grocery
print(w)
print(y+'\n')

# Example: unpacking a tuple
a,b,c,d,e,f,g,h,i=nums
print(a)
print(h+i)
print('\n')

# Method-2
# Example: unpacking a tuple or a list
def unpack(numbers):
    if type(numbers)==tuple:
        first, *middle, last=numbers #this is how we allocate all the middle values of the tuple to a single variable with addition of "*"
        avg=sum(middle)/len(middle)
        print(first,' ',avg,' ',last)
    elif type(numbers)==list:
        start,*mid,end=numbers #this is how we allocate all the middle values of the list to a single variable with addition of "*"
        print(mid)

unpack(nums)
unpack(grocery)
