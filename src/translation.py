import numpy as np
import cv2 

img = cv2.imread("src/1200.jpg")

rows, cols, ch = img.shape

M = np.float32([[1,0,50],[0,1,50]])

dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow("src", img)
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()