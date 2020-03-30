from PIL import Image
import os
from imtools import get_imlist

#Programmingcomputervision.com - good resource

pil_im = Image.open('empire.jpg')
im_size = pil_im.size
#Get tuple for image size
print(im_size)
pil_im_contr = Image.open('empire.jpg').convert('L')

pil_im.show()
pil_im_contr.show()
#Save usage with jpg
pil_im_contr.save("empire_grayscale.jpg", "jpeg")

#Copy image
pil_im_cp = pil_im.copy()

#Thumbnail usage
pil_im_contr.thumbnail((128, 128))
pil_im_contr.show()

#List all jpg images in directory
l_images = get_imlist(os.getcwd())

#Crop the image
rect = (100, 100, 400, 400)
rect_region = pil_im.crop(rect)
rect_region.show()

#rotate image, paste it
rect_region = rect_region.transpose(Image.ROTATE_180)
rect_region.show()
pil_im.paste(rect_region, rect)
pil_im.show()


#Resize and rotate
pil_im_resized = pil_im_cp.resize((256, 256))
pil_im_resized.show("Resized")
pil_im_rotated = pil_im_resized.rotate(45)
pil_im_rotated.show("Rotated")

#Currently at page ~15
print(l_images)
