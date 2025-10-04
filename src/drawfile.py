import cv2 
img = cv2.imread("src/1200.jpg")
cv2.line(img, (0,0), (100,100), (255,0,0), 5)

cv2.rectangle(img, (100,100), (200,200), (0,255,0), 5)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()