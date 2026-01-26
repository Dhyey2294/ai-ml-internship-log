import tensorflow as tf
import numpy as np
import cv2
import os
import time
import random

from tensorflow.keras.applications import MobileNetV3Small
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense
from tensorflow.keras.models import Model

# DATASET PATHS 

BASE_PATH = "dataset"

TRAIN_DIR = os.path.join(BASE_PATH, "seg_train", "seg_train")
VAL_DIR   = os.path.join(BASE_PATH, "seg_test", "seg_test")
PRED_DIR  = os.path.join(BASE_PATH, "seg_pred", "seg_pred")

# LOAD DATA
IMG_SIZE = (224, 224)
BATCH_SIZE = 32

print("Loading training dataset...")
train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    TRAIN_DIR,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE
)

print("Loading validation dataset...")
val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    VAL_DIR,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE
)

NUM_CLASSES = len(train_ds.class_names)
print("Classes:", train_ds.class_names)

# BUILD MODEL (MOBILENETV3 + TRANSFER LEARNING)

base_model = MobileNetV3Small(
    input_shape=(224, 224, 3),
    include_top=False,
    weights="imagenet"
)

base_model.trainable = False 

x = GlobalAveragePooling2D()(base_model.output)
output = Dense(NUM_CLASSES, activation="softmax")(x)

model = Model(
    inputs=base_model.input,
    outputs=output
)

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()

# TRAIN MODEL (SHORT DEMO TRAINING)
print("Training model...")
model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=3
)

# CREATE EMBEDDING MODEL (REMOVE CLASSIFIER)
embedding_model = Model(
    inputs=model.input,
    outputs=model.layers[-2].output
)

print("Embedding model ready.")

# SELECT IMAGES FOR BENCHMARK (1000 IMAGES)
image_paths = [
    os.path.join(PRED_DIR, f)
    for f in os.listdir(PRED_DIR)
    if f.lower().endswith(".jpg")
]

random.shuffle(image_paths)
image_paths = image_paths[:1000]

print("Benchmark images selected:", len(image_paths))

# IMAGE PREPROCESSING
def preprocess_image(path):
    img = cv2.imread(path)
    img = cv2.resize(img, (224, 224))
    img = img.astype(np.float32) / 255.0
    return np.expand_dims(img, axis=0)

# NAIVE BENCHMARK (SINGLE-IMAGE INFERENCE)
print("Running benchmark...")

start_time = time.time()

for img_path in image_paths:
    img = preprocess_image(img_path)
    _ = embedding_model.predict(img, verbose=0)

end_time = time.time()

total_time = end_time - start_time
avg_time = total_time / len(image_paths)

print("\n BENCHMARK RESULT")
print("Images processed:", len(image_paths))
print(f"Total time: {total_time:.2f} seconds")
print(f"Avg time per image: {avg_time * 1000:.2f} ms")
