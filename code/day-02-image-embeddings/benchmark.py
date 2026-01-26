import time
import numpy as np

def benchmark(num_images=1000):
    start = time.time()
    for _ in range(num_images):
        time.sleep(0.0005)  # simulate inference
    total = time.time() - start
    print(f"Processed {num_images} images")
    print(f"Total time: {total:.2f}s")
    print(f"Avg per image: {(total/num_images)*1000:.2f} ms")

if __name__ == "__main__":
    benchmark()
