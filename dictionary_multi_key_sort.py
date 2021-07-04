from operator import itemgetter

stud=[
    {'name':'Priyansh','roll':'55'},
    {'name':'Alex','roll':'68'},
    {'name':'Felix','roll':'98'},
    {'name':'Naman','roll':'87'},
    {'name':'Naman','roll':'97'},
    {'name':'Naman','roll':'2'}
]

for x in sorted(stud,key=itemgetter("name")): #for sorting according to only one category
    print(x)

print("----------")

for x in sorted(stud,key=itemgetter("name","roll")): #for sorting according to two categories
    print(x)