import os
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np

def get_imlist(path):
    """Returns a list of filenames for 
        all jpg images in a directory"""

    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

def imresize(im, sz):
    """ Resize an image array using PIL. """
    pil_im = Image.fromarray(uint8(im))

    return np.array(pil_im.resize(sz))

def histeq(im, nbr_bins=256):
    """ Histogram equalization of a grayscale image. """

    # Get image histogram
    imhist, bins = np.histogram(im.flatten(), nbr_bins, normed=True)
    cdf = imhist.cumsum() # Cumulative distribution function
    cdf = 255 * cdf / cdf[-1]

    # use linear interpolation of cdf to find new pixel values
    im2 = np.interp(im.flatten(), bins[:-1], cdf)

    return im2.reshape(im.shape), cdf
