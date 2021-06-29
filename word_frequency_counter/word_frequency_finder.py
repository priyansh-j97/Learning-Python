import requests
from bs4 import BeautifulSoup
import operator

def word_finder(url):
    words_list=[]
    source=requests.get(url).text
    soup=BeautifulSoup(source,'lxml')
    for word in soup.findAll('div',{'class':'_4rR01T'}):
        content=word.string
        w=content.lower().split()
        for i in w:
            words_list.append(i)
    cleaner(words_list)

def cleaner(words_list):
    clean_list=[]
    symbols="~!@#$%^&*(\")_+'=-`.\<>/?,"
    for word in words_list:
        for x in range(0,len(symbols)):
            word=word.replace(symbols[x],"")
        if (len(word)>0):
            clean_list.append(word)
    word_dictionary(clean_list)

def word_dictionary(clean_list):
    dict={}
    for word in clean_list:
        if word in dict: #this is how we enter values in a dictionary
            dict[word]+=1
        else:
            dict[word]=1
    for key,value in sorted(dict.items(),key=operator.itemgetter(1)): #this will sort all the items of the dictionary. Here itemgetter(0) will sort as per key and itemgetter(1) will sort as per the value  
        print(key+" ---> "+str(value))
        

word_finder("https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")