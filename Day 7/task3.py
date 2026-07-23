#Gaussian Filter 

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load image
image = mpimg.imread("apple.jpg").copy()

# Convert RGB to Grayscale manually
if len(image.shape) == 3:
    gray = ((image[:, :, 0] +
             image[:, :, 1] +
             image[:, :, 2]) / 3).astype(np.uint8)
else:
    gray = image.astype(np.uint8)

height, width = gray.shape

# Gaussian Kernel
kernel = np.array([[1, 2, 1],
                   [2, 4, 2],
                   [1, 2, 1]])

filtered = gray.copy()

# Apply Gaussian Filter manually
for i in range(1, height - 1):
    for j in range(1, width - 1):

        total = 0

        for x in range(-1, 2):
            for y in range(-1, 2):
                total += int(gray[i + x, j + y]) * kernel[x + 1, y + 1]

        filtered[i, j] = total // 16

# Display Images
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(gray, cmap='gray')
plt.title("Original Image")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(filtered, cmap='gray')
plt.title("Gaussian Filter Output")
plt.axis("off")

plt.show()