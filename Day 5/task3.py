import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image = mpimg.imread("apple.jpg")

if len(image.shape) == 3:
    height, width = image.shape[0], image.shape[1]
    gray = np.zeros((height, width), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            R = image[i, j, 0]
            G = image[i, j, 1]
            B = image[i, j, 2]
            gray[i, j] = int(0.299 * R + 0.587 * G + 0.114 * B)
else:
    gray = image.astype(np.uint8)

histogram = np.zeros(256, dtype=int)

for i in range(gray.shape[0]):
    for j in range(gray.shape[1]):
        intensity = gray[i, j]
        histogram[intensity] += 1

cdf = np.zeros(256, dtype=int)
cdf[0] = histogram[0]

for i in range(1, 256):
    cdf[i] = cdf[i - 1] + histogram[i]

cdf_min = 0

for value in cdf:
    if value != 0:
        cdf_min = value
        break

total_pixels = gray.shape[0] * gray.shape[1]

normalized_cdf = np.zeros(256, dtype=np.uint8)

for i in range(256):
    normalized_cdf[i] = round(((cdf[i] - cdf_min) / (total_pixels - cdf_min)) * 255)

equalized = np.zeros_like(gray)

for i in range(gray.shape[0]):
    for j in range(gray.shape[1]):
        equalized[i, j] = normalized_cdf[gray[i, j]]

mpimg.imsave("equalized_image.png", equalized, cmap="gray")

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(gray, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(equalized, cmap="gray")
plt.title("Equalized Image")
plt.axis("off")

plt.show()

print("Histogram Equalization Completed Successfully!")