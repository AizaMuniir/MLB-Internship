import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("apple.jpg")

if img is None:
    print("Image not found!")
    exit()

rgb = img[:, :, ::-1]

rgb_float = rgb.astype(np.float32) / 255

R = rgb_float[:, :, 0]
G = rgb_float[:, :, 1]
B = rgb_float[:, :, 2]

Cmax = np.maximum(np.maximum(R, G), B)
Cmin = np.minimum(np.minimum(R, G), B)

diff = Cmax - Cmin

H = np.zeros_like(Cmax)
S = np.zeros_like(Cmax)
V = Cmax

red = (Cmax == R) & (diff != 0)
green = (Cmax == G) & (diff != 0)
blue = (Cmax == B) & (diff != 0)

H[red] = (60 * ((G[red] - B[red]) / diff[red]) + 360) % 360

H[green] = 60 * ((B[green] - R[green]) / diff[green] + 2)

H[blue] = 60 * ((R[blue] - G[blue]) / diff[blue] + 4)

S[Cmax != 0] = diff[Cmax != 0] / Cmax[Cmax != 0]

mask = (
    (((H >= 0) & (H <= 10)) |
     ((H >= 170) & (H <= 180)))
    &
    (S > 0.3)
    &
    (V > 0.2)
)

segmented = np.zeros_like(rgb)

segmented[mask] = rgb[mask]

plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.imshow(rgb)
plt.title("Original Image")
plt.axis("off")


plt.subplot(1,3,2)
plt.imshow(mask, cmap="gray")
plt.title("Red Apple Mask")
plt.axis("off")


plt.subplot(1,3,3)
plt.imshow(segmented)
plt.title("Segmented Output")
plt.axis("off")


plt.tight_layout()
plt.show()