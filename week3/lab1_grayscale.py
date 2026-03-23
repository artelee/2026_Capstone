import cv2

img = cv2.imread('Lenna.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Lenna Grayscale', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
