import cv2
import numpy as np

# Load three different images
image = cv2.imread("image.jpeg")
image1 = cv2.imread("image1.jpeg")
images = cv2.imread("images.jpeg")

# Resize images to ensure they have the same dimensions
image = cv2.resize(image, (300, 300))
image1 = cv2.resize(image1, (300, 300))
images = cv2.resize(images, (300, 300))

# Concatenate images horizontally
combined_image = np.hstack((image, image1, images))

# Display the combined image
cv2.imshow("Three Images Side by Side", combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
