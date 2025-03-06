import cv2

image = cv2.imread("image.jpg.png")  # Ensure correct filename
cv2.imwrite("output.jpg",image)
cv2.imshow("Display Window", image)
cv2.waitKey(0)  # Corrected function name
cv2.destroyAllWindows() # color bgr  not as rgb