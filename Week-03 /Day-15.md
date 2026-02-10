# Day 15 – 04 Feb 2026
## 🔵 YOLOv8 Food Detection Model Training

## 🎯 Objective
To train a YOLOv8 object detection model for identifying
multiple food items in an image.

## 🔹 Work Done
- Installed Ultralytics YOLO in Google Colab.
- Selected YOLOv8 Nano model for faster experimentation.
- Configured training:
  - Image size: 640 × 640
  - Epochs: 50
  - Batch size: 16

- Executed training using:
  yolo detect train \
    model=yolov8n.pt \
    data=data.yaml \
    imgsz=640 \
    epochs=50

- Monitored:
  - Loss curves
  - Precision
  - Recall
  - mAP metrics

- Saved best model weights:
  food_detector_best.pt

## 📊 Performance Achieved
- mAP@50 → 0.848
- mAP@50–95 → 0.628
- Precision → 0.863
- Recall → 0.760

## ✅ Outcome
- Successfully trained multi-class food detector.
- High precision and good generalization.

## 🧠 Learnings
YOLOv8 provides strong detection accuracy even with
moderate training time.
