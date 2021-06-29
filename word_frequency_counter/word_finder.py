import requests
from bs4 import BeautifulSoup

def find_word(url):
    wordlist=[]
    source=requests.get(url).text
    soup=BeautifulSoup(source,'lxml')
    for data in soup.findAll('div',{'class':'_4rR01T'}):
        content=data.string
        words=content.lower().split()
        for w in words:
            print(w)
            wordlist.append(w)

find_word('https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')