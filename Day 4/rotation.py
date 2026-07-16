import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("apple.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

h, w = img.shape[:2]

rotate = np.zeros((w, h, 3), dtype=img.dtype)

for y in range(h):
    for x in range(w):
        rotate[x, h-1-y] = img[y, x]

plt.imshow(rotate)
plt.axis("off")
plt.show()

cv2.imwrite("rotate.jpg", cv2.cvtColor(rotate, cv2.COLOR_RGB2BGR))