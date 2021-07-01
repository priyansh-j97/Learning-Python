from PIL import Image #this is how we import the "pillow" library

img=Image.open("512.jpg") #img is an object of PIL
print(img.size)
print(img.format)

img.show()