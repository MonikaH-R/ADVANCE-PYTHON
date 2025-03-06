import cv2
import numpy as np
def adjust_brightness(images_path, brightness_factor):
    """
    Adjusts the brightness of an image.
    :param images_path: Path to the input image
    :param brightness_factor: Factor to adjust brightness (-255 to 255)
    :return: Brightness adjusted image
    """
    # Read the image
    image = cv2.imread(images_path)
    if image is None:
        raise ValueError("Image not found or path is incorrect")

    # Convert image to float32 to prevent data loss
    image = np.float32(image)

    # Adjust brightness
    bright_image = np.clip(image + brightness_factor, 0, 255)

    # Convert back to uint8
    bright_images = np.uint8(bright_image)

    return bright_images


# Example usage
images_path = 'images.jpeg'  # Replace with your image path
brightness_factor = 50  # Increase brightness (use negative for decrease)

brightened_images = adjust_brightness(images_path, brightness_factor)

# Show images
cv2.imshow('Original Images', cv2.imread(images_path))
cv2.imshow('Brightened Images', brightened_images)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the result
cv2.imwrite('brightened_images.jpeg', brightened_images)
