#Task 8: Stride Apply the same kernel using different stride values (1 and 2). Compare the output image size and explain how stride affects feature extraction.

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("apple.jpg", cv2.IMREAD_GRAYSCALE)

kernel = np.array([
    [-1,-1,-1],
    [-1, 8,-1],
    [-1,-1,-1]
])

def convolution_stride(image, kernel, stride):

    h, w = image.shape
    output_height = ((h - 3) // stride) + 1
    output_width = ((w - 3) // stride) + 1

    output = np.zeros((output_height, output_width))

    row = 0

    for i in range(0, h-2, stride):

        col = 0

        for j in range(0, w-2, stride):

            total = 0

            for ki in range(3):
                for kj in range(3):
                    total += image[i+ki][j+kj] * kernel[ki][kj]

            if total < 0:
                total = 0
            if total > 255:
                total = 255

            output[row][col] = total
            col += 1

        row += 1

    return output.astype(np.uint8)

output1 = convolution_stride(image, kernel, 1)
output2 = convolution_stride(image, kernel, 2)

print("Original Size :", image.shape)
print("Stride 1 Size :", output1.shape)
print("Stride 2 Size :", output2.shape)

plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.imshow(image, cmap="gray")
plt.title("Original")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(output1, cmap="gray")
plt.title("Stride = 1")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(output2, cmap="gray")
plt.title("Stride = 2")
plt.axis("off")

plt.show()

#Explanation
#Stride determines how many pixels the convolution kernel moves after each operation. 
#A stride of 1 preserves more spatial information and produces a larger output image. 
#A stride of 2 reduces the output dimensions and computational cost by skipping pixels, which may result in the loss of fine details.