# import cv2
# import os

# def create_dataset(video_path, output_folder, flip_code=0):
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     video = cv2.VideoCapture(video_path)

#     frame_count = 0
#     while True:
#         ret, frame = video.read()

#         # Break the loop if no more frames are available
#         if not ret:
#             break

#         # Flip the frame to correct orientation
#         if flip_code is not None:
#             frame = cv2.flip(frame, flip_code)

#         # Save the frame as an image
#         output_path = os.path.join(output_folder, f"frame_{frame_count}.jpg")
#         cv2.imwrite(output_path, frame)

#         frame_count += 1

#     video.release()

#     print(f"Dataset created with {frame_count} frames.")

# dirs = ["Original", "Inverted", "Flipped", "InvertedFlipped", "Gray", "Blur", "ResizedSmall", "ResizedBig", "Rotated"]

# video_path = "/media/pr3cash/825206905206895D/BHaSH/GHub/image-dataset-generator/test_video_1.MOV"
# output_folder = "/media/pr3cash/825206905206895D/BHaSH/GHub/image-dataset-generator/assets/"
# create_dataset(video_path, output_folder)



#the below will get only nth frame

import cv2
import os

def create_dataset(video_path, output_folder, flip_code=0, frame_interval=5):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    video = cv2.VideoCapture(video_path)

    frame_count = 0
    saved_frame_count = 0

    while True:
        ret, frame = video.read()

        if not ret:
            break

        # Save only every `frame_interval`-th frame
        if frame_count % frame_interval == 0:
            # Flip the frame to correct orientation if needed
            if flip_code is not None:
                frame = cv2.flip(frame, flip_code)

            # Save the frame as an image
            output_path = os.path.join(output_folder, f"frame_{saved_frame_count}.jpg")
            cv2.imwrite(output_path, frame)

            saved_frame_count += 1

        frame_count += 1

    video.release()

    print(f"Dataset created with {saved_frame_count} frames.")

# Example usage
video_path = "/media/pr3cash/825206905206895D/BHaSH/GHub/image-dataset-generator/test_video_1.MOV"
output_folder = "/media/pr3cash/825206905206895D/BHaSH/GHub/image-dataset-generator/assets/"

# Set the frame interval to 7
frame_interval = 7

create_dataset(video_path, output_folder, frame_interval=frame_interval)
