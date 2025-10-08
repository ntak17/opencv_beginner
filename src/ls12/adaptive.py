import cv2
img = cv2.imread("src/ls12/1200.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img2 = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 3)

# adaptiveThreshold: hàm này được sử dụng khi ảnh có ánh sáng không đồng đều ví dụ ảnh có chỗ sáng và chỗ tối, việc chọn ngưỡng sẽ không hiệu quả
# img_gray: ảnh đầu vào dạng grayscale
# 255 giá trị ngưỡng đúng thường là trắn
# cv2.ADAPTIVE_THRESH_MEAN_C là phương pháp tính ngưỡng cục bộ, đặt giá trị của tất cả pixel lân cận như nhau
# cv2.ADAPTIVE_THRESH_GAUSSIAN_C: chứa giá trị của tất cả pixcel trong các pixel lân cận và mục tiêu pixel, khoảng cách ngắn nhất, giá trị sẽ càng cao. Khoảng cách càng lớn giá trị càng nhỏ
# thresh binary kiểu ngưỡng 
# 5 kích thước ngưỡng vùng lân cận
# 3 giá trị C hằng số trừ đi từ ngưỡng tính được


cv2.imshow("BINARY", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
