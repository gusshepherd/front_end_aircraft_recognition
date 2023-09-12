import streamlit as st
from PIL import Image
import requests
import io
import json
from class_info import dict_aircraft_info, display_name_dict, aircraft_classes, display_name  # Import the dictionary
from base64 import b64encode  # Import the b64encode function
import numpy as np  # Import NumPy for array manipulation

# Set page tab display
st.set_page_config(
    page_title="Simple Image Uploader",
    page_icon='🖼️',
    layout="wide",
    initial_sidebar_state="expanded",
)

# App title and description
st.header('Simple Image Uploader 📸')

### Create a native Streamlit file upload input
st.markdown("### Aircraft Type Recognition 👇")
img_file_buffer = st.file_uploader('Upload an image')

if img_file_buffer is not None:

    col1, col2, col3 = st.columns(3)  # Create a column layout
    with col1:
        st.image(Image.open(img_file_buffer), use_column_width=True)
        st.caption("Here's the image you uploaded ☝️")
        ###########
        # st.image(Image.open('default_image'), use_column_width=True)
        # st.caption("Here's another image of this aircraft type")

    with col2:
        with st.spinner("Processing image..."):
            ### Get bytes from the file buffer
            img_bytes = img_file_buffer.getvalue()
            ### Make request to API (stream=True to stream response as bytes)
            res = requests.post("https://aircraftprediction-h7pqzemfza-ew.a.run.app/predict", files={'file': img_bytes})
            if res.status_code == 200:
                ### Display the image returned by the API
                content = json.loads(res.content)
                ####
                # st.write(content)

                # Extract the top 3 predicted classes and their probabilities
                prediction_probs = content["probabilty_np"]
                prediction_probs = str(prediction_probs[2:-2])
                # prediction_probs = np.array(prediction_probs)  # Convert to NumPy array
                prediction_probs_list = [float(value) for value in prediction_probs.split()]
                top_index_1 = prediction_probs_list.index(max(prediction_probs_list))
                top_prediction_1 = aircraft_classes[top_index_1]
                #####2
                # top_index_2 = np.argpartition(prediction_probs, -2)[-2]
                # top_prediction_2 = aircraft_classes[top_index_2]

                # Display the prediction
                if top_prediction_1 in display_name_dict:
                    centered_and_boxed_line = f"<div style='text-align: center; border: 2px solid #ccc; padding: 10px;'><b>Model's prediction:</b> {display_name_dict[top_prediction_1]}</div>" ##
                    centered_and_boxed_line_acc = f"<div style='text-align: center; border: 2px solid #ccc; padding: 10px;'><b>Certainty level:</b> {prediction_probs_list[top_index_1]}%</div>" ##
                    # Display the line ({prediction_probs_list[top_index_1]})
                    st.markdown(centered_and_boxed_line, unsafe_allow_html=True)
                    st.markdown(centered_and_boxed_line_acc, unsafe_allow_html=True)
                else:
                    st.write("Unknown Class")

                if top_prediction_1 in dict_aircraft_info:
                    class_info_text = dict_aircraft_info[top_prediction_1]
                    ### Add box ###
                else:
                    class_info_text = "We currently don't have extensive information about this aircraft"

                # Split the class_info_text by '\n' and join with '<br>' to display each line on a new line in HTML
                class_info_lines = class_info_text.split('\n')

                # Modify each line to make the text before ':' bold
                class_info_lines = [line.split(':', 1) for line in class_info_lines]
                class_info_lines = [f"<b>{line[0]}</b>:{line[1]}" for line in class_info_lines]

                class_info_html = "<br>".join(class_info_lines)

                # Remove the prefix and add a CSS style to align the text to the left
                information = f"<div style='text-align: left; border: 2px solid #ccc; padding: 10px;'>{class_info_html}</div>"

                info_placeholder = st.empty()
                info_placeholder.markdown(information, unsafe_allow_html=True)

            else:
                st.markdown("**Oops**, something went wrong 😓 Please try again.")
                print(res.status_code, res.content)
    with col3:
        st.markdown(
            '<div style="text-align: center; border: 2px solid #ccc; padding: 10px;">'
            '<h3>Probability Distribution</h3>'
            '</div>',
            unsafe_allow_html=True
        )

        # text_of_probs = ""
        for i in range(len(prediction_probs_list)):
            st.write(f'\n{display_name[i]}: {round(prediction_probs_list[i], 4)}%\n')

        # st.markdown(
        #     '<div style="border: 2px solid #ccc; padding: 10px;">'
        #     '<h3>f"{text_of_probs}"</h3>'
        #     '</div>',
        #     unsafe_allow_html=True
        # )



        # st.write('to be continued..')
        # st.write(f'{content}')
        # st.write(f'{prediction_probs}')
        # st.write(f'{prediction_probs_list}')
