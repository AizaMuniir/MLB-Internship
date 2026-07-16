import cv2
import matplotlib.pyplot as plt

img = cv2.imread("apple.jpg")

if img is None:
    print("Error: Could not load apple.jpg")
    exit()

rgb = img[:, :, ::-1]

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("BGR (Incorrect Colors)")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(rgb)
plt.title("RGB : Correct Colors")
plt.axis("off")

plt.tight_layout()
plt.show()