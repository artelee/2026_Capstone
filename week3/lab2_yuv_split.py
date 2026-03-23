import cv2

img = cv2.imread('Lenna.png')
yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

y, u, v = cv2.split(yuv)

cv2.imshow('Original', img)
cv2.imshow('Y', y)
cv2.imshow('U', u)
cv2.imshow('V', v)

cv2.waitKey(0)
cv2.destroyAllWindows()
