income=[5,10,25]

def factor(x):
    return x*2

new_income=list(map(factor,income)) #the format of map is map(method,iterable)

print(income)
print(new_income)
