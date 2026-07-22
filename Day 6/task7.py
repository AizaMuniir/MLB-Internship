#Task 7: Kernel Operations Create and apply the following kernels manually: Identity Kernel Blur Kernel Sharpen Kernel Edge Detection Kernel Compare the output of each kernel and explain its effect on the image.
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("apple.jpg", cv2.IMREAD_GRAYSCALE)

# Kernels
identity = np.array([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
])

blur = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]) / 9

sharpen = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

edge = np.array([
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1]
])


def manual_convolution(image, kernel):

    h, w = image.shape
    output = np.zeros((h - 2, w - 2))

    for i in range(h - 2):
        for j in range(w - 2):

            total = 0

            for ki in range(3):
                for kj in range(3):
                    total += image[i + ki][j + kj] * kernel[ki][kj]

            if total < 0:
                total = 0

            if total > 255:
                total = 255

            output[i][j] = total

    return output.astype(np.uint8)


identity_output = manual_convolution(image, identity)
blur_output = manual_convolution(image, blur)
sharpen_output = manual_convolution(image, sharpen)
edge_output = manual_convolution(image, edge)

plt.figure(figsize=(12,8))

plt.subplot(2,3,1)
plt.imshow(image, cmap="gray")
plt.title("Original")
plt.axis("off")

plt.subplot(2,3,2)
plt.imshow(identity_output, cmap="gray")
plt.title("Identity")
plt.axis("off")

plt.subplot(2,3,3)
plt.imshow(blur_output, cmap="gray")
plt.title("Blur")
plt.axis("off")

plt.subplot(2,3,5)
plt.imshow(sharpen_output, cmap="gray")
plt.title("Sharpen")
plt.axis("off")

plt.subplot(2,3,6)
plt.imshow(edge_output, cmap="gray")
plt.title("Edge Detection")
plt.axis("off")

plt.show()