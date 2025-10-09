import cv2

img =cv2.imread("src/ls13/test.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img2= cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy= cv2.findContours(img2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[1]
# lấy coutours 1
approx1 = cv2.approxPolyDP(cnt, 20, False)
# tham số đầu tiên là một curve để thuật toán tìm kiếm
# tham số thứ 2 biểu thị độ chính xác. Số càng nhỏ độ chính xác càng giảm và nếu nhiều thì độ chính xác càng cao
# tham số thứ 3 closed quyết đinh contour là đóng hay không, Nếu có đặt nó là đúng nếu không đặt là false

img3 = cv2.drawContours(img, [approx1],-1, (255,0,0),3)

cv2.imshow("BINARY",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

