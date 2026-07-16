import numpy as np
import matplotlib.image as mpimg

image = mpimg.imread("apple.jpg").copy()

image[50, 50] = [1, 0, 0]       
image[100, 100] = [0, 1, 0]     
image[150, 150] = [0, 0, 1]    
image[200, 200] = [1, 1, 0]     
image[250, 250] = [1, 0, 1]     

mpimg.imsave("modified_apple.jpg", image)

print("5 pixels modified and image saved successfully!")
