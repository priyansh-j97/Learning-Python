#this will create and write in the newly created file
fw = open("sample.txt",'w') #w stands for write and fw is the file object
fw.write("Hello Dunia!\n")
fw.write('Ssup?\n')
fw.close()

#this will read data from the mentioned file
fr = open("sample.txt",'r')
text=fr.read() #the data gets stored in this variable
print(text)
fr.close()