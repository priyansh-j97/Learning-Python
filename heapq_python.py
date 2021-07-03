import heapq

# for the case of a simple "list"
nums=[5,4,8,44,845,669]
print(heapq.nlargest(3,nums)) #this will print the largest 3 numbers of the "list"
print(heapq.nsmallest(2,nums))

# for the case of a "list" of "dictionaries"
stud=[
    {'name':'Priyansh','roll':'55'},
    {'name':'Alex','roll':'68'},
    {'name':'Felix','roll':'98'},
    {'name':'Naman','roll':'87'}
]
print(heapq.nsmallest(2,stud,key=lambda x: x['roll']))
print(heapq.nlargest(2,stud,key=lambda x: x['name']))
