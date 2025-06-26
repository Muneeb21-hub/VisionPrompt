# Technical Report: Real-Time Object Detection with YOLOv8 and Streamlit

## 1. Introduction
This project implements a real-time object detection system using the YOLOv8 deep learning model, integrated into a user-friendly web application built with Streamlit. The system allows users to perform live object detection using their webcam, with support for both online (WebRTC) and offline (OpenCV) modes. The project is designed for accessibility, performance, and ease of use, making advanced computer vision technology available to a broad audience.

---

## Why We Use ONNX
ONNX (Open Neural Network Exchange) is used in this project for several important reasons:

- **Interoperability**: ONNX allows models trained in different frameworks (like PyTorch or TensorFlow) to be exported and run in other environments. This makes it easy to integrate the YOLOv8 model into our Python application, regardless of how it was originally trained.
- **Performance**: ONNX Runtime is optimized for fast inference and supports hardware acceleration (CPU, GPU, etc.), which is essential for real-time object detection.
- **Portability**: The ONNX format enables the same model to be deployed across different operating systems and devices without compatibility issues.
- **Ease of Integration**: ONNX models can be loaded and run in Python with simple APIs, making them ideal for use in web apps like Streamlit.

In summary, ONNX makes the model faster, more portable, and easier to use in production and cross-platform environments.

---

## 2. Project Objectives
- Enable real-time object detection using a pre-trained YOLOv8 model.
- Provide a simple and interactive web interface for users.
- Support both online and offline webcam access for robust usability.
- Allow users to adjust detection parameters (e.g., confidence threshold) on the fly.
- Ensure easy deployment and reproducibility with Docker and requirements files.

---

## 3. System Architecture

### 3.1. Model Backend
- **YOLOv8 ONNX Model**: The core detection engine is a YOLOv8 model exported to the ONNX format for efficient inference.
- **yolo_predictions.py**: This module loads the ONNX model, preprocesses input frames, runs inference, and post-processes results (drawing bounding boxes, labels, etc.).
- **Confidence Threshold**: Users can set a minimum confidence level for detections, filtering out low-confidence predictions.

### 3.2. Web Application (Frontend)
- **Streamlit**: Provides the web interface, page navigation, and UI controls (sliders, buttons, etc.).
- **Pages**: Includes a home page, about page, and dedicated pages for live detection and presentation.
- **Sidebar Controls**: Users can adjust detection parameters in real time.

### 3.3. Real-Time Video Processing
- **Online Mode (WebRTC)**: Uses `streamlit-webrtc` to access the webcam and stream video frames to the backend for detection. WebRTC requires an internet connection to establish peer-to-peer communication using STUN servers.
- **Offline Mode (OpenCV)**: If no internet connection is detected, the app falls back to OpenCV for direct webcam access, ensuring the system works anywhere.
- **YOLOVideoProcessor**: A custom class that processes each video frame, applies the YOLO model, and returns annotated frames for display.

---

## 4. Key Features and Concepts

### 4.1. YOLOv8 Object Detection
- **YOLO (You Only Look Once)** is a state-of-the-art, real-time object detection algorithm.
- The model detects multiple objects in a single pass, making it fast and efficient for live applications.
- The ONNX format allows for hardware-accelerated inference and easy integration with Python.

### 4.2. Real-Time Webcam Integration
- **WebRTC**: Enables low-latency, real-time video streaming in the browser. The app uses STUN servers to establish connections, which is why internet is required for this mode.
- **OpenCV Fallback**: When offline, OpenCV directly captures frames from the webcam, ensuring the app remains functional.

### 4.3. Interactive User Interface
- **Streamlit**: Simplifies web app development with Python, allowing rapid prototyping and deployment.
- **Sidebar Controls**: Users can adjust the confidence threshold slider to control detection sensitivity.
- **Live Feedback**: Detection results are displayed in real time, with bounding boxes and labels drawn on detected objects.

### 4.4. Robustness and Usability
- **Automatic Mode Switching**: The app detects internet connectivity and switches between WebRTC and OpenCV modes automatically.
- **Error Handling**: The system provides user-friendly messages if the webcam is not accessible or if detection fails.
- **Documentation**: Comprehensive guides and in-app help ensure users can easily understand and use all features.

### 4.5. Deployment and Reproducibility
- **Dockerfile**: Allows the entire application to be containerized for consistent deployment across environments.
- **requirements.txt**: Lists all Python dependencies for easy setup.
- **Version Control**: The project uses Git for collaborative development and version management.

---

## 5. How It Works (Step-by-Step)
1. **User opens the web app** (locally or on a server).
2. **App checks for internet connectivity**:
   - If online, uses WebRTC for webcam access.
   - If offline, uses OpenCV for webcam access.
3. **User starts live detection**:
   - The webcam feed is displayed in the app.
   - Each frame is sent to the YOLOv8 model for object detection.
   - Detected objects are highlighted with bounding boxes and labels.
4. **User can adjust the confidence threshold** in real time to filter detections.
5. **Results are displayed live** until the user stops the detection session.

---

## 6. Challenges and Solutions
- **WebRTC Dependency on Internet**: Solved by implementing an OpenCV fallback for offline use.
- **Model Performance**: Optimized ONNX model and frame processing for real-time speed.
- **User Experience**: Iterative UI design and user testing ensured the app is intuitive and accessible.
- **Deployment**: Docker and requirements files make setup and sharing straightforward.

---

## 7. Conclusion
This project demonstrates how advanced deep learning models like YOLOv8 can be made accessible through modern web technologies. By combining efficient model inference, real-time video processing, and a user-friendly interface, the system provides a powerful tool for object detection that works both online and offline. The modular design and comprehensive documentation make it easy to extend and adapt for future use cases.

---

## 8. References
- YOLOv8: https://github.com/ultralytics/ultralytics
- Streamlit: https://streamlit.io/
- streamlit-webrtc: https://github.com/whitphx/streamlit-webrtc
- OpenCV: https://opencv.org/
- ONNX: https://onnx.ai/

---

## How the YOLOv8 Model is Saved in ONNX Format

The YOLOv8 model is originally trained using a deep learning framework such as PyTorch. To make the model portable and efficient for inference in different environments, it is exported to the ONNX format. Here’s how this process works:

1. **Train the Model**: The YOLOv8 model is first trained in PyTorch using a dataset of images and labels.
2. **Export to ONNX**: After training, the model is exported to ONNX using a built-in export function. For Ultralytics YOLOv8, this can be done with a simple script:

```python
from ultralytics import YOLO

model = YOLO('yolov8n.pt')  # Load a trained PyTorch model
model.export(format='onnx')  # Export to ONNX format
```

This command creates a `.onnx` file (e.g., `yolov8n.onnx`) that contains the model architecture and weights.

**Benefits of Saving as ONNX:**
- The ONNX file can be loaded in different programming languages and environments.
- It enables hardware acceleration and efficient inference.
- It makes deployment easier and more flexible.

In this project, the ONNX model file is loaded in Python for real-time object detection in the Streamlit app.

---

## Benefits of Live Detection Using WebRTC and Offline Mode

### Live Detection with WebRTC (Online Mode)
- **Low Latency & Real-Time Processing:** WebRTC is designed for real-time communication, enabling smooth, low-latency video streaming and instant object detection feedback.
- **Browser Integration:** WebRTC works directly in the browser, so users don’t need to install extra software or drivers.
- **Cross-Platform Compatibility:** Works on Windows, macOS, Linux, and even mobile browsers.
- **Async Processing:** Streamlit’s WebRTC integration allows for asynchronous frame processing, keeping the UI responsive.
- **Security:** WebRTC uses secure protocols, and access to the webcam is managed by the browser, protecting user privacy.

### Offline Detection with OpenCV (Offline Mode)
- **No Internet Required:** Users can run detection even without an internet connection, making the app robust in all environments.
- **Direct Hardware Access:** OpenCV accesses the webcam directly, which can sometimes offer better performance or compatibility on certain systems.
- **Privacy:** All processing happens locally, and no video data leaves the user’s device.

### Why Not Use Only Offline Functionality?
- **User Experience:** WebRTC provides a seamless, browser-based experience without requiring users to install additional libraries or handle hardware permissions manually.
- **Compatibility:** Some environments (e.g., cloud deployments, shared computers) may restrict direct hardware access, making OpenCV less reliable.
- **Streamlit Integration:** Streamlit’s WebRTC component is designed for web apps, making it easier to build interactive, real-time applications.

### Why Support Both?
- **Robustness:** By supporting both modes, the app works everywhere—online or offline, with or without browser support for WebRTC.
- **Fallback:** If WebRTC fails (e.g., due to network issues), users can still use the app offline.

---

For further details, see the project documentation and code comments.
