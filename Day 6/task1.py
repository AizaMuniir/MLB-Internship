#Task 1: Matrix Representation of an Image Read a grayscale image. Print its matrix representation. Display the image dimensions (Height × Width). Access and print the pixel values at different coordinates. Modify selected pixel values and display the updated image.

import cv2
import matplotlib.pyplot as plt
#Read an image
image = cv2.imread("apple.jpg", cv2.IMREAD_GRAYSCALE)
#Matrix Representation
print("Matrix Representation:")
print(image)
#Image Dimensions
height, width = image.shape
print("Height =", height)
print("Width =", width)
print("Image Dimension =", height * width)
#Random Pixel Values
print("Pixel (10,10):", image[10][10])
print("Pixel (50,20):", image[50][20])
print("Pixel (100,100):", image[100][100])
#Modified Pixel Values
image[10][10] = 255
image[50][20] = 0
#Display Modified Pixel Values
print("Pixel (10,10):", image[10][10])
print("Pixel (50,20):", image[50][20])
#Display updated image
plt.imshow(image, cmap="gray")
plt.title("Modified Image")
plt.axis("off")
plt.show()