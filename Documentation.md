# Project Documentation: Real-Time Object Detection with YOLOv8 and Streamlit

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [System Requirements](#system-requirements)
4. [Installation](#installation)
5. [Usage Guide](#usage-guide)
6. [Project Structure](#project-structure)
7. [Technical Details](#technical-details)
8. [Troubleshooting](#troubleshooting)
9. [Future Improvements](#future-improvements)
10. [Credits](#credits)

---

## 1. Overview
This project is a real-time object detection web application using the YOLOv8 deep learning model. Built with Streamlit, it allows users to detect objects live from their webcam, with support for both online (WebRTC) and offline (OpenCV) modes. The app is designed for accessibility, performance, and ease of use.

---

## 2. Features
- Real-time object detection using YOLOv8 ONNX model
- Live webcam detection (online and offline)
- Adjustable confidence threshold
- User-friendly Streamlit interface
- Automatic switching between WebRTC and OpenCV modes
- Error handling and user guidance
- Docker and requirements.txt for easy deployment

---

## 3. System Requirements
- Python 3.8+
- pip (Python package manager)
- Webcam (for live detection)
- Internet connection (for online mode)
- OS: Windows, macOS, or Linux

---

## 4. Installation
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd VisionPrompt
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **(Optional) Build Docker image:**
   ```bash
   docker build -t yolo-streamlit-app .
   ```

---

## 5. Usage Guide
1. **Run the app:**
   ```bash
   streamlit run Home.py
   ```
2. **Navigate the interface:**
   - Use the sidebar to adjust the confidence threshold.
   - Start live detection from the appropriate page.
   - If offline, the app will automatically use OpenCV for webcam access.
   - Stop detection using the provided button.
3. **Upload images/videos (if feature is enabled):**
   - Use the upload section to process files instead of live video.

---

## 6. Project Structure
```
VisionPrompt/
├── Dockerfile
├── Home.py
├── README.md
├── requirements.txt
├── yolo_predictions.py
├── models/
│   ├── best_model.onnx
│   ├── data.yaml
│   └── yolov8n-seg.onnx
├── images/
├── pages/
│   ├── 1_YOLO_Vision.py
│   └── 2_YOLO_Live.py
└── ...
```
- **Home.py**: Main entry point for the Streamlit app
- **yolo_predictions.py**: Model loading and inference logic
- **pages/**: Contains Streamlit app pages
- **models/**: Contains ONNX models and config files

---

## 7. Technical Details
- **YOLOv8 ONNX Model**: Exported from PyTorch for efficient, cross-platform inference
- **WebRTC (streamlit-webrtc)**: Used for online webcam streaming
- **OpenCV**: Used for offline webcam access
- **Session State**: Manages start/stop of webcam detection in offline mode
- **Confidence Threshold**: Adjustable in real time via sidebar
- **Docker**: Ensures consistent deployment

---

## 8. Troubleshooting
- **DuplicateWidgetID Error**: Ensure button keys are unique and not created inside loops
- **Webcam Not Detected**: Check camera permissions and device connection
- **ONNX Model Errors**: Verify model path and compatibility
- **Dependency Issues**: Reinstall packages using `pip install -r requirements.txt`
- **Port Conflicts**: If Streamlit fails to start, try a different port with `streamlit run Home.py --server.port 8502`

---

## 9. Future Improvements
- Image and video file upload for detection
- Object tracking across frames
- Custom class filtering
- Detection history and export
- User authentication and personalized settings
- Performance metrics (FPS, latency)
- Mobile device optimization

---

## 10. Credits
- Project developed by a team of four members (see `task_performed_by_each_memeber.md` for details)
- YOLOv8 by Ultralytics: https://github.com/ultralytics/ultralytics
- Streamlit: https://streamlit.io/
- streamlit-webrtc: https://github.com/whitphx/streamlit-webrtc
- OpenCV: https://opencv.org/

---

For more details, see the technical report and code comments.
