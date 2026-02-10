from ultralytics import YOLO
import cv2

detector = YOLO("models/detector/food_detector_best.pt")
classifier = YOLO("models/classifier/food_classifier.pt")

img_path = "data/test_images/1.jpg"
img = cv2.imread(img_path)

results = detector(img, conf=0.25, verbose=False)[0]

for box in results.boxes:
    x1, y1, x2, y2 = map(int, box.xyxy[0])
    crop = img[y1:y2, x1:x2]

    cls = classifier(crop, verbose=False)[0]
    probs = cls.probs

    label = classifier.names[int(probs.top1)]
    conf = float(probs.top1conf)

    print(f"{label} ({conf:.2f}) at [{x1},{y1},{x2},{y2}]")
