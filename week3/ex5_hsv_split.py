import cv2

img = cv2.imread('Lenna.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(hsv)

cv2.imshow('Original', img)
cv2.imshow('H', h)
cv2.imshow('S', s)
cv2.imshow('V', v)

cv2.waitKey(0)
cv2.destroyAllWindows()
