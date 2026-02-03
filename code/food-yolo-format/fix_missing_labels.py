import os

IMG_DIR = "Dataset/final_dataset/train/images"
LBL_DIR = "Dataset/final_dataset/train/labels"

def fix():
    created = 0

    for img in os.listdir(IMG_DIR):
        base = os.path.splitext(img)[0]
        label_path = os.path.join(LBL_DIR, base + ".txt")

        if not os.path.exists(label_path):
            open(label_path, "w").close()
            created += 1

    print(f"Created {created} empty labels")

if __name__ == "__main__":
    fix()
