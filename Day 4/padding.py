import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("apple.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

pad = 50

h, w = img.shape[:2]

padding = np.zeros((h+2*pad, w+2*pad, 3), dtype=img.dtype)

padding[pad:pad+h, pad:pad+w] = img

plt.imshow(padding)
plt.axis("off")
plt.show()

cv2.imwrite("padding.jpg", cv2.cvtColor(padding, cv2.COLOR_RGB2BGR))