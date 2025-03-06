# create black image with red rectangle and green circle on the black image
import numpy as np
import cv2

# Create a black image (500x500 pixels, 3 color channels for RGB)
image = np.zeros((500, 500, 3), dtype=np.uint8)

# Define the rectangle (top-left corner, bottom-right corner, color, thickness)
cv2.rectangle(image, (100, 100), (400, 300), (0, 0, 255), -1)  # Red rectangle (BGR format)

# Define the circle (center, radius, color, thickness)
cv2.circle(image, (250, 400), 50, (0, 255, 0), -1)  # Green circle

# Display the image
cv2.imshow("Black Image with Red Rectangle and Green Circle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Optionally, save the image
cv2.imwrite("black_image_with_shapes.png", image)
