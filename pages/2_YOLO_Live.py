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

# Enhanced UI/UX: Add tabs, better layout, and more guidance
st.markdown("""
    <style>
    .custom-title { font-size: 2.5em; font-weight: bold; color: #1746A2; margin-bottom: 0.2em; }
    .custom-desc { font-size: 1.2em; color: #333; margin-bottom: 1em; }
    .custom-section { background: #fff; border-radius: 12px; padding: 1.5em; box-shadow: 0 2px 8px rgba(0,0,0,0.07); margin-bottom: 1.5em; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="custom-title">🎥 Real-time Object Detection with YOLOv8</div>', unsafe_allow_html=True)
st.markdown('<div class="custom-desc">Start your webcam and see object detection in action, live! Adjust settings, switch themes, and enjoy a modern experience.</div>', unsafe_allow_html=True)

# Sidebar logo and description
with st.sidebar:
    st.image("./images/camera.png", width=80)
    st.markdown("<h4 style='color:#1746A2;'>YOLO Live Detection</h4>", unsafe_allow_html=True)
    st.write("Detect objects in real time using your webcam.")
    st.markdown("---")
    st.markdown("<small>Developed by Team VisionPrompt</small>", unsafe_allow_html=True)
    st.header("Threshold Settings")
    confidence_threshold = st.slider(
        "Confidence Threshold",
        min_value=0.1,
        max_value=1.0,
        value=0.5,
        help="Adjust the minimum confidence level for object detection."
    )
    mode = st.radio(
        "Choose Theme Mode:",
        ("Light", "Dark"),
        index=0,
        help="Switch between light and dark mode for comfort."
    )
    with st.expander("Advanced Settings", expanded=False):
        st.write("You can adjust detection thresholds and other parameters here.")
        st.markdown("- More features coming soon!")

# Apply dark mode CSS if selected
if mode == "Dark":
    st.markdown('''
        <style>
        .main { background-color: #222831; color: #EEEEEE; }
        .stButton>button { background-color: #393E46; color: #EEEEEE; }
        .stButton>button:hover { background-color: #00ADB5; color: #fff; }
        .stSidebar { background-color: #393E46; }
        .stSlider>div>div { background: #00ADB5; }
        </style>
    ''', unsafe_allow_html=True)

# Tabs for user guidance and detection
main_tabs = st.tabs(["Live Detection", "How to Use", "About"])

with main_tabs[0]:
    st.markdown('<div class="custom-section">', unsafe_allow_html=True)
    st.info("Use the sidebar to adjust detection settings and switch themes.")
    st.markdown("<small>For help, hover over the info icons next to each control.</small>", unsafe_allow_html=True)
    if ONLINE:
        st.success("Online mode: Using WebRTC for live detection.")
        with st.spinner("Loading WebRTC and model, please wait..."):
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
        if ctx.video_processor:
            ctx.video_processor.set_confidence(confidence_threshold)
        st.info("You can adjust the confidence threshold in the sidebar.")
        st.success("Detection ready! Start your webcam to begin.")
        st.balloons()
    else:
        st.warning("Offline mode: Using OpenCV for webcam access.")
        model = YOLO_Pred(
            onnx_model='models/best_model.onnx',
            data_yaml='models/data.yaml'
        )
        model.confidence = confidence_threshold
        run = st.button("Start Webcam Detection", help="Click to start webcam detection in offline mode.")
        if 'offline_running' not in st.session_state:
            st.session_state['offline_running'] = False
        stop = st.button("Stop Webcam Detection", help="Click to stop webcam detection.")
        frame_placeholder = st.empty()
        if run:
            st.session_state['offline_running'] = True
        if stop:
            st.session_state['offline_running'] = False
        if st.session_state['offline_running']:
            cap = cv2.VideoCapture(0)
            with st.spinner("Accessing webcam and running detection..."):
                while cap.isOpened() and st.session_state['offline_running']:
                    ret, frame = cap.read()
                    if not ret:
                        st.error("Failed to grab frame from webcam.")
                        break
                    model.confidence = confidence_threshold
                    processed_img = model.predictions(frame)
                    frame_placeholder.image(processed_img, channels="BGR")
                cap.release()
                frame_placeholder.empty()
            st.success("Detection stopped.")
            st.snow()
    st.markdown('</div>', unsafe_allow_html=True)

with main_tabs[1]:
    st.markdown('<div class="custom-section">', unsafe_allow_html=True)
    st.header("How to Use")
    st.markdown("""
    1. **Choose your theme** (Light or Dark) from the sidebar.
    2. **Adjust the confidence threshold** for detection sensitivity.
    3. **Start your webcam** (online or offline mode will be selected automatically).
    4. **View detected objects** live on your video stream.
    5. **Stop detection** at any time.
    """)
    st.info("For best results, ensure good lighting and a clear camera view.")
    st.markdown('</div>', unsafe_allow_html=True)

with main_tabs[2]:
    st.markdown('<div class="custom-section">', unsafe_allow_html=True)
    st.header("About")
    st.write("""
    This app demonstrates real-time object detection using YOLOv8 and Streamlit. It supports both online (WebRTC) and offline (OpenCV) webcam access, with a modern, user-friendly interface.
    
    **Developed by Team VisionPrompt**
    """)
    st.markdown('</div>', unsafe_allow_html=True)

