from ultralytics import YOLO
import cv2
import os

DETECTOR_PATH = "models/detector/food_detector_best.pt"
CLASSIFIER_PATH = "models/classifier/food_classifier.pt"
IMAGE_DIR = "data/test_images"
CONF_THRES = 0.25

detector = YOLO(DETECTOR_PATH)
classifier = YOLO(CLASSIFIER_PATH)

print("Detector & Classifier loaded successfully")

for img_name in sorted(os.listdir(IMAGE_DIR)):
    img_path = os.path.join(IMAGE_DIR, img_name)
    img = cv2.imread(img_path)

    if img is None:
        continue

    print(f"\nImage: {img_name}")

    det_results = detector(img, conf=CONF_THRES, verbose=False)[0]

    if det_results.boxes is None or len(det_results.boxes) == 0:
        print("No food detected")
        continue

    for box in det_results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        crop = img[y1:y2, x1:x2]

        if crop.size == 0:
            continue

        cls_result = classifier(crop, verbose=False)[0]
        probs = cls_result.probs

        class_id = int(probs.top1)
        class_name = classifier.names[class_id]
        confidence = float(probs.top1conf)

        print(
            f"Detected: {class_name} | "
            f"Confidence: {confidence:.2f} | "
            f"BBox: [{x1},{y1},{x2},{y2}]"
        )
