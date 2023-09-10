import streamlit as st
from PIL import Image
import requests
from dotenv import load_dotenv
import os
import io
import json

# Set page tab display
st.set_page_config(
   page_title="Simple Image Uploader",
   page_icon= '🖼️',
   layout="wide",
   initial_sidebar_state="expanded",
)

load_dotenv()
url = os.getenv('API_URL')

# App title and description
st.header('Simple Image Uploader 📸')

### Create a native Streamlit file upload input
st.markdown("### Aircraft Type Recognition 👇")
img_file_buffer = st.file_uploader('Upload an image')

if img_file_buffer is not None:

  col1, col2 = st.columns(2) # Create a column layout

  with col1:
    ### Display the image user uploaded
    st.image(Image.open(img_file_buffer), caption="Here's the image you uploaded ☝️")

  with col2:
    with st.spinner("Processing image..."):
      ### Get bytes from the file buffer
      img_bytes = img_file_buffer.getvalue()
      ### Make request to  API (stream=True to stream response as bytes)
      res = requests.post("https://aircraftprediction-h7pqzemfza-ew.a.run.app/predict", files={'file': img_bytes})
      if res.status_code == 200:
        ### Display the image returned by the API
        content = json.loads(res.content)
        predicted_class = content["predicted_class"]
        placeholder = st.empty() # Create a placeholder ## <-- new change
        placeholder.markdown(f"<div style='text-align: center;'>Predicted Class: {predicted_class}</div>", unsafe_allow_html=True)
        # placeholder.write(f"Predicted Class: {predicted_class}") # Write to the placeholder ## <-- new change
        information = "info about the class " + predicted_class
        info_placeholder = st.empty()
        info_placeholder.markdown(f"<div style='text-align: center;'>Information: {information}</div>", unsafe_allow_html=True) 
        # info_placeholder.write(f"Information: {information}") ## <-- info placeholder
        # st.write(f"Predicted Class: {predicted_class}")
      else:
        st.markdown("**Oops**, something went wrong 😓 Please try again.")
        print(res.status_code, res.content)


