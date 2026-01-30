from ultralytics import YOLO
import torch

MODEL_PATH = "runs/classify/models/food_classifier.pt/weights/best.pt"
IMAGE_PATH = "Dataset/images_raw/sample_food.jpg"

device = 0 if torch.cuda.is_available() else "cpu"

model = YOLO(MODEL_PATH)

results = model.predict(
    source=IMAGE_PATH,
    imgsz=224,
    device=device
)

top1_idx = results[0].probs.top1
top1_conf = results[0].probs.top1conf
class_name = results[0].names[top1_idx]

print(f"Predicted food: {class_name}")
print(f"Confidence: {top1_conf:.4f}")
