def gender(sex='Unknown'):
    if sex is 'm' or sex is 'M':
        sex='Male'
    elif sex is 'f' or sex=='F': #here sex=='F' is the same as sex is 'F'
        sex='Female'
    print(sex)

gender('M')
gender('m')
gender('F')
gender('f')
gender()

    