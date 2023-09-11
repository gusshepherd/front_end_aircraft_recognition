import streamlit as st
from PIL import Image
import requests
from dotenv import load_dotenv
import os
import io
import json
from class_info import dict_aircraft_info, display_name_dict  # Import the dictionary
# Set page tab display
st.set_page_config(
    page_title="Simple Image Uploader",
    page_icon='🖼️',
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

    col1, col2 = st.columns(2)  # Create a column layout

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

                placeholder = st.empty()  # Create a placeholder
                placeholder.markdown(
                f"<div style='text-align: center; border: 2px solid #000; padding: 10px;'><b>Predicted Class: {display_name_dict[predicted_class]}</b></div>",
                unsafe_allow_html=True)


                if predicted_class in dict_aircraft_info:
                    class_info_text = dict_aircraft_info[predicted_class]
                else:
                    class_info_text = "We currently don't have extensive information for this aircraft"

                # Format aircraft information using HTML tags
                formatted_info = "<div style='text-align: left;'>"
                for line in class_info_text.split('\n'):
                    if ':' in line:
                        key, value = line.split(':', 1)
                        formatted_info += f"<strong>{key.strip()} :</strong> {value.strip()}<br>"
                    else:
                        formatted_info += f"{line.strip()}<br>"
                formatted_info += "</div>"

                info_placeholder = st.empty()
                info_placeholder.markdown(formatted_info, unsafe_allow_html=True)
            else:
                st.markdown("**Oops**, something went wrong 😓 Please try again.")
                print(res.status_code, res.content)
