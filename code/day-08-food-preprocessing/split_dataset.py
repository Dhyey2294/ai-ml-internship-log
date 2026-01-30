import os
import shutil
import random

SRC_DIR = "Dataset/images_raw"
DST_DIR = "Dataset/images_cls_split"
TRAIN_RATIO = 0.8

os.makedirs(DST_DIR, exist_ok=True)

for split in ["train", "val"]:
    os.makedirs(os.path.join(DST_DIR, split), exist_ok=True)

for cls_name in os.listdir(SRC_DIR):
    cls_path = os.path.join(SRC_DIR, cls_name)
    if not os.path.isdir(cls_path):
        continue

    images = os.listdir(cls_path)
    random.shuffle(images)

    split_idx = int(len(images) * TRAIN_RATIO)
    train_imgs = images[:split_idx]
    val_imgs = images[split_idx:]

    for img in train_imgs:
        dst = os.path.join(DST_DIR, "train", cls_name)
        os.makedirs(dst, exist_ok=True)
        shutil.copy(os.path.join(cls_path, img), os.path.join(dst, img))

    for img in val_imgs:
        dst = os.path.join(DST_DIR, "val", cls_name)
        os.makedirs(dst, exist_ok=True)
        shutil.copy(os.path.join(cls_path, img), os.path.join(dst, img))

print("Dataset split completed")
