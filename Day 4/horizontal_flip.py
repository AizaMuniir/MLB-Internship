import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("apple.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

h, w = img.shape[:2]

flip = np.zeros_like(img)

for y in range(h):
    for x in range(w):
        flip[y, w-1-x] = img[y, x]

plt.imshow(flip)
plt.axis("off")
plt.show()

cv2.imwrite("flip.jpg", cv2.cvtColor(flip, cv2.COLOR_RGB2BGR))