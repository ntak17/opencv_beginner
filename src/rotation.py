import cv2
import numpy as np

img = cv2.imread("src/1200.jpg")
rows, cols, ch= img.shape

M= cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
dst= cv2.warpAffine(img, M, (cols, rows))

cv2.imshow("src", img)
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()