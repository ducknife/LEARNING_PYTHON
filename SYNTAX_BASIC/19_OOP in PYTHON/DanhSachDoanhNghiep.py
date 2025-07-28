import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
ret, prev_frame = cap.read()
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

motion_threshold = 5000
no_motion_count = 0
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # So sánh chuyển động với frame trước
    diff = cv2.absdiff(gray, prev_gray)
    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
    motion = np.sum(thresh)

    if motion < motion_threshold:
        no_motion_count += 1
    else:
        no_motion_count = 0

    prev_gray = gray.copy()
    frame_count += 1

    # Đánh dấu khuôn mặt
    for (x, y, w, h) in faces:
        color = (0, 255, 0) if no_motion_count < 20 else (0, 0, 255)
        label = "Real" if no_motion_count < 20 else "Fake"
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    cv2.imshow("Face Spoof Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
