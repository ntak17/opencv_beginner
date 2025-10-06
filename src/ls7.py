import cv2
import numpy as np

img = cv2.imread("src/1200.jpg")

GRAY = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
LAB = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
YCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

cv2.imshow("src", img)
cv2.imshow("GRAY", GRAY)
cv2.imshow("HSV", HSV)
cv2.imshow("LAB", LAB)
cv2.imshow("YCrCb", YCrCb)

cv2.waitKey(0)
cv2.destroyAllWindows()