import cv2
import matplotlib.pyplot as plt

image = cv2.imread("low_contrast.jpg", cv2.IMREAD_GRAYSCALE)

equalized = cv2.equalizeHist(image)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe_image = clahe.apply(image)

cv2.imwrite("equalized.jpg", equalized)
cv2.imwrite("clahe.jpg", clahe_image)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(image, cmap="gray")
plt.title("Original")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(equalized, cmap="gray")
plt.title("Histogram Equalization")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(clahe_image, cmap="gray")
plt.title("CLAHE")
plt.axis("off")

plt.show()

print("Task completed successfully!")