### Imports ###

import streamlit as st
from PIL import Image
import requests
import io
import json
from class_info_imp import aircraft_data, aircraft_classes
from base64 import b64encode
import numpy as np
import base64


# Set page tab display
st.set_page_config(
    page_title="AeroID",
    page_icon='🖼️',
    layout="wide",
    initial_sidebar_state='collapsed',
)

# App title and description
st.title('AeroID ✈')
### Create a native Streamlit file upload input
# st.markdown("### Aircraft Type Recognition 👇")
img_file_buffer = st.file_uploader('Upload an image')

### Defining CSS styles for smooth displays

custom_css_green = """
                    <style>
                        .custom-markdown-green {
                            border: 2px solid #00FF00; /* Green border */
                            border-radius: 15px; /* Rounded corners *
                            padding: 10px; /* Padding inside the box */
                            background-color: #F0FFF0; /* Light green background */
                            text-align: center; /* Center text */
                        }
                    </style>
                    """


rounded_image_style = """
                    <style>
                        .rounded-image-container {
                            border: none;
                            padding: 10px;
                            border-radius: 15px; /* Adjust this value for rounded corners */
                            overflow: hidden; /* Hide overflowing content (for rounded corners) */
                        }

                        .rounded-image {
                            width: 100%;
                            height: auto;
                            border-radius: 15px; /* Match the container's border-radius for rounded corners */
                            border: none;
                        }
                    </style>
                    """


if img_file_buffer is not None: # if a picture has been uploaded, proceed

    ### Read from API
    img_bytes = img_file_buffer.getvalue()
    res = requests.post("https://aircraftprediction-h7pqzemfza-ew.a.run.app/predict", files={'file': img_bytes})
    content = json.loads(res.content)

    if res.status_code == 200: # if the image is processed by the model & API

        # defining vairables used throughout code
        format_size = (400,400)
        prediction_probs = str(content["probabilty_np"][2:-2])
        prediction_probs_list = [float(value) for value in prediction_probs.split()]
        top_index_1 = prediction_probs_list.index(max(prediction_probs_list))
        top_prediction_1 = aircraft_classes[top_index_1]
        top_pred_acc = round(prediction_probs_list[top_index_1]*100, 2)
        indices_list = sorted(range(len(prediction_probs_list)), key = lambda i: prediction_probs_list[i], reverse=True)
        top_pred_list = [aircraft_classes[i] for i in indices_list]

        # 3 first predictions :
        pred_1 = f"{aircraft_data[top_pred_list[0]]['display_name']} : {round(prediction_probs_list[indices_list[0]]*100,2)}%"
        pred_2 = f"{aircraft_data[top_pred_list[1]]['display_name']} : {round(prediction_probs_list[indices_list[1]]*100,2)}%"
        pred_3 = f"{aircraft_data[top_pred_list[2]]['display_name']} : {round(prediction_probs_list[indices_list[2]]*100,2)}%"

    else:
        st.markdown("**Oops**, something went wrong 😓 Please try again.")
        print(res.status_code, res.content)

    col1, col2 = st.columns(2)  # Create a column layout

    with col1:

        ### Display text "here's your uploaded picture"
        st.markdown(
            '<h2 style="text-align: center;">🔽 Here is the picture you uploaded 🔽</h2>',
            unsafe_allow_html=True
        )

        ### Display uploaded image
        st.markdown(rounded_image_style, unsafe_allow_html=True)

        # img_bytes.resize(format_size)
        img_base64 = base64.b64encode(img_bytes).decode()
        rounded_image_html = f"""
        <div class="rounded-image-container">
            <img src="data:image/jpeg;base64,{img_base64}" style="width: 100%; height: 400px; border-radius: 15px;" class="rounded-image">
        </div>
        """
        st.markdown(rounded_image_html, unsafe_allow_html=True)

        if top_pred_acc >= 70: # On the condition that the model has a confident prediction

            st.write('')

            with st.expander('🛂 Want to learn more about this aircraft type ?'):
                info = aircraft_data[top_pred_list[0]]['info_box'].split('\n')
                for i in info:
                    st.write(i)

        else : pass

    with col2:

        if top_pred_acc >= 70: # If the model has a confident prediction, proceed :

            ### Display the model's prediction

            st.markdown(
                '<h2 style="text-align: center;">⏬ Here is our model\'s prediction ⏬</h2>',
                unsafe_allow_html=True
            )

            ### Display image of prediction
            img_best_model = aircraft_data[top_pred_list[0]]['image_url']

            st.markdown(rounded_image_style, unsafe_allow_html=True)

            rounded_image_html_2 = f"""
            <div class="rounded-image-container style="width:600px; hieght:400px; overflow:hidden; border'radius: 15px">
                <img src="{img_best_model}" style="width: 100%; height: 400px; object-fit: cover;" class="rounded-image">
            </div>
            """

            st.markdown(rounded_image_html_2, unsafe_allow_html=True)

            ### Display the model's prediction

            st.markdown(custom_css_green, unsafe_allow_html=True)

            prediction_display_1 = f"<div class='custom-markdown-green' style='font-size: 24px;'><b>1️⃣ {pred_1} 🛫</b></div>"
            st.markdown(prediction_display_1, unsafe_allow_html=True)

            st.write('')
            ### Display expandable box containing secondary and tertiary predictions

            with st.expander('2️⃣ See our model\'s second prediction'):
                prediction_display_2 = f"<div style='text-align: center; border: 2px solid #ccc; padding: 10px;'>{pred_2}</div>" ##
                st.markdown(prediction_display_2, unsafe_allow_html=True)
                st.image(aircraft_data[top_pred_list[1]]['image_url'], caption=f"This is a {aircraft_data[top_pred_list[1]]['display_name']}!", use_column_width=True)
            with st.expander('3️⃣ See our model\'s third prediction'):
                prediction_display_3 = f"<div style='text-align: center; border: 2px solid #ccc; padding: 10px;'>{pred_3}</div>" ##
                st.markdown(prediction_display_3, unsafe_allow_html=True)
                st.image(aircraft_data[top_pred_list[2]]['image_url'], caption=f"This is a {aircraft_data[top_pred_list[2]]['display_name']}!", use_column_width=True)


        else: # Ask user to upload different image, or otherwise see predictions anyway

            ### Display to request a different picture

            st.markdown(
                '<h2 style="text-align: center;">Hmm, our model couldn\'t recognise this aircraft type.. Could you try another image ? 💩</h2>',
                unsafe_allow_html=True
            )
            html_code_3= f"""
            <div style="padding: 10px; border-radius: 15px; overflow: hidden;">
                <img src=https://tse1.mm.bing.net/th?id=OIP.d8vl4WyKrSnxwFyyENQtqwHaEK&pid=Api&P=0&h=180 style="width: 100%; height: auto; border-radius: 15px;">
            </div>
            """

            st.markdown(html_code_3, unsafe_allow_html=True)

            ### Give user the option to see predictions anyway

            with st.expander('Want to see the model\'s predictions anyway ?'):
                st.markdown(
                '<h2 style="text-align: center;">Here is our model\'s prediction 👇</h2>',
                unsafe_allow_html=True
                )
                st.markdown(custom_css_green, unsafe_allow_html=True)
                prediction_display_1 = f"<div class='custom-markdown-green' style='font-size: 24px;'><b>{pred_1}</b></div>"
                st.markdown(prediction_display_1, unsafe_allow_html=True)
                html_code_1 = f"""
                <div style="padding: 10px; border-radius: 15px; overflow: hidden;">
                    <img src={aircraft_data[top_pred_list[0]]['image_url']} style="width: 100%; height: auto; border-radius: 15px;">
                </div>
                """
                st.markdown(html_code_1, unsafe_allow_html=True)
