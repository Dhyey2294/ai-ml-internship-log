import os
import shutil

SRC = "Dataset/food_final_selected"
DST = "Dataset/final_dataset/train/images"

def merge():
    for cls in os.listdir(SRC):
        class_dir = os.path.join(SRC, cls)

        for img in os.listdir(class_dir):
            src = os.path.join(class_dir, img)
            new_name = f"{cls}_{img}"

            shutil.copy(src, os.path.join(DST, new_name))

    print("Merge complete")

if __name__ == "__main__":
    merge()
