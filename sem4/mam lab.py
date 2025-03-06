import cv2
import numpy as np
width, height=640,480
image=np.zeros((height,width,3), dtype=np.uint8)


top_left=(30,30)
bottom_right=(10,10)
red_color=(0,0,255)
cv2.rectangle(image, top_left, bottom_right, red_color, thickness=cv2.FILLED)

center=(300,300)
radius=50
green_color=(0,255,0)
cv2.circle(image, center, radius, green_color, thickness=cv2.FILLED)

cv2.imshow('Image with pixels', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''import cv2
import numpy as np
# Create a black image (512x512 pixels, 3 color channels)
image = np.zeros((512, 512, 3))
# Define red color (BGR format)
red = (0, 0, 255)
# Draw a red square (top-left corner at (100,100), bottom-right at (300,300))
cv2.rectangle(image, (100, 100), (300, 300), red, thickness=3)
# Draw a red circle (center at (400, 400), radius 50)
cv2.circle(image, (400, 400), 50, red, thickness=2)
# Display the image
cv2.imshow("Black Image with Shapes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Save the image (optional)
cv2.imwrite("shapes.jpg", image)'''