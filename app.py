import os
import streamlit as st
import PIL.Image as Image

# Function to save uploaded image to specified folder
def save_uploaded_file(uploaded_file, target_folder):
    img = Image.open(uploaded_file)
    img.save(os.path.join(target_folder,'uploaded_image.jpg'))
    return os.path.join(target_folder, uploaded_file.name)

# Title of the web app
st.title('Image Uploader')

# Specify the target folder to save the images
target_folder = "C:\Users\tbsmi\OneDrive\Desktop\Images"

# Display a file uploader widget
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Check if an image has been uploaded
if uploaded_file is not None:
    # Save the uploaded image to the target folder
    saved_path = save_uploaded_file(uploaded_file, target_folder)
    st.success(f"Image saved successfully at: {saved_path}")
