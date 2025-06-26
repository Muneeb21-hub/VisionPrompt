import sys
import logging

def handle_exception(exc_type, exc_value, exc_traceback):
    logging.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))
    sys.__excepthook__(exc_type, exc_value, exc_traceback)
    sys.exit(1)

sys.excepthook = handle_exception

import streamlit as st


st.set_page_config(
    page_title="PromptVision: YOLOv8-Powered Smart Object Detection",
    layout="wide",
    page_icon = '🧠'
    # page_icon='./images/home.png'
)


# Custom CSS for modern look
st.markdown('''
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .stButton>button {
        background-color: #4F8BF9;
        color: white;
        border-radius: 8px;
        padding: 0.5em 2em;
        font-weight: bold;
        border: none;
        margin: 0.5em 0;
    }
    .stButton>button:hover {
        background-color: #1746A2;
        color: #fff;
    }
    .stSidebar {
        background-color: #e3e9f7;
    }
    .stSlider>div>div {
        background: #4F8BF9;
    }
    </style>
''', unsafe_allow_html=True)

# Sidebar logo and description
with st.sidebar:
    st.image("./images/home.png", width=80)
    st.markdown("<h4 style='color:#1746A2;'>PromptVision Home</h4>", unsafe_allow_html=True)
    st.write("Welcome to the YOLOv8-powered smart object detection.")
    st.markdown("---")
    st.markdown("<small>Developed by Team VisionPrompt</small>", unsafe_allow_html=True)
    st.markdown("<small>Navigate to Vision or Live Processing using the menu below.</small>", unsafe_allow_html=True)

# Enhanced UI/UX: Add tabs, better layout, and more guidance
st.markdown("""
    <style>
    .custom-title { font-size: 2.5em; font-weight: bold; color: #1746A2; margin-bottom: 0.2em; }
    .custom-desc { font-size: 1.2em; color: #333; margin-bottom: 1em; }
    .custom-section { background: #fff; border-radius: 12px; padding: 1.5em; box-shadow: 0 2px 8px rgba(0,0,0,0.07); margin-bottom: 1.5em; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="custom-title">🧠 PromptVision: YOLOv8-Powered Smart Object Detection</div>', unsafe_allow_html=True)
st.markdown('<div class="custom-desc">Detect objects in images, videos, or live streams with a modern, easy-to-use interface.</div>', unsafe_allow_html=True)

main_tabs = st.tabs(["Home", "How to Use", "About"])

with main_tabs[0]:
    st.markdown('<div class="custom-section">', unsafe_allow_html=True)
    st.caption("Custom and real-time object detection")
    st.markdown("""
    ---
    ### Welcome to the PromptVision: YOLOv8-Powered Smart Object Detection
    This web app uses YOLO V8 pre-trained model for transfer learning on 20 different objects, supported by a prompt to detect custom classes. You can also play a live video for real-time object detection.
    - **Custom Class Selection:** Choose the classes you want to detect using the prompt for focused object detection.
    - **Adjustable Thresholds:** 
      1. **Confidence Threshold:** Adjust the confidence level to control the balance between precision and recall.
      2. **Class Score Threshold:** The minimum class probability required for detection.
    - **Real-Time Object Detection:** Process live video streams using the above adjustable parameters.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with main_tabs[1]:
    st.markdown('<div class="custom-section">', unsafe_allow_html=True)
    st.header("How to Use")
    st.markdown("""
    1. **Navigate** to Vision or Live Processing using the sidebar.
    2. **Upload images/videos** or use your webcam for detection.
    3. **Adjust thresholds** and settings in the sidebar.
    4. **View results** in real time.
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

# Replace page links with a selectbox for navigation
page = st.sidebar.selectbox(
    "Navigation",
    ["Home", "Vision Processing", "Live Processing"],
    index=0
)

if page == "Vision Processing":
    st.experimental_set_query_params(page="1_YOLO_Vision")
    exec(open("pages/1_YOLO_Vision.py").read())
elif page == "Live Processing":
    st.experimental_set_query_params(page="2_YOLO_Live")
    exec(open("pages/2_YOLO_Live.py").read())

st.markdown("""
---

**Reference Repo**: [YOLO Prompt-based Customized App](https://github.com/Muneeb21-hub/VisionPrompt)

""")


