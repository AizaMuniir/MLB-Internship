import numpy as np
import matplotlib.image as mpimg

image = mpimg.imread("apple.jpg")

height = image.shape[0]
width = image.shape[1]

if len(image.shape) == 3:
    channels = image.shape[2]
else:
    channels = 1

datatype = image.dtype

total_pixels = height * width

print("Height:", height)
print("Width:", width)
print("Number of Channels:", channels)
print("Data Type:", datatype)
print("Total Number of Pixels:", total_pixels)