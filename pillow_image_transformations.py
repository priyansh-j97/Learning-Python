from PIL import Image

img=Image.open("512.jpg")

resized_img=img.resize((250,250)) #to resize the image
transposed_img=img.transpose(Image.FLIP_LEFT_RIGHT) #to transpose the image
rotate_img=img.transpose(Image.ROTATE_180)

img.show()
resized_img.show()
transposed_img.show()
rotate_img.show()