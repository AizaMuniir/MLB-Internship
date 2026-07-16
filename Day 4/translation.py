import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("apple.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

h, w = img.shape[:2]

tx = 100
ty = 50

translate = np.zeros_like(img)

for y in range(h):
    for x in range(w):

        new_x = x + tx
        new_y = y + ty

        if new_x < w and new_y < h:
            translate[new_y, new_x] = img[y, x]

plt.imshow(translate)
plt.axis("off")
plt.show()

cv2.imwrite("translate.jpg", cv2.cvtColor(translate, cv2.COLOR_RGB2BGR))