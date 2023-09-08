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

# Example local Docker container URL
# url = 'http://api:8000'
# Example localhost development URL
# url = 'http://localhost:8000'
load_dotenv()
url = os.getenv('API_URL')

# App title and description
st.header('Simple Image Uploader 📸')

### Create a native Streamlit file upload input
st.markdown("### aircraft type recognition 👇")
img_file_buffer = st.file_uploader('Upload an image')

if img_file_buffer is not None:

  col1, col2 = st.columns(2)

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
        st.write(f"Predicted Class: {predicted_class}")
      else:
        st.markdown("**Oops**, something went wrong 😓 Please try again.")
        print(res.status_code, res.content)

# import streamlit as st
# import requests
# from PIL import Image
# from io import BytesIO

# # Set the URL of the prediction API
# PREDICTION_URL = "https://aircraftprediction-h7pqzemfza-ew.a.run.app/predict"

# # Create a file uploader widget
# uploaded_file = st.file_uploader("Choose an image to upload")

# # Check if a file has been uploaded
# if uploaded_file is not None:
#     # Load the uploaded image
#     image = Image.open(uploaded_file)
    
#     # Display the uploaded image
#     st.image(image, caption="Uploaded Image", use_column_width=True)
    
#     # Convert the image to JPEG format and save it in memory
#     with BytesIO() as buffer:
#         image.save(buffer, format="JPEG")
#         image_bytes = buffer.getvalue()
    
#     # Send the image to the prediction API
#     response = requests.post(PREDICTION_URL, files={"image": image_bytes})
    
#     # Check if the request was successful
#     if response.status_code == 200:
#         # Get the prediction result from the response
#         result = response.json()
#         print(result)
#         # Display the prediction result
#         st.write(f"Prediction: {result['prediction']}")
#         st.write(f"Confidence: {result['confidence']:.2f}")
#     else:
#         # Display an error message
#         st.error("An error occurred while making the prediction")
