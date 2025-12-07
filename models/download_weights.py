import requests
import os
from tqdm import tqdm

# URL of YOLOv8m pretrained weights
MODEL_URL = "https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8m.pt"
MODEL_NAME = "yolov8m.pt"

def download_file(url, filename):
    """Downloads file with progress bar."""
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get("content-length", 0))

    with open(filename, "wb") as file, tqdm(
        total=total_size, unit="B", unit_scale=True, desc=filename
    ) as bar:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
                bar.update(len(chunk))

    print(f"\nDownload complete: {filename}")


if __name__ == "__main__":
    if os.path.exists(MODEL_NAME):
        print(f"Model '{MODEL_NAME}' already exists — skipping download.")
    else:
        print(f"Downloading YOLOv8m model from {MODEL_URL} ...\n")
        download_file(MODEL_URL, MODEL_NAME)
