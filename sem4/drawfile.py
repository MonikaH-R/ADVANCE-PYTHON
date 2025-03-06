import numpy as np
import cv2

# Create a black image
width, height = 640, 480
images = np.zeros((height, width, 3), dtype=np.uint8)

# Draw a red square
top_left = (30, 30)
bottom_right = (10, 10)
red_color = (0, 0, 255)
cv2.rectangle(images, top_left, bottom_right, red_color,
              thickness=cv2.FILLED)

# Draw a green circle
center = (300, 300)
radius = 50
green_color = (0, 255, 0)
cv2.circle(images, center, radius, green_color,
           thickness=cv2.FILLED)

# Display the image
cv2.imshow('Images with Pixels', images)
cv2.waitKey(0)
cv2.destroyAllWindows()