from PIL import Image
from matplotlib import pyplot as plt
import numpy as np

#Read image to array
im = np.array(Image.open('empire.jpg').convert('L'))

#create new figure
plt.figure()
#Dont use colors
plt.gray()
#Show contours with origin upper left corner
plt.contour(im, origin='image')
plt.axis('equal')
plt.axis('off')
plt.figure()
#create histogram, flatten array into 1D, have 128 'bins'
#could also use im.ravel(). ravel is faster, but space is O(1). it changes the array, while
#flatten creates a copy
plt.hist(im.flatten(),128)
plt.show()
