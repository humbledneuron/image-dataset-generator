# import cv2 as cv

# def rotate_image(img, angle, rotPoint=None):
#     (height, width) = img.shape[:2]  # Get image dimensions

#     if rotPoint is None:
#         rotPoint = (width // 2, height // 2)  # Rotate around the center of the image

#     # Generate the rotation matrix
#     rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)  # 1.0 means no scaling
#     dimensions = (width, height)  # Width first, then height

#     # Apply the rotation using the warpAffine function
#     rotated_image = cv.warpAffine(img, rotMat, dimensions)

#     return rotated_image

# # Load the image
# # img = cv.imread('path/to/your/image.jpg')
# img = cv.imread('/media/pr3cash/825206905206895D/BHaSH/GHub/py_learn/fcc/opencv/Photos/park.jpg')

# # Check if the image was successfully loaded
# if img is not None:
#     rotated_img = rotate_image(img, 45)  # Rotate the image by 45 degrees
#     cv.imshow("Rotated Image", rotated_img)  # Display the rotated image
#     cv.waitKey(0)  # Wait indefinitely for a key press
#     cv.destroyAllWindows()  # Close the image window
# else:
#     print("Error: Could not load the image.")


import cv2 as cv
import numpy as np

def rotate_image_with_expanded_canvas(img, angle):
    (height, width) = img.shape[:2]

    # Calculate the center of the image
    rotPoint = (width // 2, height // 2)

    # Get the rotation matrix for the specified angle
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)

    # Calculate the new bounding dimensions of the image after rotation
    cos = np.abs(rotMat[0, 0])
    sin = np.abs(rotMat[0, 1])

    new_width = int((height * sin) + (width * cos))
    new_height = int((height * cos) + (width * sin))

    # Adjust the rotation matrix to take into account the translation
    rotMat[0, 2] += (new_width / 2) - rotPoint[0]
    rotMat[1, 2] += (new_height / 2) - rotPoint[1]

    # Perform the actual rotation and return the image
    rotated_image = cv.warpAffine(img, rotMat, (new_width, new_height))

    return rotated_image

# Load the image
# img = cv.imread('path/to/your/image.jpg')
img = cv.imread('/media/pr3cash/825206905206895D/BHaSH/GHub/py_learn/fcc/opencv/Photos/park.jpg')

# Check if the image was successfully loaded
if img is not None:
    rotated_img = rotate_image_with_expanded_canvas(img, 45)  # Rotate the image by 45 degrees
    cv.imshow("Rotated Image", rotated_img)  # Display the rotated image
    cv.waitKey(0)  # Wait indefinitely for a key press
    cv.destroyAllWindows()  # Close the image window
else:
    print("Error: Could not load the image.")
