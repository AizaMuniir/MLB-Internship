#Task 4: Euclidean Distance Select multiple pairs of image coordinates. Calculate the Euclidean distance between each pair manually. Verify your calculations with Python's math functions.
import math
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("apple.jpg")

pairs = [
((10,20),(40,60)),
((100,30),(150,70)),
((20,120),(90,160))
]

for p1,p2 in pairs:

    x1,y1=p1
    x2,y2=p2

    manual=((x2-x1)**2+(y2-y1)**2)**0.5

    verify=math.dist(p1,p2)

    print(manual,verify)