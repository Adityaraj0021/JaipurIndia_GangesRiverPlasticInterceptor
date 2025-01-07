import streamlit as st

# Page title and header
st.title("Real-time Plastic Waste Segmentation on Edge Devices")
st.subheader("Optimize AI Models for Mobile and Edge Deployment")

# Introduction section
st.markdown("""
Plastic waste segmentation involves identifying and categorizing plastic waste in real-time using edge devices like mobile phones, Raspberry Pi, or Nvidia Jetson Nano.
To achieve this, we use lightweight models that are optimized for performance and speed.
Below, you can find steps to implement this solution and download pre-trained models in **TFLite** and **TensorRT** formats.
""")

# Implementation steps
st.markdown("### Steps to Implement:")
st.markdown("""
1. **Model Optimization:** Convert a trained model (e.g., TensorFlow or PyTorch) to formats like TFLite or TensorRT for edge device compatibility.
2. **Edge Deployment:**
   - Use **TensorFlow Lite Interpreter** for mobile or embedded systems.
   - Use **TensorRT Runtime** for Nvidia GPUs like Jetson Nano.
3. **Real-Time Inference:** Integrate the model with edge device hardware for on-the-fly segmentation.
4. **Testing and Performance Tuning:** Evaluate latency, accuracy, and power consumption.
""")

# Download model section
st.markdown("### Pre-Trained Models")
st.markdown("Access pre-trained models via the following links:")

# Links to models
tflite_url = "https://example.com/path/to/plastic_segmentation_model.tflite"
tensorrt_url = "https://example.com/path/to/plastic_segmentation_model.trt"

st.markdown(f"""
- [Download TFLite Model]({tflite_url})  
- [Download TensorRT Model]({tensorrt_url})
""")

# Edge device compatibility
st.markdown("### Compatible Edge Devices")
st.markdown("""
- **Mobile Devices:** Android (via TensorFlow Lite), iOS
- **Embedded Systems:** Raspberry Pi, Nvidia Jetson Nano, Nvidia Jetson Xavier NX
""")

st.markdown("For more details, visit the [documentation](https://www.tensorflow.org/lite) or [Nvidia TensorRT resources](https://developer.nvidia.com/tensorrt).")
