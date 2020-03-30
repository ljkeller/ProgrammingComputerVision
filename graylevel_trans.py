from PIL import Image
from matplotlib import pyplot as plt
import numpy as np

# SET ALL PLOTS TO GRAY
plt.gray()

im = np.array(Image.open('empire.jpg').convert('L'))

#invert image
im2 = 255 - im
 
# Clamp to interval 100....200
im3 = (100.0/255.0) * im + 100 

# squared (This is a quadratic function that lowers values of darker pixels)
im4 = 255.0 * (im/255.0)**2

print(im)

#Displaying multiple plots
plt.figure(1)
plt.imshow(im, cmap='gray')
plt.figure(2)
plt.imshow(im2)
plt.figure(3)
plt.imshow(im3)
plt.figure(4)
plt.imshow(im4)

#Gather information about images
print(im.min(), im.max())
print(im2.min(), im2.max())
print(int(im3.min()), int(im3.max()))
print(int(im4.min()), int(im4.max()))

#Generate graph data
gl1 = np.arange(0,256)
gl2 = np.flip(np.arange(0, 256))
gl3 = (100.0/255.0) * np.arange(0,256) + 100
gl4 = 255.0*(np.arange(0,256)/255.0)**2

#Set plot limiters, or x and y axis range
plt.figure(5)
plt.xlim(0, 255)
plt.ylim(0, 255)

#plot graphs
plt.plot(gl1)
plt.plot(gl2)
plt.plot(gl3)
plt.plot(gl4)

plt.show()
