import cv2
import os
import numpy as np


video_path = "/media/pr3cash/825206905206895D/BHaSH/GHub/image-dataset-generator/test_video_1.MOV"
# output_folder = "/media/pr3cash/825206905206895D/BHaSH/GHub/image-dataset-generator/Original/"

frame_interval = 5

base_path = os.getcwd()

data_set_path = os.path.join(base_path, "DataSet")
# if os.path.exists(data_set_path):
    # os.rmdir(data_set_path)

if not os.path.exists(data_set_path):
    os.mkdir(data_set_path)

original_imgs_path = os.path.join(data_set_path, "Original")
if not os.path.exists(original_imgs_path):
    os.mkdir(original_imgs_path)



def Original(video_path, flip_code=0, frame_interval=5):

    video = cv2.VideoCapture(video_path)

    frame_count = 0
    saved_frame_count = 0

    while True:
        ret, frame = video.read()

        # Break the loop if no more frames are available
        if not ret:
            break

        # Save only every `frame_interval`-th frame
        if frame_count % frame_interval == 0:
            # Flip the frame to correct orientation if needed
            if flip_code is not None:
                frame = cv2.flip(frame, flip_code)

            # Save the frame as an image
            output_path = os.path.join(original_imgs_path, f"Original_{saved_frame_count}.jpg")
            cv2.imwrite(output_path, frame)

            saved_frame_count += 1

        frame_count += 1

    video.release()


    print(f"Original Dataset with BGR created with {frame_count//frame_interval} frames.")

Original(video_path, frame_interval=frame_interval)
    
imgs_in_Oringal_path = []
#os.path.join(original_imgs_path, os.listdir(original_imgs_path))
    
for image in os.listdir(original_imgs_path):
    imgs_in_Oringal_path.append(os.path.join(original_imgs_path, image))


def FlippedHorizontally():
    FlippedHorizontally_imgs = os.path.join(data_set_path, "FlippedHorizontally")
    
    if not os.path.exists(FlippedHorizontally_imgs):
        os.mkdir(FlippedHorizontally_imgs)

    for index, img in enumerate(imgs_in_Oringal_path):
        img = cv2.imread(img)
        flip = cv2.flip(img, 1)
    
        output_path = os.path.join(FlippedHorizontally_imgs, f"FlippedHorizontally_{index}.jpg")
        cv2.imwrite(output_path, flip)

    print(f"Horizontally Flipped Dataset created with {index} frames.")

FlippedHorizontally()


def FlippedVertically():
    FlippedVertically_imgs = os.path.join(data_set_path, "FlippedVertically")
    
    if not os.path.exists(FlippedVertically_imgs):
        os.mkdir(FlippedVertically_imgs)

    for index, img in enumerate(imgs_in_Oringal_path):
        img = cv2.imread(img)
        flip = cv2.flip(img, 0)
    
        output_path = os.path.join(FlippedVertically_imgs, f"FlippedVertically_{index}.jpg")
        cv2.imwrite(output_path, flip)

    print(f"Vertically Flipped Dataset created with {index} frames.")

FlippedVertically()


def FlippedInverted():
    FlippedInverted_imgs = os.path.join(data_set_path, "FlippedInverted")
    
    if not os.path.exists(FlippedInverted_imgs):
        os.mkdir(FlippedInverted_imgs)

    for index, img in enumerate(imgs_in_Oringal_path):
        img = cv2.imread(img)
        flip = cv2.flip(img, -1)
    
        output_path = os.path.join(FlippedInverted_imgs, f"FlippedInverted_{index}.jpg")
        cv2.imwrite(output_path, flip)

    print(f"Invertedly Flipped Dataset created with {index} frames.")

FlippedInverted()

  
def GrayScale():
    GrayScale_imgs = os.path.join(data_set_path, "GrayScale")
    if not os.path.exists(GrayScale_imgs):
        os.mkdir(GrayScale_imgs)

    for index, img in enumerate(imgs_in_Oringal_path):
        img = cv2.imread(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
        output_path = os.path.join(GrayScale_imgs, f"GrayScale_{index}.jpg")
        cv2.imwrite(output_path, gray)

    print(f"GrayScale Dataset created with {index} frames.")
    

def Blur():
    Blur_imgs = os.path.join(data_set_path, "Blur")

    if not os.path.exists(Blur_imgs):
        os.mkdir(Blur_imgs)

    for index, img in enumerate(imgs_in_Oringal_path):
        img = cv2.imread(img)
        blur = cv2.GaussianBlur(img, (9,9), cv2.BORDER_DEFAULT)
    
        output_path = os.path.join(Blur_imgs, f"Blurred_{index}.jpg")
        cv2.imwrite(output_path, blur)

    print(f"Blurred Dataset created with {index} frames.")

Blur()


def ResizedHorizontal():
    ResizedHorizontal_imgs = os.path.join(data_set_path, "ResizedHorizontal")

    if not os.path.exists(ResizedHorizontal_imgs):
        os.mkdir(ResizedHorizontal_imgs)

   
    for index, img in enumerate(imgs_in_Oringal_path):

        # (height, width) = img.shape[:2]  
        # new_width = width * 2
        # new_height = height // 2

        img = cv2.imread(img)
        resize = cv2.resize(img, (900, 450), interpolation=cv2.INTER_CUBIC)
    
        output_path = os.path.join(ResizedHorizontal_imgs, f"ResizedHorizontal_{index}.jpg")
        cv2.imwrite(output_path, resize)

    print(f"Resized Horizontal Dataset created with {index} frames.")    

ResizedHorizontal()

def ResizedVertical():
    ResizedVertical_imgs = os.path.join(data_set_path, "ResizedVertical")

    if not os.path.exists(ResizedVertical_imgs):
        os.mkdir(ResizedVertical_imgs)

    for index, img in enumerate(imgs_in_Oringal_path):


        # height, width = img.shape[:2]  
        # new_width = width // 2
        # new_height = height * 2

        img = cv2.imread(img)
        resize = cv2.resize(img, (450, 900), interpolation=cv2.INTER_CUBIC)
    
        output_path = os.path.join(ResizedVertical_imgs, f"ResizedVertical_{index}.jpg")
        cv2.imwrite(output_path, resize)

    print(f"Resized Vertical Dataset created with {index} frames.")

ResizedVertical()

def rotate(img, angle):
    (height,width) = img.shape[:2]

    rotPoint = (width//2, height//2)

    rotMat = cv2.getRotationMatrix2D(rotPoint, angle, 1.0)

    # Calculate the new bounding dimensions of the image after rotation
    cos = np.abs(rotMat[0, 0])
    sin = np.abs(rotMat[0, 1])

    new_width = int((height * sin) + (width * cos))
    new_height = int((height * cos) + (width * sin))

    # Adjust the rotation matrix to take into account the translation
    rotMat[0, 2] += (new_width / 2) - rotPoint[0]
    rotMat[1, 2] += (new_height / 2) - rotPoint[1]

    # Perform the actual rotation and return the image
    rotated_image = cv2.warpAffine(img, rotMat, (new_width, new_height))

    return rotated_image

def Rotated(angle = 180):
    Rotated_imgs = os.path.join(data_set_path, "Rotated")
    
    if not os.path.exists(Rotated_imgs):
        os.mkdir(Rotated_imgs)

    for index, img in enumerate(imgs_in_Oringal_path):
        img = cv2.imread(img)
        rotated = rotate(img, angle)
    
        output_path = os.path.join(Rotated_imgs, f"{angle}_Degrees_Rotated_imgs_{index}.jpg")
        cv2.imwrite(output_path, rotated)

    print(f"{angle} Degrees Rotated Dataset created with {index} frames.")

angle = 45
Rotated(angle)
Rotated(90)
Rotated(180)
Rotated(270)

def HSV():
    HSV_imgs = os.path.join(data_set_path, "HSV")

    if not os.path.exists(HSV_imgs):
        os.mkdir(HSV_imgs)

    for index, img in enumerate(imgs_in_Oringal_path):
        img = cv2.imread(img)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
        output_path = os.path.join(HSV_imgs, f"HSV_imgs_{index}.jpg")
        cv2.imwrite(output_path, hsv)

    print(f"HSV Dataset created with {index} frames.")

HSV()

def LAB():
    LAB_imgs = os.path.join(data_set_path, "LAB")

    if not os.path.exists(LAB_imgs):
        os.mkdir(LAB_imgs)

    for index, img in enumerate(imgs_in_Oringal_path):
        img = cv2.imread(img)
        lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    
        output_path = os.path.join(LAB_imgs, f"LAB_imgs_{index}.jpg")
        cv2.imwrite(output_path, lab)

    print(f"LAB Dataset created with {index} frames.")

LAB()

def RGB():
    RGB_imgs = os.path.join(data_set_path, "RGB")

    if not os.path.exists(RGB_imgs):
        os.mkdir(RGB_imgs)

    for index, img in enumerate(imgs_in_Oringal_path):
        img = cv2.imread(img)
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
        output_path = os.path.join(RGB_imgs, f"RGB_imgs_{index}.jpg")
        cv2.imwrite(output_path, rgb)

    print(f"RGB Dataset created with {index} frames.")

RGB()