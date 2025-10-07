import cv2
import numpy as np
import matplotlib.pyplot as plt

# IMAGE READING
img = cv2.imread('src/ls9/noise.jpg')

# IMAGE FILTERING
mean = cv2.blur(img, (5, 5))
grass = cv2.GaussianBlur(img, (5, 5), 1)
median = cv2.medianBlur(img, 5)

# IMAGE DISPLAY
plt.figure(figsize=(10, 5), dpi=100)
plt.rcParams['axes.unicode_minus'] = False
plt.subplot(141), plt.imshow(img), plt.title("Original")
plt.xticks([]), plt.yticks([])
plt.subplot(142), plt.imshow(mean), plt.title("Mean filtering")
plt.xticks([]), plt.yticks([])
plt.subplot(143), plt.imshow(grass), plt.title("Gauss filtering")
plt.xticks([]), plt.yticks([])
plt.subplot(144), plt.imshow(median), plt.title("Median filtering")
plt.xticks([]), plt.yticks([])
plt.show()