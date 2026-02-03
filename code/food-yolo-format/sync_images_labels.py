import os

IMG_DIR = "Dataset/final_dataset/train/images"
LBL_DIR = "Dataset/final_dataset/train/labels"

def sync():
    imgs = {os.path.splitext(f)[0] for f in os.listdir(IMG_DIR)}
    lbls = {os.path.splitext(f)[0] for f in os.listdir(LBL_DIR)}

    deleted_imgs = 0
    deleted_lbls = 0

    for base in imgs - lbls:
        os.remove(os.path.join(IMG_DIR, base + ".jpg"))
        deleted_imgs += 1

    for base in lbls - imgs:
        os.remove(os.path.join(LBL_DIR, base + ".txt"))
        deleted_lbls += 1

    print(f"Deleted images: {deleted_imgs}")
    print(f"Deleted labels: {deleted_lbls}")

if __name__ == "__main__":
    sync()

