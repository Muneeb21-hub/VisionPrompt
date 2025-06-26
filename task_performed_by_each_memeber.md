# Task Performed by Each Member

This project was developed by a team of four members. Below is a detailed breakdown of the tasks performed by each member, including specific technical responsibilities, research, and collaboration highlights:

---

## Muneeb ur Rehman (23BSCS11): Model Integration & Backend Development
- Researched and selected the YOLOv8 ONNX model suitable for real-time object detection.
- Converted and optimized the model for ONNX runtime, ensuring efficient inference on various hardware.
- Developed the `yolo_predictions.py` module, implementing preprocessing, postprocessing, and custom confidence threshold logic.
- Integrated support for both image and video frame inputs, handling edge cases and error management.
- Collaborated with Member 3 to ensure seamless integration of backend inference with real-time video streams.
- Provided technical documentation for model usage and troubleshooting.

---

## Ayesha Naseer (23BSCS07): Streamlit App & UI/UX Design
- Designed the overall user interface, focusing on clarity, accessibility, and responsiveness.
- Implemented multi-page navigation using Streamlit’s page system, including the home, about, and detection pages.
- Developed sidebar controls for real-time parameter adjustment (e.g., confidence threshold slider) and contextual help.
- Created custom icons, banners, and layout elements to enhance visual appeal.
- Conducted user testing sessions and iterated on feedback to improve usability.
- Coordinated with Member 4 to ensure documentation matched the app’s UI/UX.

---

## Amina (22BSCS50): Real-Time Video Processing & WebRTC Integration
- Integrated `streamlit-webrtc` for live webcam streaming, configuring ICE servers and handling network issues.
- Developed the `YOLOVideoProcessor` class, optimizing frame-by-frame detection for low latency.
- Implemented dynamic confidence threshold updates, allowing real-time tuning during detection sessions.
- Researched and implemented an offline fallback using OpenCV for direct webcam access, ensuring robustness when internet is unavailable.
- Profiled and optimized video processing pipeline for performance and stability.
- Worked closely with Member 1 to debug and synchronize model inference with video frame acquisition.

---

## Zulkeha (23BSCS37): Documentation, Testing & Deployment
- Authored comprehensive documentation, including `README.md`, usage guides, and project presentation materials.
- Developed and executed test cases for all major features, including live detection, offline mode, and UI controls.
- Automated environment setup with `requirements.txt` and Dockerfile for reproducible deployment.
- Managed Git version control, coordinated pull requests, and led code review sessions.
- Organized team meetings, tracked progress, and ensured timely delivery of project milestones.
- Assisted other members with troubleshooting and provided feedback on code and documentation.

---

Each member contributed to code reviews, collaborative debugging, and regular team discussions to ensure a high-quality and cohesive final product.
