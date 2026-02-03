# Day 13 – 02 Feb 2026
## 🔵 YOLO Dataset Formatting & Label Synchronization

## 🎯 Objective
To convert the collected food dataset into YOLO detection format,
fix label inconsistencies, and prepare it for YOLOv8 training.

## 🔹 Work Done
- Organized dataset into YOLO directory structure:
  final_dataset/
    train/images
    train/labels
    val/images
    val/labels

- Created automated script to split dataset:
  - 80% training
  - 20% validation
  - Randomized split

- Identified dataset issues:
  - Images without labels
  - Labels without images
  - Count mismatches

- Developed utility scripts to:
  - Detect missing labels
  - Create empty labels where required
  - Remove orphan labels
  - Synchronize images and labels

- Verified:
  - Train images ≈ train labels
  - Validation images = validation labels
  - Full YOLO compatibility

- Removed raw zips, temporary folders, and intermediate files.
- Cleaned project structure for training readiness.

## ✅ Outcome
- ~35,000+ images prepared for detection training.
- Multi-class dataset successfully converted to YOLO format.
- Fully synchronized images and labels.
- Dataset ready for YOLOv8 model training.

## 🧠 Learnings
- Label synchronization is critical for YOLO training stability.
- Small mismatches can break training pipelines.
- Structured dataset organization simplifies large-scale projects.

## 🔹 Code & Implementation
- Train/Val split:  
  [split_dataset.py](../code/day-13-food-yolo-format/split_dataset.py)
- Fix missing labels:  
  [fix_missing_labels.py](../code/day-13-food-yolo-format/fix_missing_labels.py)
- Sync images and labels:  
  [sync_images_labels.py](../code/day-13-food-yolo-format/sync_images_labels.py)
