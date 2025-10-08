import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('src/ls11/origin.png')
img_noi = cv2.imread('src/ls11/noise.png')
img_cave = cv2.imread('src/ls11/cave.png')

kernel = np.ones((10, 10), np.uint8)

erosion_img = cv2.erode(img,kernel)
dilate_img = cv2.dilate(img,kernel)
open_img = cv2.morphologyEx(img_noi, cv2.MORPH_OPEN, kernel)
close_img = cv2.morphologyEx(img_cave, cv2.MORPH_CLOSE, kernel)
top_hat_img = cv2.morphologyEx(img_noi, cv2.MORPH_TOPHAT, kernel)
black_hat_img = cv2.morphologyEx(img_noi, cv2.MORPH_BLACKHAT, kernel)

plt.figure(figsize=(10, 6), dpi=100)
plt.rcParams['axes.unicode_minus'] = False


plt.subplot(331), plt.imshow(img), plt.title("Original")
plt.xticks([]), plt.yticks([])
plt.subplot(332), plt.imshow(erosion_img), plt.title("Erosion")
plt.xticks([]), plt.yticks([])
plt.subplot(333), plt.imshow(dilate_img), plt.title("Dilation")
plt.xticks([]), plt.yticks([])

plt.subplot(334), plt.imshow(img_noi), plt.title("Noise")
plt.xticks([]), plt.yticks([])
plt.subplot(335), plt.imshow(open_img), plt.title("Open Operation")
plt.xticks([]), plt.yticks([])
plt.subplot(336), plt.imshow(top_hat_img), plt.title("TopHat")
plt.xticks([]), plt.yticks([])

plt.subplot(337), plt.imshow(img_cave), plt.title("Cave")
plt.xticks([]), plt.yticks([])
plt.subplot(338), plt.imshow(close_img), plt.title("Close Operation")
plt.xticks([]), plt.yticks([])
plt.subplot(339), plt.imshow(black_hat_img), plt.title("BlackHat")
plt.xticks([]), plt.yticks([])

plt.show()