import cv2
import numpy as np
import os

def calculate_brightness_contrast(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    brightness = np.mean(gray)
    contrast = np.std(gray)
    return brightness, contrast

def adjust_brightness_contrast(image, target_brightness, target_contrast):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    current_brightness = np.mean(gray)
    current_contrast = np.std(gray)
    
    # Adjust brightness
    brightness_adjusted = image + (target_brightness - current_brightness)
    
    # Adjust contrast
    contrast_adjusted = (brightness_adjusted - target_brightness) * (target_contrast / current_contrast) + target_brightness
    
    # Clip the values to [0, 255] and convert back to uint8
    contrast_adjusted = np.clip(contrast_adjusted, 0, 255).astype(np.uint8)
    
    return contrast_adjusted

def batch_process_images(input_dir, output_dir, reference_image_path):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Load reference image and calculate its brightness and contrast
    reference_image = cv2.imread(reference_image_path)
    target_brightness, target_contrast = calculate_brightness_contrast(reference_image)
    
    # Process each image in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):  # Adjust as per your file types
            file_path = os.path.join(input_dir, filename)
            image = cv2.imread(file_path)
            
            # Adjust brightness and contrast
            adjusted_image = adjust_brightness_contrast(image, target_brightness, target_contrast)
            
            # Save the adjusted image to the output directory
            output_path = os.path.join(output_dir, filename)
            cv2.imwrite(output_path, adjusted_image)
            print(f"Processed {filename}")

input_dir = "/media/pr3cash/825206905206895D/BHaSH/GHub/image-dataset-generator/La_serenísima/final_la_serenísima_copy/images_original/train"
output_dir = "/media/pr3cash/825206905206895D/BHaSH/GHub/image-dataset-generator/La_serenísima/final_la_serenísima_copy/images_brightness_converted_glossy/train"
reference_image_path = "/media/pr3cash/825206905206895D/BHaSH/GHub/freelance/bottles_classifier/converter_reference_glossy.png"

batch_process_images(input_dir, output_dir, reference_image_path)
