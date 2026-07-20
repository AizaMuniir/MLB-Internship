import numpy as np
import matplotlib.image as mpimg

image = mpimg.imread("apple.jpg")

if len(image.shape) == 3:
    height, width = image.shape[0], image.shape[1]
    gray = np.zeros((height, width))

    for i in range(height):
        for j in range(width):
            R = image[i, j, 0]
            G = image[i, j, 1]
            B = image[i, j, 2]
            gray[i, j] = 0.299 * R + 0.587 * G + 0.114 * B

    image = gray


image = image.astype(np.uint8)

T = 127

binary = np.zeros_like(image)
binary_inverse = np.zeros_like(image)
truncate = np.zeros_like(image)
to_zero = np.zeros_like(image)
inverse_to_zero = np.zeros_like(image)

height, width = image.shape

for i in range(height):
    for j in range(width):

        pixel = image[i, j]

        # Binary Threshold
        if pixel > T:
            binary[i, j] = 255
        else:
            binary[i, j] = 0

        # Binary Inverse Threshold
        if pixel > T:
            binary_inverse[i, j] = 0
        else:
            binary_inverse[i, j] = 255

        # Truncate Threshold
        if pixel > T:
            truncate[i, j] = T
        else:
            truncate[i, j] = pixel

        # To Zero Threshold
        if pixel > T:
            to_zero[i, j] = pixel
        else:
            to_zero[i, j] = 0

        # Inverse To Zero Threshold
        if pixel > T:
            inverse_to_zero[i, j] = 0
        else:
            inverse_to_zero[i, j] = pixel

mpimg.imsave("binary.png", binary, cmap="gray")
mpimg.imsave("binary_inverse.png", binary_inverse, cmap="gray")
mpimg.imsave("truncate.png", truncate, cmap="gray")
mpimg.imsave("to_zero.png", to_zero, cmap="gray")
mpimg.imsave("inverse_to_zero.png", inverse_to_zero, cmap="gray")

print("Thresholding completed successfully!")