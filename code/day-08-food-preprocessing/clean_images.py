import cv2
import os

ROOT_DIR = "Dataset/images_cls_split"

def clean_images(root_dir):
    removed = 0

    for split in ["train", "val"]:
        split_path = os.path.join(root_dir, split)
        if not os.path.exists(split_path):
            continue

        for cls_name in os.listdir(split_path):
            cls_path = os.path.join(split_path, cls_name)
            if not os.path.isdir(cls_path):
                continue

            for img_name in os.listdir(cls_path):
                img_path = os.path.join(cls_path, img_name)
                try:
                    img = cv2.imread(img_path)
                    if img is None:
                        os.remove(img_path)
                        removed += 1
                except Exception:
                    os.remove(img_path)
                    removed += 1

    print(f"Removed {removed} corrupted images")

if __name__ == "__main__":
    clean_images(ROOT_DIR)
