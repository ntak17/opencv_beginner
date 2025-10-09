import cv2
img = cv2.imread("src/ls13/images.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img2 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("GRAY_IMG",img2)
contours, hierarchy = cv2.findContours(img2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#Tham số mode cv2.RETR_TREE
#RETR_EXTERNAL = 0: CHỈ VIỀN NGOÀI CÙNG ĐƯỢC PHÁT HIỆN
#RETR_LIST = 1: phát hiện tất các những contours mà không cần xây dựng phân cấp và tất cả contours sẽ được đặt trong một list
#RETR_CCOMP = 2: phát hiện tất các contour và chia chúng thành 2 lớp
#RETR_TREE = 3: phát hiện bởi các lớp từ phải sang trái theo đường viền lưu trữ dạng cây 


#Tham số mode cv2.CHAIN_APPROX_SIMPLE
# CHAIN_APPROX_NONE: giữ nguyên các điểm trên đường viền
# CHAIN_APPROX_SIMPLE: nén phần ngang dọc và xiên chỉ giữ lại toạ độ của chúng



img3 = cv2.drawContours(img, contours, -1, (0,255,255), 3)
#img: ảnh gốc 
#contours: danh sách các đường viền tìm được từ cv2.findContours
#contourIdx: vẽ tất cả các contour dùng -1
#color BGR màu sắc của đường
#3 độ dày của nét vẽ 
cv2.imshow("BINARY", img)


cv2.waitKey(0)
cv2.destroyAllWindows()