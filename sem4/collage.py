import cv2
import numpy as np

# Load images
image1 = cv2.imread("image1.jpeg")
image2 = cv2.imread("image.jpeg")
image3 = cv2.imread("images.jpeg")

# Resize images to same height
height = 200
image1 = cv2.resize(image1, (200, height))
image2 = cv2.resize(image2, (200, height))
image3 = cv2.resize(image3, (200, height))

# Stack images horizontally
collage = np.vstack([image1, image2, image3])

# Show and save collage
cv2.imshow("Collage", collage)
cv2.imwrite("collage.jpeg", collage)

cv2.waitKey(0)
cv2.destroyAllWindows()
