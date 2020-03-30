from PIL import Image
from matplotlib import pyplot as plt
import numpy as np

im = np.array(Image.open('empire.jpg'))
plt.imshow(im)
plt.axis("off")

print("Please click three points")

#Gets three button clicks from the user and puts them into list 'x'
x = plt.ginput(3)

print(f"You clicked: {x}")
plt.show()
