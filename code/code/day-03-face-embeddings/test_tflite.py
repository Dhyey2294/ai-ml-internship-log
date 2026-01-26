import tensorflow as tf
import numpy as np

interpreter = tf.lite.Interpreter(model_path="face_embedding.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

print("Input shape:", input_details[0]["shape"])
print("Output shape:", output_details[0]["shape"])

dummy_input = np.random.rand(1, 224, 224, 3).astype(np.float32)
interpreter.set_tensor(input_details[0]["index"], dummy_input)
interpreter.invoke()

embedding = interpreter.get_tensor(output_details[0]["index"])
print("Embedding generated:", embedding.shape)
