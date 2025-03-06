import cv2
# Open video file
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()  # Read frame-by-frame
    if not ret:
        break  # Break if video ends
    cv2.imshow('Video Frame', frame)
    # Display frame
    if cv2.waitKey(25) & 0xFF==ord('q'):  # Press 'q' to exit
        break


cap.release()
cv2.destroyAllWindows()