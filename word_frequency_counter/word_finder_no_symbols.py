import requests
from bs4 import BeautifulSoup

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
            print(word)
            clean_list.append(word)
        

word_finder("https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
