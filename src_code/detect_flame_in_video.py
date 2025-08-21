from ultralytics import YOLO
import os

# Paths
model_path = 'D:/Obj_detection/model/best.pt'  # Your trained flame detection model
# Input video 
# 1. video_path = 'D:/Obj_detection/source_file_img_video/fire.mp4'
# 2.video_path = 'D:/Obj_detection/source_file_img_video/Campfire by the River.mp4'
video_path = 'D:/Obj_detection/source_file_img_video/Campfire by the River.mp4'
save_dir = 'D:/Obj_detection/source_file_img_video'  # Folder to save results

# Load YOLO model
model = YOLO(model_path)

# Run inference on video
results = model.predict(
    source=video_path,
    save=True,          # Save output video with bounding boxes
    save_txt=True,      # Save detections for each frame in .txt files
    save_conf=True,     # Save confidence scores
    project=save_dir,   # Output folder
    name='predicted_video', # Subfolder name
    show=False          # Change to True if you want to display the video while processing
)

print("✅ Video processing complete. Results saved in:", os.path.join(save_dir, 'predicted_video'))
