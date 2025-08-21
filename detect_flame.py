from ultralytics import YOLO
import os

# Paths
model_path = 'D:/Obj_detection/model/best.pt'  # Your trained model
image_path = 'D:/Obj_detection/source_file_img_video/fire2.jpg'  # Input image
save_dir = 'D:/Obj_detection/source_file_img_video'  # Folder to save results

# Load model
model = YOLO(model_path)

# Run inference and save image + text
results = model.predict(
    source=image_path,
    save=True,              # Save image with bounding boxes
    save_txt=True,          # Save bounding box coordinates as .txt
    save_conf=True,         # Save confidence score in .txt
    project=save_dir,       # Main folder to save
    name='predicted'        # Subfolder name inside save_dir
)

print("✅ Inference complete. Results saved in:", os.path.join(save_dir, 'predicted'))
