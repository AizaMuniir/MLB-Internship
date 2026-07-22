#Task 10: Build a Mini Image Processing Pipeline Create a complete pipeline that performs the following: Read a grayscale image. Apply manual padding. Perform manual convolution using a selected kernel. Apply different stride values. Display and compare all intermediate and final outputs. Briefly explain the result of each processing step.

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the grayscale image
image = cv2.imread("apple.jpg", cv2.IMREAD_GRAYSCALE)

# Sharpen kernel for convolution
kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

# Get original image size
h, w = image.shape

# Create a new image with one-pixel border (Zero Padding)
padded = np.zeros((h + 2, w + 2), dtype=np.uint8)

# Copy original image into the center of padded image
for i in range(h):
    for j in range(w):
        padded[i + 1][j + 1] = image[i][j]

# Function to perform manual convolution
def convolution(image, kernel, stride):

    h, w = image.shape

    # Calculate output image size
    output_h = ((h - 3) // stride) + 1
    output_w = ((w - 3) // stride) + 1

    output = np.zeros((output_h, output_w))

    row = 0

    # Move kernel over image according to stride
    for i in range(0, h - 2, stride):

        col = 0

        for j in range(0, w - 2, stride):

            total = 0

            # Multiply each kernel value with corresponding image pixel
            for ki in range(3):
                for kj in range(3):
                    total += image[i + ki][j + kj] * kernel[ki][kj]

            # Keep pixel values between 0 and 255
            if total < 0:
                total = 0
            elif total > 255:
                total = 255

            output[row][col] = total
            col += 1

        row += 1

    return output.astype(np.uint8)

# Apply convolution using stride = 1
output_stride1 = convolution(padded, kernel, 1)

# Apply convolution using stride = 2
output_stride2 = convolution(padded, kernel, 2)

# Print image sizes
print("Original Image Size:", image.shape)
print("Padded Image Size:", padded.shape)
print("Stride 1 Output Size:", output_stride1.shape)
print("Stride 2 Output Size:", output_stride2.shape)

# Display all processing steps
plt.figure(figsize=(12, 8))

# Original image
plt.subplot(2, 2, 1)
plt.imshow(image, cmap="gray")
plt.title("Original Image")
plt.axis("off")

# Image after zero padding
plt.subplot(2, 2, 2)
plt.imshow(padded, cmap="gray")
plt.title("Padded Image")
plt.axis("off")

# Convolution result with stride 1
plt.subplot(2, 2, 3)
plt.imshow(output_stride1, cmap="gray")
plt.title("Stride = 1")
plt.axis("off")

# Convolution result with stride 2
plt.subplot(2, 2, 4)
plt.imshow(output_stride2, cmap="gray")
plt.title("Stride = 2")
plt.axis("off")

plt.show()

#Explanation
#The grayscale image is loaded.
#Padding: A 1-pixel border of zeros is added around the image.
#Convolution: A sharpening kernel is applied manually using nested loops.
#Stride 1: The kernel moves one pixel at a time, producing a larger output with more detail.
#Stride 2: The kernel moves two pixels at a time, producing a smaller output with less detail.
#Result: All intermediate and final images are displayed to compare the effects of padding and different stride values.