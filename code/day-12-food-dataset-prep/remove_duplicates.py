import os
import hashlib

DATASET = "Dataset/food_final_selected"

def file_hash(path):
    with open(path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def remove_duplicates(folder):
    seen = {}
    removed = 0

    for root, _, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)

            try:
                h = file_hash(path)
                if h in seen:
                    os.remove(path)
                    removed += 1
                else:
                    seen[h] = path
            except:
                pass

    print(f"Removed duplicates: {removed}")

if __name__ == "__main__":
    remove_duplicates(DATASET)
