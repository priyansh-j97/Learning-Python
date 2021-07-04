dict={"google":55, "facebook":48, 'amazon':88, 'netflix':65}

# by default, the calculation on a "dictionary" is made to its first set i.e. in this case, names of companies

print(min(dict)) #this will find the minimum of "keys" i.e. names of the companies, hence alphabetically

print(min(zip(dict.values(),dict.keys()))) #using "zip" allows us to change the order of the contents