import streamlit as st
import cv2
import os
from ultralytics import YOLO
import numpy as np
from detect_image import process_image
from detect_video import process_video
from cost_estimator import estimate_cost_model2, estimate_cost_model3

st.set_page_config(page_title="Road Damage Detection & Cost Estimator", layout="wide")

# Load YOLO model
MODEL_PATH = "../models/yolov8m.pt"

if not os.path.exists(MODEL_PATH):
    st.error("YOLO model not found! Run download_weights.py in the models folder.")
else:
    model = YOLO(MODEL_PATH)

st.title("🛣️ Road Damage Detection & Cost Estimation System")

st.sidebar.header("Upload Input")
mode = st.sidebar.radio("Choose Input Type:", ["Image", "Video"])

# -----------------------------
# IMAGE MODE
# -----------------------------
if mode == "Image":
    file = st.sidebar.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

    if file:
        img_array = np.frombuffer(file.read(), np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        st.image(img, caption="Uploaded Image", use_column_width=True)

        if st.button("Run Detection"):
            result_img, area = process_image(img, model)
            st.image(result_img, caption="Detection Result", use_column_width=True)

            st.subheader("📌 Damage Area Detected:")
            st.write(f"**{area:.4f} m²**")

            cost_mode = st.selectbox("Choose Cost Model:", ["Model 2 – Road Type", "Model 3 – PWD Standard"])

            if cost_mode == "Model 2 – Road Type":
                road_type = st.radio("Select Road Type:", ["Asphalt", "Concrete"])
                cost = estimate_cost_model2(area, road_type)
                st.success(f"Estimated Repair Cost (Model 2): ₹ {int(cost)}")

            else:
                cost = estimate_cost_model3(area)
                st.success(f"Estimated Repair Cost (Model 3): ₹ {int(cost)}")

# -----------------------------
# VIDEO MODE
# -----------------------------
elif mode == "Video":
    file = st.sidebar.file_uploader("Upload Video", type=["mp4", "avi", "mov"])

    if file:
        temp_video = "uploaded_video.mp4"
        with open(temp_video, "wb") as f:
            f.write(file.read())

        if st.button("Run Video Detection"):
            output_path, total_area = process_video(temp_video, model)

            st.video(output_path)

            st.subheader("📌 Total Damage Area Detected:")
            st.write(f"**{total_area:.4f} m²**")

            cost_mode = st.selectbox("Select Cost Model:", ["Model 2 – Road Type", "Model 3 – PWD Standard"])

            if cost_mode == "Model 2 – Road Type":
                road_type = st.radio("Road Type:", ["Asphalt", "Concrete"])
                cost = estimate_cost_model2(total_area, road_type)
                st.success(f"Estimated Cost (Model 2): ₹ {int(cost)}")

            else:
                cost = estimate_cost_model3(total_area)
                st.success(f"Estimated Cost (Model 3): ₹ {int(cost)}")
