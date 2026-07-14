import matplotlib.image as mpimg
import numpy as np

image = mpimg.imread("apple.jpg")

image = image.copy()

red_channel = np.zeros_like(image)
green_channel = np.zeros_like(image)
blue_channel = np.zeros_like(image)

red_channel[:, :, 0] = image[:, :, 0]
green_channel[:, :, 1] = image[:, :, 1]
blue_channel[:, :, 2] = image[:, :, 2]

mpimg.imsave("red_channel.jpg", red_channel)
mpimg.imsave("green_channel.jpg", green_channel)
mpimg.imsave("blue_channel.jpg", blue_channel)

print("RGB channels separated and saved successfully!")
