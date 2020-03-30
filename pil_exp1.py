from PIL import Image
import os
from imtools import get_imlist

#Programmingcomputervision.com - good resource

pil_im = Image.open('empire.jpg')
pil_im.show()
rot = pil_im.rotate(23)
rot.show()
