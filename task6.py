import matplotlib.image as mpimg
import numpy as np

image = mpimg.imread("apple.jpg")

image = image.astype(float)

height = image.shape[0]
width = image.shape[1]

gray_image = np.zeros((height, width))

for i in range(height):
    for j in range(width):
        R = image[i, j, 0]
        G = image[i, j, 1]
        B = image[i, j, 2]

        gray_image[i, j] = 0.299 * R + 0.587 * G + 0.114 * B

gray_image = gray_image.astype(np.uint8)

mpimg.imsave("grayscale_apple.jpg", gray_image, cmap="gray")

print("RGB image converted to grayscale successfully!")