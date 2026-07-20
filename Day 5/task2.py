import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image = mpimg.imread("apple.jpg")

if len(image.shape) == 3:
    height = image.shape[0]
    width = image.shape[1]

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

height = gray.shape[0]
width = gray.shape[1]

for i in range(height):
    for j in range(width):
        intensity = gray[i, j]
        histogram[intensity] += 1

print("Histogram:")
for i in range(256):
    print(f"Intensity {i}: {histogram[i]}")

plt.figure(figsize=(8,5))
plt.bar(range(256), histogram, width=1)
plt.title("Manual Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")
plt.show()