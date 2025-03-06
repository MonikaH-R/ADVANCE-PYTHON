import cv2
import numpy as np

# Load images
img1 = cv2.imread("image.jpeg")
img2 = cv2.imread("image1.jpeg")

# Ensure both images have the same width
width = min(img1.shape[1], img2.shape[1])
img1 = cv2.resize(img1, (width, img1.shape[0]))
img2 = cv2.resize(img2, (width, img2.shape[0]))

# Stack images vertically
v_stacked = cv2.vconcat([img1, img2])

# Display and save the stacked image
cv2.imshow("Vertical Stacked", v_stacked)
cv2.imwrite("v_stacked.jpeg", v_stacked)
cv2.waitKey(0)
cv2.destroyAllWindows()
