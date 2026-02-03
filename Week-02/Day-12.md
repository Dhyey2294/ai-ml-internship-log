# Day 12 – 31 Jan 2026
## 🟢 Food Detection Dataset Collection & Cleaning

## 🎯 Objective
To build a large-scale multi-class food dataset for training a YOLOv8
object detection model capable of detecting multiple food items in a single image.

## 🔹 Work Done
- Downloaded a YOLOv8 food detection dataset from Roboflow containing:
  - Images
  - Bounding box labels (.txt)
- Used it as the base detection dataset.

- Downloaded Food-101 dataset from Kaggle.
- Filtered only relevant food classes.
- Removed unnecessary or unrelated western dishes.
- Used selected images to increase food diversity.

- Built a custom image crawler using `icrawler (BingImageCrawler)`.
- Crawled additional Indian foods, fruits, and vegetables such as:
  - Dal, roti, dosa, idli, rajma, pav bhaji
  - Guava, papaya, orange, pear, strawberry
  - Carrot, cabbage, spinach, capsicum, broccoli
- Performed multiple crawl runs to increase variety.
- Collected approximately 90–300 images per class.

- Removed duplicate images using hash-based comparison.
- Merged all cleaned images into a class-wise folder structure:
  food_final_selected/class_name/

## ✅ Outcome
- Large multi-source dataset created.
- Improved class diversity across Indian foods, fruits, and vegetables.
- Clean and deduplicated image collection ready for formatting.

## 🧠 Learnings
- Dataset diversity is essential for better detection performance.
- Crawling helps cover region-specific foods not present in public datasets.
- Deduplication prevents biased training.

## 🔹 Code & Implementation
- Image crawler:  
  [crawler.py](../code/day-12-food-dataset-prep/crawler.py)
- Duplicate removal:  
  [remove_duplicates.py](../code/day-12-food-dataset-prep/remove_duplicates.py)
- Merge to YOLO format:  
  [merge_to_yolo.py](../code/day-12-food-dataset-prep/merge_to_yolo.py)

