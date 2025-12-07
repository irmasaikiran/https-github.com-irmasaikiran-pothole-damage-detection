import cv2

def read_image(path):
    """Reads an image from a given path."""
    return cv2.imread(path)


def resize_image(image, width=640):
    """Optional helper: resize image while keeping aspect ratio."""
    h, w = image.shape[:2]
    scale = width / w
    height = int(h * scale)
    return cv2.resize(image, (width, height))


def convert_to_rgb(image):
    """Convert BGR (OpenCV) to RGB (Streamlit use)."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
