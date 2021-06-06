s1 = "Hello World"
s2 = 'Hola World'
s3 = 'I don\'t think she\'s 18!' #using "\" just before the quotation mark will consider it just as normal text
s4 = "But she said, \"I am 18 indeed!\""
print (s1+"\n"+s2+"\n"+s3+"\n"+s4+"\n")

s5 = r"C:\\path\noob" #considers the string as a raw string without taking into consideration "\" related operations like "\n" or "\t"
print(s5)