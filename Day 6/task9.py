#Task 9: Padding Mathematics Implement Zero Padding manually. Implement Same Padding manually. Compare the image dimensions before and after padding. Explain why padding is required during convolution.

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("apple.jpg", 0)

pad = 1

h, w = image.shape

zero_padded = np.zeros((h + 2*pad, w + 2*pad), dtype=np.uint8)

for i in range(h):
    for j in range(w):
        zero_padded[i+pad][j+pad] = image[i][j]

print("Original Shape =", image.shape)
print("Zero Padded Shape =", zero_padded.shape)

plt.figure(figsize=(8,4))

plt.subplot(1,2,1)
plt.imshow(image, cmap="gray")
plt.title("Original")

plt.subplot(1,2,2)
plt.imshow(zero_padded, cmap="gray")
plt.title("Zero Padding")

plt.show()

#Explanation
#Zero padding adds zeros around the border of the image, increasing its dimensions. 
#Same padding uses enough padding to keep the output image the same size as the input after convolution. 
#Padding is important because it preserves edge information and prevents excessive shrinking of the image during repeated convolution operations.