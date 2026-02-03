import os
import random
import shutil

SRC = "Dataset/final_dataset/train"
VAL = "Dataset/final_dataset/val"
SPLIT = 0.2

def split():
    imgs = os.listdir(os.path.join(SRC, "images"))

    random.shuffle(imgs)
    val_count = int(len(imgs) * SPLIT)

    val_imgs = imgs[:val_count]

    for img in val_imgs:
        shutil.move(
            os.path.join(SRC, "images", img),
            os.path.join(VAL, "images", img)
        )

        label = img.replace(".jpg", ".txt")
        shutil.move(
            os.path.join(SRC, "labels", label),
            os.path.join(VAL, "labels", label)
        )

    print("Validation split complete")

if __name__ == "__main__":
    split()
