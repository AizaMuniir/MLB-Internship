#Task 3: Pixel Intensity Analysis Find the minimum, maximum, and average pixel intensity of a grayscale image. Count how many pixels belong to different intensity ranges (0–50, 51–100, 101–150, 151–200, 201–255). Visualize the intensity distribution.

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
image = cv2.imread("apple.jpg", 0)

# Min, Max, Mean
minimum = image.min()
maximum = image.max()
average = image.mean()

print("Minimum =", minimum)
print("Maximum =", maximum)
print("Average =", average)

# Fast range counting using NumPy masks (no manual pixel loop needed)
ranges = [
    np.sum((image >= 0)   & (image <= 50)),
    np.sum((image >= 51)  & (image <= 100)),
    np.sum((image >= 101) & (image <= 150)),
    np.sum((image >= 151) & (image <= 200)),
    np.sum((image >= 201) & (image <= 255)),
]

print("Pixel counts per range:", ranges)

# Labels for the 5 ranges, in order, with 0-50 at index 0
labels = ["0-50", "51-100", "101-150", "151-200", "201-255"]

# Bar chart of the 5 custom ranges
plt.figure(figsize=(8, 5))
plt.bar(labels, ranges, color="gray", edgecolor="black")
plt.title("Pixel Intensity Distribution (5 Ranges)")
plt.xlabel("Intensity Range")
plt.ylabel("Number of Pixels")
plt.show()