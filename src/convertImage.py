import cv2

img = cv2.imread("src/1200.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()