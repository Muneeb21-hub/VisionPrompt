import av
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, WebRtcMode
from yolo_predictions import YOLO_Pred
import socket
import cv2

st.set_page_config(
    page_title="Real-Time YOLO Detection",
    page_icon="🎥",
    layout="centered"
)


class YOLOVideoProcessor(VideoProcessorBase):
    def __init__(self):
        super().__init__()
        self.model = YOLO_Pred(
            onnx_model='models/best_model.onnx',
            data_yaml='models/data.yaml'
        )
        self.confidence_threshold = 0.4  # default conf threshold

    def set_confidence(self, threshold):
        self.confidence_threshold = threshold

    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
        # Convert the frame to a numpy array
        img = frame.to_ndarray(format="bgr24")

        # Update the model's confidence threshold dynamically
        self.model.confidence = self.confidence_threshold

        # Perform predictions on the current frame
        processed_img = self.model.predictions(img)

        # Return the processed frame
        return av.VideoFrame.from_ndarray(processed_img, format="bgr24")


def is_online():
    try:
        # Try to connect to Google's DNS
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        return True
    except OSError:
        return False


ONLINE = is_online()

st.title("Real-time Object Detection with YOLOv8")


with st.sidebar:
    st.header("Threshold Settings")
    confidence_threshold = st.slider(
        "Confidence Threshold",
        min_value=0.1,
        max_value=1.0,
        value=0.5,
        help="adjust the minimum confidence level for object detection"
    )

# webRTC component
if ONLINE:
    st.success("Online mode: Using WebRTC for live detection.")
    ctx = webrtc_streamer(
        key="yolo-live-detection",
        mode=WebRtcMode.SENDRECV,
        video_processor_factory=YOLOVideoProcessor,
        rtc_configuration={
            "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
        },
        media_stream_constraints={
            "video": True,
            "audio": False
        },
        async_processing=True,
    )
    # updating confidence threshold
    if ctx.video_processor:
        ctx.video_processor.set_confidence(confidence_threshold)
else:
    st.warning("Offline mode: Using OpenCV for webcam access.")
    model = YOLO_Pred(
        onnx_model='models/best_model.onnx',
        data_yaml='models/data.yaml'
    )
    model.confidence = confidence_threshold
    run = st.button("Start Webcam Detection")
    frame_placeholder = st.empty()
    if run:
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                st.error("Failed to grab frame from webcam.")
                break
            model.confidence = confidence_threshold
            processed_img = model.predictions(frame)
            frame_placeholder.image(processed_img, channels="BGR")
            if st.button("Stop", key="stop_btn"):
                break
        cap.release()
        frame_placeholder.empty()

