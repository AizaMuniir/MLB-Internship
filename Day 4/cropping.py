import cv2
import matplotlib.pyplot as plt

img = cv2.imread("apple.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

crop = img[50:250, 50:250]

plt.imshow(crop)
plt.axis("off")
plt.show()

cv2.imwrite("crop.jpg", cv2.cvtColor(crop, cv2.COLOR_RGB2BGR))