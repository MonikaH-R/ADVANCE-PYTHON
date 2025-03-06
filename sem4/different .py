import cv2

images_path = 'images.jpeg'
images = cv2.imread(images_path)
if images is None:
    print("Error: Unable to load image from {image_path}")
else:
    # Display the original image
    cv2.imshow('Original Image', images)
    # Convert the image to different color models
    gray_image = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
    hsv_image = cv2.cvtColor(images, cv2.COLOR_BGR2HSV)
    lab_image = cv2.cvtColor(images, cv2.COLOR_BGR2LAB)
    # Display the converted images
    cv2.imshow('Grayscale Image', gray_image)
    cv2.imshow('HSV Image', hsv_image)
    cv2.imshow('LAB Image', lab_image)

    # Wait for a key press and then close the windows
    cv2.waitKey(30000)
    cv2.destroyAllWindows()