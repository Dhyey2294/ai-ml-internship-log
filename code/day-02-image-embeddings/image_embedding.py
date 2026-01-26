import tensorflow as tf
import numpy as np
import cv2
import os
import time
import random
from tensorflow.keras.applications import MobileNetV3Small
from tensorflow.keras.layers import GlobalAveragePooling2D
from tensorflow.keras.models import Model

# DATASET PATH
BASE_PATH = "dataset_new/lfw-deepfunneled"
IMG_SIZE = (224, 224)

# BUILD EMBEDDING MODEL
base_model = MobileNetV3Small(
    input_shape=(224, 224, 3),
    include_top=False,
    weights="imagenet"
)
base_model.trainable = False

embedding_model = Model(
    inputs=base_model.input,
    outputs=GlobalAveragePooling2D()(base_model.output)
)

print("Embedding model loaded.")

# IMAGE PREPROCESSING
def preprocess_image(path):
    img = cv2.imread(path)
    img = cv2.resize(img, IMG_SIZE)
    img = img.astype(np.float32) / 255.0
    return np.expand_dims(img, axis=0)

# COLLECT IMAGES
image_paths = []
for root, _, files in os.walk(BASE_PATH):
    for file in files:
        if file.lower().endswith(".jpg"):
            image_paths.append(os.path.join(root, file))

random.shuffle(image_paths)
image_paths = image_paths[:1000]

print(f"Images selected: {len(image_paths)}")

# RUN INFERENCE
start = time.time()
for path in image_paths:
    img = preprocess_image(path)
    _ = embedding_model.predict(img, verbose=0)

end = time.time()
total_time = end - start
avg_time = total_time / len(image_paths)

print("\n=== EMBEDDING BENCHMARK ===")
print(f"Total time: {total_time:.2f} s")
print(f"Avg per image: {avg_time * 1000:.2f} ms")
