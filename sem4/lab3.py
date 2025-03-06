#write a python program to find the centre pixel co-ordinates of the uploaded image and set
#pixels to RED (BGR FORMAT)

import cv2
image = cv2.imread("white.jpeg")
height, width,_ = image.shape # shape returns (height, width, channels)
center_x = width//2
center_y = height// 2
image[center_y, center_x] = (0, 0, 255)
cv2.imshow("Modified white", image)
cv2.waitKey(0)
cv2.destroyAllWindows()