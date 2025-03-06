import cv2
import numpy as np
# Load an image
image1 = cv2.imread("image1.jpeg")
image1 = cv2.resize(image1, (500, 500))  # Resize for better visualization
# Function to update color changes
def update_color(x):
    # Get current trackbar positions
    r = cv2.getTrackbarPos("Red", "Color Adjuster")
    g = cv2.getTrackbarPos("Green", "Color Adjuster")
    b = cv2.getTrackbarPos("Blue", "Color Adjuster")
 # Create a new image with modified colors
    modified_image = np.zeros_like(image1)
    modified_image[:, :, 0] = np.clip(image1[:, :, 0] + b, 0, 255)  # Blue
    modified_image[:, :, 1] = np.clip(image1[:, :, 1] + g, 0, 255)  # Green
    modified_image[:, :, 2] = np.clip(image1[:, :, 2] + r, 0, 255)  # Red

    cv2.imshow("Color Adjuster", modified_image)
# Create a window
cv2.namedWindow("Color Adjuster")
# Create trackbars for RGB adjustments
cv2.createTrackbar("Red", "Color Adjuster", 0, 255, update_color)
cv2.createTrackbar("Green", "Color Adjuster", 0, 255, update_color)
cv2.createTrackbar("Blue", "Color Adjuster", 0, 255, update_color)
# Show the original image first
cv2.imshow("Color Adjuster", image1)
cv2.waitKey(0)
cv2.destroyAllWindows()
