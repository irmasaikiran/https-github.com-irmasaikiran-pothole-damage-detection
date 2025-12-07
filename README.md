# https-github.com-irmasaikiran-pothole-damage-detection
# 🛣️ Road Damage Detection & Cost Estimation System

This project uses **YOLOv8m** deep learning model to detect:
- Potholes  
- Cracks  
- Patches  
- General road surface damage  

It also estimates the **repair cost** automatically using:
1. **Model 2 – Road-Type Based Cost**  
2. **Model 3 – PWD Standard Government Cost**
3. 
##  Features

### 🖼 Image Damage Detection  
Upload any road image → Detect damages → Estimate repair cost.

### 🎥 Video Damage Detection  
Upload road inspection video → Frame-by-frame detection → Total damage area → Cost calculation.

### 📏 Damage Area Calculation  
Bounding-box pixel area → Converted to approximate m².

###  Cost Estimation Models  
- **Model 2**  
  - Asphalt: ₹500/m²  
  - Concrete: ₹800/m²  
- **Model 3 (PWD Model)**  
  - Material cost  
  - Labor cost  
  - Machinery  
  - Overheads  

###  Streamlit Web Application  
User-friendly interface for demo and deployment.

Custom YOLO Training Notebook  

---
##  Project Structure
pothole-damage-detection/
│
├── app/
│ ├── app.py
│ ├── detect_image.py
│ ├── detect_video.py
│ ├── cost_estimator.py
│ ├── utils.py
│
├── models/
│ └── download_weights.py
│
├── training/
│ ├── train_custom_yolo.ipynb
│ ├── data.yaml
│ └── dataset_template/
│ ├── images/
│ └── labels/
│
├── docs/
│ ├── Cost_Model_Explanation.pdf
│
├── samples/
│ ├── sample_image.jpg
│ └── sample_video.mp4
│
├── requirements.txt
├── LICENSE
---

## ⚙️ Installation

pip install -r requirements.txt
Download YOLOv8m model:

cd models
python download_weights.py
---
## ▶️ Run Application

streamlit run app.py
---
## 🧪 Train the YOLO Model
training/train_custom_yolo.ipynb
---
##  License
This project is licensed under the **MIT License**.
