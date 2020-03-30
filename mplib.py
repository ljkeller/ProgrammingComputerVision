from PIL import Image
from matplotlib import pyplot as plt
import numpy as np

# read image into array
im = np.array(Image.open('empire.jpg'))

#Doesn't seem to be working as inteneded
imgplot = plt.imshow(im)
#Display all figures
#plt.show()

#Array slicing 
im_slice = im[:, :, 0]

#CHange the colormap to be non-default
plt.imshow(im_slice, cmap="nipy_spectral")

#Could also use
# im_slice.set_cmap('nipy_spectral')

#Add a color bar
plt.colorbar()

#make a histogram to analyze, ect...
plt.hist(im_slice.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')

plt.show()
print(type(imgplot))
