🔥 Flame Detection using YOLOv8
# Real-Time Flame Detection using YOLOv8
=======
Features:
1. Detect flames in images, videos, or webcam streams
2. Saves output images/videos with bounding boxes
3. Exports detection results (.txt) with class, confidence, and coordinates
4. Option to process large videos efficiently using stream=True

This project provides a complete solution for detecting flames in images and videos using a custom-trained YOLOv8 model. The system is designed for applications in fire safety, surveillance, and early-warning systems.

 <!-- You can replace this with a GIF of the video detection for a better effect -->

## Table of Contents
- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Model Results](#model-results)
- [Project Structure](#project-structure)
- [Installation Guide](#installation-guide)
- [How to Use](#how-to-use)
- [License](#license)
- [Acknowledgments](#acknowledgments)

<<<<<<< HEAD
## Project Overview

This repository contains Python scripts that leverage the Ultralytics YOLOv8 framework to perform object detection. A pre-trained model (`best.pt`) is used to identify and locate flames within a given image or video source. The scripts automatically save the annotated results, including output images/videos with bounding boxes and text files with detection coordinates.

## Key Features

- **High-Accuracy Detection:** Utilizes a custom-trained YOLOv8 model for robust flame detection.
- **Image & Video Support:** Capable of processing both static images and video files.
- **Saved Outputs:** Automatically saves annotated images, videos, and detection data (bounding box coordinates and confidence scores) in text files.
- **Easy to Use:** Simple and well-documented Python scripts for quick implementation.
- **Customizable:** Easily modify the source files, model, and output directories.

## Model Results

Here are some examples of the model's performance on different images.


| Original Image | Detected Flame |
| :---: | :---: |
| <img src="https://github.com/user-attachments/assets/ca6678f7-1e25-45c6-b370-79d315a1c60b" width="300"> | <img src="https://github.com/user-attachments/assets/cdcf130a-ad64-4ff3-9a36-a829b1d0cfaf" width="300"> |
| <img src="https://github.com/user-attachments/assets/bc40ea7c-db1e-4b6e-ad6b-13b9d626084f" width="300"> | <img src="https://github.com/user-attachments/assets/7ca1806a-3811-44af-803e-cd0afc31822d" width="300"> |

The model successfully identifies the flame regions with high confidence, drawing bounding boxes labeled "Api" (which you can change based on your class name).

## Project Structure

For the scripts to work correctly, organize your project folder as follows. This structure uses relative paths, which is recommended over absolute paths.

```
flame-detection-yolov8/
├── model/
│   └── best.pt                 # Your trained YOLOv8 model
├── source_file_img_video/
│   ├── fire.mp4
│   ├── fire2.jpg
│   └── Campfire by the River.mp4 # Your input images and videos
├── detect_flame.py             # Script for image detection
├── detect_flame_in_video.py    # Script for video detection
├── README.md                   # This file
└── requirements.txt            # Project dependencies
```

## Installation Guide

Follow these steps to set up the project environment.

**1. Prerequisites**
- Python 3.8 or higher
- `pip` package manager

**2. Clone the Repository**
```bash
git clone https://github.com/Al-Masrafi/Obj_detection.git
cd flame-detection-yolov8
```

**3. Create a Virtual Environment (Recommended)**
It's best practice to create a virtual environment to keep project dependencies isolated.
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**4. Install Dependencies**


Now, install these packages using pip:
```bash
pip install ultralytics torch opencv-python

```

**5. Place Your Model**
Download or place your trained `best.pt` model file inside the `model/` directory.

## How to Use

Before running, make sure you have updated the paths inside the Python scripts to match your file locations or, even better, modify them to use the relative paths shown in the [Project Structure](#project-structure) section.

### 1. Image Detection

The `detect_flame.py` script processes a single image.

- **Setup:** Open `detect_flame.py` and ensure the `model_path`, `image_path`, and `save_dir` variables point to the correct files and folders.
- **Run the script:**
  ```bash
  python detect_flame.py
  ```
- **Output:** The annotated image and a `.txt` file with detection data will be saved in a new directory like `source_file_img_video/predicted/`.

### 2. Video Detection

The `detect_flame_in_video.py` script processes a video file.

- **Setup:** Open `detect_flame_in_video.py` and ensure the `model_path`, `video_path`, and `save_dir` variables are set correctly.
- **Run the script:**
  ```bash
  python detect_flame_in_video.py
  ```
- **Output:** The processed video with bounding boxes and a `labels` folder containing `.txt` files for each frame will be saved in a new directory like `source_file_img_video/predicted_video/`.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments

- This project is built upon the powerful [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) library.
- Thanks to the creators of the datasets used for training the model.
