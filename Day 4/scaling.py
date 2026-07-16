import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("apple.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

factor = 2

new_h = int(img.shape[0] * factor)
new_w = int(img.shape[1] * factor)

scale = np.zeros((new_h, new_w, 3), dtype=img.dtype)

for y in range(new_h):
    for x in range(new_w):

        src_y = int(y / factor)
        src_x = int(x / factor)

        scale[y, x] = img[src_y, src_x]

plt.imshow(scale)
plt.axis("off")
plt.show()

cv2.imwrite("scale.jpg", cv2.cvtColor(scale, cv2.COLOR_RGB2BGR))