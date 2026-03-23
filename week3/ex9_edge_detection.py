import cv2
import numpy as np

img = cv2.imread('desert.JPG')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.array([[0,  1, 0],
                   [1, -4, 1],
                   [0,  1, 0]])

edges = cv2.filter2D(gray, -1, kernel)

cv2.imshow('Original', img)
cv2.imshow('Edges', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
