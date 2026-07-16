import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("apple.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

minimum = img.min()
maximum = img.max()

normalize = ((img - minimum) / (maximum - minimum)) * 255
normalize = normalize.astype(np.uint8)

plt.imshow(normalize)
plt.axis("off")
plt.show()

cv2.imwrite("normalize.jpg", cv2.cvtColor(normalize, cv2.COLOR_RGB2BGR))