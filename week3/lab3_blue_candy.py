import cv2
import numpy as np

img = cv2.imread('candies.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_blue = np.array([100, 50, 50])
upper_blue = np.array([140, 255, 255])

mask = cv2.inRange(hsv, lower_blue, upper_blue)
result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('Original', img)
cv2.imshow('Mask', mask)
cv2.imshow('Blue Candy', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
