from ultralytics import YOLO

# Load your trained model
model = YOLO('D:\Obj_detection\model\best.pt')  # Replace with the actual path to your downloaded model file

# Run inference on an image
results = model('D:\Obj_detection\source_file_img_video\fire.jpg')  # Replace with the path to the image on your PC

# Process the results (optional)
for r in results:
    # r.boxes contains bounding box coordinates, confidence scores and class IDs
    # r.masks contains segmentation masks (if applicable)
    # r.keypoints contains keypoints (if applicable)
    # r.probs contains class probabilities (if applicable)
    print(r.boxes)

# To save the predicted image with bounding boxes:
results[0].save_dir = 'D:\Obj_detection\source_file_img_video\fire2clr.jpg' # Replace with the directory where you want to save the result
results[0].save()