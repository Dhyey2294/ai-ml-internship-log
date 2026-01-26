import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import GlobalAveragePooling2D
from tensorflow.keras.models import Model

# Input
inputs = tf.keras.Input(shape=(224, 224, 3))
x = inputs / 255.0

# Base model
base_model = MobileNetV2(
    input_tensor=x,
    include_top=False,
    weights="imagenet"
)
base_model.trainable = False

# Embedding head
outputs = GlobalAveragePooling2D()(base_model.output)
model = Model(inputs, outputs)

print("✅ Face embedding model built")

# Convert to TFLite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]

tflite_model = converter.convert()

with open("face_embedding.tflite", "wb") as f:
    f.write(tflite_model)

print("✅ TFLite model exported")
