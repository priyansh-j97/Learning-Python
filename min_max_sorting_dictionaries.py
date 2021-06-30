#this is a dictionary with keys and values in the format keys:values
stocks={ 
    'Facebook':77,
    'Amazon':89,
    'Apple':99,
    'Netflix':94.7,
    'Google':78
}

print(min(zip(stocks.keys(),stocks.values()))) #this calculates the minimum key
print(min(zip(stocks.values(),stocks.keys()))) #this calculates the minimum value

print('\n')

print(max(zip(stocks.keys(),stocks.values()))) #this calculates the maximum key
print(max(zip(stocks.values(),stocks.keys()))) #this calculates the maximum value

print('\n')

print(sorted(zip(stocks.keys(),stocks.values()))) #this sorts the dictionary by keys as per alphabetical order, as there are stings
print(sorted(zip(stocks.values(),stocks.keys()))) #this sorts the dictionary by values