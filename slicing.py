from PIL import Image
from matplotlib import pyplot as plt
import numpy as np

i, j, k = 0, 0, 0
im = np.array(Image.open('empire.jpg'))
#Prints the dimensions, static data type, and num-elements
print(im.shape, im.dtype, im.size)
#Access the value at coordinates i, j and color channel k
value = im[i,j,k]

#Set the values of row i with the values from row j
im[i,:] = im[j,:]

# set all values in column i to 100 
im[:,i] = 100

# the sum of the values of the first 100 rows and columns
im[:100, :50].sum()

#Average of row i
im[i].mean()

#last column
im[:,-1]

#second to last row, important to note if only one index is mentioned, its the row index
im[-2,:] (or im[-2])
