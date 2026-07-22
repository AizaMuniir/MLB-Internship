#Task 6: Manual Convolution Implement the convolution operation from scratch using loops. Do not use any built-in convolution functions. Apply a 3×3 kernel to a grayscale image and generate the output image.
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("apple.jpg", 0).astype(np.float64)  # to avoid uint8 overflow

kernel = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])

h, w = image.shape

# Zero-pad by 1 pixel on each side so output size == input size
padded = np.zeros((h + 2, w + 2))
padded[1:-1, 1:-1] = image

output = np.zeros((h, w))

for i in range(h):
    for j in range(w):
        total = 0
        for ki in range(3):
            for kj in range(3):
                total += padded[i + ki][j + kj] * kernel[ki][kj]
        output[i][j] = total

# Clip to valid pixel range before displaying/saving
output_clipped = np.clip(output, 0, 255).astype(np.uint8)

plt.imshow(output_clipped, cmap="gray")
plt.axis("off")
plt.show()