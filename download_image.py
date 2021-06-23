import random
import urllib.request

def download_image(url):
    name=random.randrange(1,1000)
    full_name=str(name)+".jpg"
    urllib.request.urlretrieve(url,full_name)

download_image("https://hatrabbits.com/wp-content/uploads/2017/01/random.jpg") #stores the file in the immediate directory in which the code is running