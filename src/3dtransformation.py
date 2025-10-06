import cv2
import numpy as np

img = cv2.imread("src/1200.jpg")

rows, cols = img.shape[:2]

print(rows, cols)

pts1= np.float32([[150,50],[400,50],[60,450],[310, 450]])
pts2= np.float32([[50,50],[rows - 50 ,50],[50,cols-50],[rows - 50, cols - 50]])

M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(img, M, (cols, rows))

cv2.imshow("src", img)
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()