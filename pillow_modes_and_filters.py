#CMYK is commonly used for printing by printers
from PIL import Image, ImageFilter
img=Image.open("512.jpg")
bw_img=img.convert("L") #"L" code is used for "Black and White" mode
cmyk_img=img.convert("CMYK") #"CMYK" code is used for "CMYK" mode

print(bw_img.mode)
print(cmyk_img.mode)

bw_img.show()
cmyk_img.show()

#filters
blur=img.filter(ImageFilter.BLUR)
detail=img.filter(ImageFilter.DETAIL)
edges=img.filter(ImageFilter.FIND_EDGES)

blur.show()
detail.show()
edges.show()