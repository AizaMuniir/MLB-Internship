#Task 2: Coordinate System Mark the coordinates of different pixels on an image. Print the pixel value for each selected coordinate. Explain the difference between the image coordinate system (x, y) and the matrix indexing system (row, column)

import cv2
import matplotlib.pyplot as plt
#Read Image
image = cv2.imread("apple.jpg")
#Selected Coordinates
points = [(30,40), (80,120), (150,60)]
#Display Image
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
#Coordinates and Pixel value in Graph
for x, y in points:
    plt.scatter(x, y, color='red')
    # Display Coordinate Values
    plt.text(x+2, y+2, f"({x},{y})", color="blue")
    print("Coordinate:", (x,y),
          "Pixel Value:", image[y][x])
plt.show()
#Explanation
#The image coordinate system uses (x, y), while NumPy accesses the same pixel using image[y][x] because arrays are indexed as [row][column].