import numpy as np
import cv2 

img = cv2.imread("src/1200.jpg")

height, width = img.shape[:2]

res1 = cv2.resize(img, (int(width*1.2), int(height*1.2)), interpolation=cv2.INTER_CUBIC)
res2 = cv2.resize(img, (int(width*0.6), int(height*0.6)), interpolation=cv2.INTER_CUBIC)

cv2.imshow("src", img)
cv2.imshow("res1", res1)
cv2.imshow("res2", res2)

cv2.waitKey(0)
cv2.destroyAllWindows()