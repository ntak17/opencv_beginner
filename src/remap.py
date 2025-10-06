import cv2
import numpy as np


img = cv2.imread("src/1200.jpg")

rows, cols, ch = img.shape

mapx = np.ones((rows, cols), np.float32)
mapy = np.ones((rows, cols), np.float32)
print(mapx)

for i in range(rows):

    for j in range(cols):
        mapx.itemset((i, j),j)
        mapy.itemset((i, j), i*2)


dst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

cv2.imshow("src", img)
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows() 