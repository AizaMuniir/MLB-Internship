import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("apple.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

copy = np.copy(img)

plt.imshow(copy)
plt.title("Copied Image")
plt.axis("off")
plt.show()

cv2.imwrite("copy.jpg", cv2.cvtColor(copy, cv2.COLOR_RGB2BGR))