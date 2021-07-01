from PIL import Image

img1=Image.open("512.jpg")
img2=Image.open("God Why.jpg")

#this is for determining the sizes of the 2 images
size1=img1.size
size2=img2.size
print(size1," ",size2)

#defining the area as a tuple of 4 values for 2 coordinates
area=(1133,0,1920,444) #the area has to be in accordance with the image to be pasted and the image onto which it is to be pasted

#pasting img1 on img2
img2.paste(img1,area) #this is the format for pasting one image onto the other

img2.show()
