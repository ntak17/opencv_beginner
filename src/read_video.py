import cv2

cap = cv2.VideoCapture("src/videoplayback.mp4")

if not cap.isOpened():
    print("❌ Không mở được video")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:  # hết video hoặc lỗi đọc frame
        print("Đã hết video hoặc không đọc được frame.")
        break

    cv2.imshow('capture', frame)

    # bấm phím q để thoát
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()