import os
import requests
import zipfile

BASE_URL = "https://raw.githubusercontent.com/irmasaikiran/pothole-damage-detection/main/"
PROJECT = "pothole_damage_detection_system"

FILES = [
    "app/app.py",
    "app/detect_image.py",
    "app/detect_video.py",
    "app/cost_estimator.py",
    "app/utils.py",
    "models/download_weights.py",
    "training/train_custom_yolo.ipynb",
    "training/data.yaml",
    "docs/Cost_Model_Explanation.pdf",
    "samples/sample_image.jpg",
    "samples/sample_video.mp4",
    "requirements.txt",
    "LICENSE",
    "README.md"
]

def download(url, path):
    r = requests.get(url)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(r.content)
    print(f"[+] Downloaded: {path}")

def build_project():
    print("\n=== Building Project ===\n")

    for f in FILES:
        download(BASE_URL + f, f"{PROJECT}/{f}")

    print("\n=== Creating ZIP ===\n")
    with zipfile.ZipFile(f"{PROJECT}.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for root, dirs, files in os.walk(PROJECT):
            for file in files:
                filepath = os.path.join(root, file)
                z.write(filepath, filepath.replace(PROJECT + "/", ""))

    print(f"\n✔ DONE! ZIP Created: {PROJECT}.zip\n")

if __name__ == "__main__":
    build_project()
