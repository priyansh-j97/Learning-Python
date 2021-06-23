def health_calculator(age,apples,cigs):
    calculate=age+apples-cigs
    print(calculate)

priyansh=[25,55,0]
health_calculator(*priyansh) #this will unpack the entire list named "priyansh" so as to provide arguements to the function