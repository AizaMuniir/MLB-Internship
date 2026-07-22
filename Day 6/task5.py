#Task 5: Manhattan Distance Calculate the Manhattan distance for the same coordinate pairs used in Task 4. Compare the Euclidean and Manhattan distances. Explain in which situations each distance metric is more suitable.

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

    manhattan=abs(x2-x1)+abs(y2-y1)

    euclidean=((x2-x1)**2+(y2-y1)**2)**0.5

    print("Euclidean =",euclidean)
    print("Manhattan =",manhattan)

#Explanation
#Euclidean is Straight-line distance and used in geometry, clustering, object detection.
#Manhattan is grid distance used in city-block navigation and path planning.