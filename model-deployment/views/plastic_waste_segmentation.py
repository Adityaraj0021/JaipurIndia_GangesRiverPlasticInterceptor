import os
import streamlit as st
import cv2
import numpy as np
from PIL import Image
from yoloseg.YOLOSeg import YOLOSeg
from yoloseg.utils import pad_and_resize

# Define a cached function to load the YOLOSeg model
@st.cache_resource
def load_model(model_path, conf_thres=0.2, iou_thres=0.3):
    return YOLOSeg(model_path, conf_thres=conf_thres, iou_thres=iou_thres)

st.markdown("<h3 style='text-align: center;'>Plastic Waste Segmentation</h3>", unsafe_allow_html=True)

# Toggle between image and video segmentation
segmentation_type = st.radio(
    "Select Segmentation Type:",
    ("Image Segmentation", "Video Segmentation"),
    horizontal=True
)

if segmentation_type == "Image Segmentation":
    st.write("### Upload an Image")
    uploaded_image = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Read the uploaded image using PIL
        image = Image.open(uploaded_image)
        img = np.array(image)
        
        # Resize input image
        input_img = pad_and_resize(img, (640, 640))
        
        # Load the model using the cached function
        base_dir = os.getcwd()
        model_path = os.path.join(base_dir, "assets", "best.onnx")
        yoloseg = load_model(model_path)
        
        # Perform segmentation
        boxes, scores, class_ids, masks = yoloseg(input_img)
        combined_img = yoloseg.draw_masks(input_img)
        
        # Display the uploaded image
        st.markdown("<h4 style='text-align: center;'>Input Image</h4>", unsafe_allow_html=True)
        st.image(image, use_container_width=True)
        
        st.markdown("---")

        # Display the segmented image
        st.markdown("<h4 style='text-align: center;'>Segmented Image</h4>", unsafe_allow_html=True)
        st.image(combined_img, use_container_width=True)

elif segmentation_type == "Video Segmentation":
    st.write("### Upload a Video")
    uploaded_video = st.file_uploader("Choose a video file", type=["mp4", "avi", "mov"])

    if uploaded_video is not None:
        # Display uploaded video
        st.video(uploaded_video)

        # Simulate segmentation output (replace with your model's prediction)
        st.write("### Segmentation Output")
        cap = cv2.VideoCapture(uploaded_video.name)
        if cap.isOpened():
            ret, frame = cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # Resize input image
                input_frame = pad_and_resize(frame, (640, 640))
                
                # Load the model using the cached function
                base_dir = os.getcwd()
                model_path = os.path.join(base_dir, "assets", "best.onnx")
                yoloseg = load_model(model_path)
                
                # Update object localizer
                boxes, scores, class_ids, masks = yoloseg(input_frame)

                combined_frame= yoloseg.draw_masks(input_frame, mask_alpha=0.4)
                
                st.image(combined_frame, caption="Segmented Frame", use_container_width=True)
        cap.release()
