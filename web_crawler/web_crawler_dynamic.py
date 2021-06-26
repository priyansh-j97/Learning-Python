from bs4 import BeautifulSoup
import requests

def web_crawler(max_pages):
    p=1 
    count1=1
    while(p<=max_pages):
        url="https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_6_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_6_0_na_na_na&as-pos=6&as-type=TRENDING&suggestionId=mobiles&requestId=57a7a889-10e6-4db7-925e-2e671814323f&page="+str(p)
        source_code=requests.get(url) #this line fetches the source code of the stated url
        plain_text=source_code.text
        soup=BeautifulSoup(plain_text,"lxml") #"lxml" is the parser name            
        for link in soup.find_all('a',{'class':'_1fQZEK'}): #finds all the elements of the stated type from the entire source code
            href='https://www.flipkart.com'+link.get('href')
            crawler_further(href)
            print(href+'\n')
            count1+=1
            p+=1
            
def crawler_further(item_url):
    source1=requests.get(item_url)
    plain1=source1.text
    soup1=BeautifulSoup(plain1,"lxml")
    for title in soup1.find_all("div",{"class":"_30jeq3 _16Jk6d"}):
        print("Cost: "+title.string) #fetches the cost of the mobile phone from the next page


web_crawler(1)