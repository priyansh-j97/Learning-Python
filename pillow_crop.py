from PIL import Image

img=Image.open("512.jpg")
area=(0,111,787,333) #this is an area tuple which contains 4 values as coordinates of 2 points (x1,y1,x2,y2)
cropped_img=img.crop(area)

img.show()
cropped_img.show()