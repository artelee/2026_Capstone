import os
import cv2
import numpy as np

dir_path = os.path.dirname(os.path.abspath(__file__))
img = cv2.imread(os.path.join(dir_path, 'candies.png'))
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red1 = np.array([0, 50, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 50, 50])
upper_red2 = np.array([180, 255, 255])

mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = mask1 | mask2

result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('Original', img)
cv2.imshow('Mask', mask)
cv2.imshow('Red Candy', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
