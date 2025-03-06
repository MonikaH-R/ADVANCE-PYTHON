import cv2

image = cv2.imread("image.jpg.png",cv2.IMREAD_UNCHANGED)  # Ensure correct filename
cv2.imshow("Display Window", image)
cv2.waitKey(0)  # Corrected function name
cv2.destroyAllWindows()