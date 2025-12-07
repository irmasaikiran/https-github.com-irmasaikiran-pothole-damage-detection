import cv2
import numpy as np

def process_video(video_path, model):
    cap = cv2.VideoCapture(video_path)
    output = "output_video.mp4"

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(
        output,
        fourcc,
        30.0,
        (int(cap.get(3)), int(cap.get(4)))
    )

    total_area_m2 = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model.predict(frame)

        for r in results:
            for box in r.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                width = x2 - x1
                height = y2 - y1
                frame_area_m2 = (width * height) * 0.000001
                total_area_m2 += frame_area_m2

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(
                    frame,
                    f"{frame_area_m2:.4f} m²",
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2
                )

        out.write(frame)

    cap.release()
    out.release()

    return output, total_area_m2
