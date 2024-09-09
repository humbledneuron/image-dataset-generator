import os

folders = ["IMG_7909", "IMG_7910", "IMG_7911", "IMG_7912", "IMG_7913", "IMG_7920", "IMG_79210", "IMG_7922"]

base_path = os.path.join(os.getcwd(), "final_DS")

imgs_folder_path = []


    


import cv2
import os
import numpy as np
import time 

# "IMG_7909"
data_set_product = os.path.join(os.getcwd(), "Cocacola")

data_set_folder =  os.listdir(data_set_product)

# new_data_set_folder = []

# for data_set_name in data_set_folder:
#     new_video_folder = os.path.join(data_set_product_name, "data_set_name")
#     new_data_set_folder.append(new_video_folder)



def imager(data_set_name, video_path):

    # output_folder = "/media/pr3cash/825206905206895D/BHaSH/GHub/image-dataset-generator/Original/"

    frame_interval = 30

    base_path = os.getcwd()

    # data_set_path = os.path.join(base_path, data_set_product, f"{data_set_name}_DataSet")
    data_set_path = os.path.join(data_set_product, f"{data_set_name}_DataSet")

    if not os.path.exists(data_set_path):
        os.mkdir(data_set_path)

    original_imgs_path = os.path.join(data_set_path, "Original")
    if not os.path.exists(original_imgs_path):
        os.mkdir(original_imgs_path)



    def Original(video_path, flip_code=-1, frame_interval=5):

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
                output_path = os.path.join(original_imgs_path, f"{data_set_name}_Original_{saved_frame_count}.jpg")
                cv2.imwrite(output_path, frame)

                saved_frame_count += 1

            frame_count += 1

        video.release()


        print(f"{data_set_name} Original Dataset with BGR created with {frame_count//frame_interval} frames.")

    Original(video_path, frame_interval=frame_interval)
        
    imgs_in_Oringal_path = []
    #os.path.join(original_imgs_path, os.listdir(original_imgs_path))
        
    for image in os.listdir(original_imgs_path):
        imgs_in_Oringal_path.append(os.path.join(original_imgs_path, image))


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

    def Rotated(angle = 90):
        Rotated_imgs = os.path.join(data_set_path, "Rotated")
        
        if not os.path.exists(Rotated_imgs):
            os.mkdir(Rotated_imgs)

        for index, img in enumerate(imgs_in_Oringal_path):
            img = cv2.imread(img)
            rotated = rotate(img, angle)
        
            # output_path = os.path.join(Rotated_imgs, f"{data_set_name}_{angle}_Degrees_Rotated_imgs_{index}.jpg")
            output_path = os.path.join(Rotated_imgs, f"{data_set_name}_{angle}_Degrees_Rotated_imgs_{index}.jpg")
            cv2.imwrite(output_path, rotated)

        print(f"{data_set_name} {angle} Degrees Rotated Dataset created with {index} frames.")

    angle = 90
    # Rotated(angle)
    # Rotated(0)
    # Rotated(180)

    # Rotated(90)
    # Rotated(270)
    # for i in range(359):
        # if i % 10 == 0:
            # Rotated(i)
            
for data_set_name in data_set_folder:
    # imgs_folder_path.append(os.path.join(os.getcwd(), f"{image}_DataSet"))
    video_path = f"/media/pr3cash/825206905206895D/BHaSH/GHub/image-dataset-generator/{data_set_product}/{data_set_name}.MOV"
    imager(data_set_name, video_path)
