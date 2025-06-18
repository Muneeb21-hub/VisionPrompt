# Project Presentation: YOLO Prompt-based and Customized Object Detection Web App

## Overview

This project is a web application that leverages the power of the YOLOv8 (You Only Look Once, version 8) object detection model, enhanced with prompt-based customization. The app allows users to select specific object classes for detection, adjust detection thresholds, and perform real-time object detection on images and live video streams.

## Key Features

### 1. Custom Class Selection via Prompt
- Users can specify which object classes they want to detect by entering prompts.
- This enables focused and efficient object detection tailored to user needs.

### 2. Adjustable Detection Thresholds
- **Confidence Threshold:** Users can set the minimum confidence score for detections, balancing between precision and recall.
- **Class Score Threshold:** Users can define the minimum class probability required for an object to be considered detected.

### 3. Real-Time Object Detection
- The app supports live video stream processing, enabling real-time detection and visualization of objects.
- Users can see detection results instantly as they adjust parameters.

### 4. Transfer Learning with YOLOv8
- The application uses a YOLOv8 model pre-trained on a large dataset and fine-tuned on 20 custom object classes.
- This approach ensures high accuracy and adaptability to specific use cases.

### 5. User-Friendly Web Interface
- The app provides an intuitive interface for uploading images, selecting classes, adjusting thresholds, and viewing results.
- Visual feedback is provided for each detection, including bounding boxes and class labels.

## Technical Details

- **Backend:** Python, leveraging ONNX models for efficient inference.
- **Frontend:** Web-based interface (details depend on implementation, e.g., Streamlit, Flask, or custom JS).
- **Model:** YOLOv8, with support for ONNX runtime for fast and portable inference.
- **Deployment:** The app can be deployed using Docker for easy setup and scalability. A live demo is available at [App Link](https://vpromptscope-production.up.railway.app/).

## Directory Structure

- `Home.py`: Main entry point for the web application.
- `yolo_predictions.py`: Contains logic for running YOLOv8 predictions.
- `models/`: Stores ONNX models and configuration files.
- `images/`: Contains static images used in the app.
- `pages/`: Contains different UI pages for the app (e.g., image detection, live detection).
- `requirements.txt`: Lists Python dependencies.
- `Dockerfile`: For containerized deployment.

## Use Cases

- Custom object detection for industrial, educational, or research purposes.
- Real-time monitoring and analytics.
- Rapid prototyping for computer vision applications.

## How It Works

1. **User uploads an image or starts a live video stream.**
2. **User selects object classes to detect via prompt.**
3. **User adjusts detection thresholds as needed.**
4. **The app processes the input using the YOLOv8 model and displays results with bounding boxes and labels.**

## Conclusion

This project demonstrates the flexibility and power of modern object detection models, combined with user-driven customization. It is suitable for anyone interested in computer vision, from students to professionals.
