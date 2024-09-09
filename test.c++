#include <opencv2/opencv.hpp>
#include <iostream>
#include <filesystem>
#include <vector>

namespace fs = std::filesystem;

// Function to create a directory if it doesn't exist
void create_directory_if_not_exists(const std::string& path) {
    if (!fs::exists(path)) {
        fs::create_directory(path);
    }
}

// Function to rotate an image by a specified angle
cv::Mat rotate_image(const cv::Mat& img, double angle) {
    cv::Point2f center(img.cols / 2.0, img.rows / 2.0);
    cv::Mat rotMat = cv::getRotationMatrix2D(center, angle, 1.0);
    cv::Rect bbox = cv::RotatedRect(cv::Point2f(), img.size(), angle).boundingRect();
    rotMat.at<double>(0, 2) += bbox.width / 2.0 - img.cols / 2.0;
    rotMat.at<double>(1, 2) += bbox.height / 2.0 - img.rows / 2.0;
    cv::Mat rotated;
    cv::warpAffine(img, rotated, rotMat, bbox.size());
    return rotated;
}

// Function to rotate all images in a folder
void rotate_images_in_folder(const std::string& input_folder, const std::string& output_folder, double angle) {
    create_directory_if_not_exists(output_folder);

    for (const auto& entry : fs::directory_iterator(input_folder)) {
        if (entry.is_regular_file()) {
            cv::Mat img = cv::imread(entry.path().string());
            if (img.empty()) continue;

            cv::Mat rotated_img = rotate_image(img, angle);
            std::string output_path = output_folder + "/" + fs::path(entry.path()).stem().string() + "_Rotated_" + std::to_string(angle) + ".jpg";
            cv::imwrite(output_path, rotated_img);
        }
    }
}

// Function to apply a series of rotations to images
void apply_rotations(const std::string& input_folder, const std::string& output_folder) {
    for (int i = 0; i < 360; ++i) {
        rotate_images_in_folder(input_folder, output_folder, i);
    }
}

int main() {
    std::string base_path = fs::current_path().string();
    std::string data_set_product = "Short_videos";
    std::string data_set_name = "IMG_7835(1)";

    std::string data_set_path = base_path + "/" + data_set_product + "/" + data_set_name + "_DataSet";
    create_directory_if_not_exists(data_set_path);

    std::string original_imgs_path = data_set_path + "/Original";
    create_directory_if_not_exists(original_imgs_path);

    // Assuming images are already extracted and stored in original_imgs_path

    // Rotate images
    std::string rotated_imgs_path = data_set_path + "/Rotated";
    apply_rotations(original_imgs_path, rotated_imgs_path);

    return 0;
}


// g++ -o process_video test.c++ `pkg-config --cflags --libs opencv4`
