from PIL import Image
from matplotlib import pyplot as plt
import numpy as np

im = np.array(Image.open('empire.jpg'))

#Plot the image
plt.imshow(im)
#plt.show()

# Some points
x = [100,100, 400, 400]
y = [200, 500, 200, 500]

#plot the points with red star-markers
plt.plot(x,y,'r*')

#line plot connecting the first two points, (100,200) to (200,500)
plt.plot(x[:2],y[:2])

# add title and show the plot
plt.title('Plotting: "empire.jpg"')

# remove the axis if you want
plt.axis('off')
plt.show()


