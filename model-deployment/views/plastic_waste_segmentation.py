import streamlit as st
import cv2
import numpy as np

from PIL import Image

st.subheader("Plastic Waste Segmentation")

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
        # Display the uploaded image
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Simulate segmentation output (replace with your model's prediction)
        st.write("### Segmentation Output")
        segmented_image = np.array(image) // 2  # Dummy output (darkened image)
        st.image(segmented_image, caption="Segmented Image", use_column_width=True)

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
                segmented_frame = frame // 2  # Dummy output (darkened frame)
                st.image(segmented_frame, caption="Segmented Frame", use_column_width=True)
        cap.release()

# Footer information
st.markdown("---")
st.caption("Plastic Waste Segmentation Tool")
