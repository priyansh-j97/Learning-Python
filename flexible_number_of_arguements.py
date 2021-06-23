def addition(*args): #here args is just a variable name which is generally used in Python, we can also name it something else
    sum=0
    for a in args:
        sum+=a
    print(sum)

addition(5)
addition(5,8)
addition(4,5,6,7,8,9,7)

def random_text(*args):
    net=''
    for a in args:
        net=net+a+" "
    print(net)

random_text('hello')
random_text('hello',"world",'yeah!')
