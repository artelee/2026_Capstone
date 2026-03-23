import cv2
import matplotlib.pyplot as plt

img = cv2.imread('Lenna.png')

colors = ('b', 'g', 'r')
plt.figure()
plt.title('BGR Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

for i, color in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)

plt.xlim([0, 256])
plt.show()
