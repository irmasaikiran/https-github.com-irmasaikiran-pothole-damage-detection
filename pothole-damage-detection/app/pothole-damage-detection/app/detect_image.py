import cv2
import numpy as np

def process_image(image, model):
    results = model.predict(image)
    total_area_m2 = 0

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            width = x2 - x1
            height = y2 - y1
            pixel_area = width * height

            # Convert pixel area to approximate square meters
            area_m2 = pixel_area * 0.000001  
            total_area_m2 += area_m2

            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(
                image,
                f"{area_m2:.4f} m²",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    return image, total_area_m2
