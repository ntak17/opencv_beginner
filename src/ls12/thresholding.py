import cv2

image = cv2.imread("src/ls12/1200.jpg")

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, img2 = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)

# image_gray: là hình ảnh cần xử cần import vào ảnh xám
# 127: là giá trị của thresh
# 255: là giá trị của thứ ba khi mà cuối được set “THRESH_BINARY”, “THRESH_BINARY_INV”. Nó đề cập đến giá trị mới
# được gắn khi giá trị xám của các điểm ảnh trong ảnh lớn hơn hay nhỏ hơn ngưỡng
# ret là giá trị ngưỡng được dùng ở đây bằng 127 
# image là ảnh nhị phân kết quả toàn 0 hoặc 255
# cv2.THRESH_BINARY set giá trị lớn hơn threshold được đặt như giá trị max
# cv2.THRESH_BINARY_INV: giá trị lớn hơn threahold sẽ được set là 0 và phần còn lại là max
# cv2.THRESH_TRUNC: phần lớn nhất sẽ được set bằng với threshold và phần nhỏ hơn threshold ngưỡng không thay đổi
# cv2.THRESH_TOZERO: phần lớn hơn threshold được set bằng threshold và phần nhỏ hơn sẽ được set là 0\
# cv2.THRESH_TOZERO_INV: phần lớn hơn threshold được set là 0 và phần nhỏ hơn sẽ không thay đổi
print(ret)
cv2.imshow("BINARY",image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()


