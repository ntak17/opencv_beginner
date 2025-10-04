import cv2

image = cv2.imread("src/1200.jpg")

B,G,R = cv2.split(image)

while True:
    cv2.imshow("Blue", B)
    cv2.imshow("Green", G)
    cv2.imshow("Red", R)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()