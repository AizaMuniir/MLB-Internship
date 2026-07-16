import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("apple.jpg")

if img is None:
    print("Error: Could not load apple.jpg")
    exit()

rgb = img[:, :, ::-1]

R = rgb[:, :, 0]
G = rgb[:, :, 1]
B = rgb[:, :, 2]

red = np.zeros_like(rgb)
green = np.zeros_like(rgb)
blue = np.zeros_like(rgb)

red[:, :, 0] = R
green[:, :, 1] = G
blue[:, :, 2] = B

merged = np.zeros_like(rgb)

merged[:, :, 0] = R
merged[:, :, 1] = G
merged[:, :, 2] = B

plt.figure(figsize=(15, 8))

plt.subplot(2, 3, 1)
plt.imshow(rgb)
plt.title("Original RGB")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(red)
plt.title("Red Channel")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(green)
plt.title("Green Channel")
plt.axis("off")

plt.subplot(2, 3, 4)
plt.imshow(blue)
plt.title("Blue Channel")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(merged)
plt.title("Merged Image")
plt.axis("off")

plt.tight_layout()
plt.show()