from PIL import Image

i1=Image.open("512.jpg")
i2=Image.open("628.jpg")

print(i1.mode) #this prints the mode of the image i.e. whether RGB or CMYK or something else
print(i2.mode)

r1,b1,g1=i1.split() #this will split the image in the individual color components
r2,b2,g2=i2.split()

#Note that the size of the component images should be same in order to get merged
img=Image.merge("RGB",(b1,b2,b2)) #this will merge the color components to form an image

img.show()