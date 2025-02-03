import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
from PIL import Image

genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))

## Function to load Google Gemini Pro Vision API And get response

def get_gemini_response(input_prompt, image):

    model = genai.GenerativeModel(model_name = 'gemini-1.5-flash')
    response = model.generate_content([input_prompt, image[0]])
    return response.text

def input_image_setup(uploaded_image):

    #Check if the file has been uploaded
    if uploaded_image:
        #Read the file into bytes
        bytes_data = uploaded_image.getvalue()

        image_parts = [

            {"mime_type": uploaded_image.type,  # Get the mime type of the uploaded file
                "data": bytes_data}
        ]

        return image_parts

    else:
        raise FileNotFoundError("No file uploaded")
    
## Initialize Streamlit app

st.set_page_config(page_title = 'Gemini Health APP')
st.title('Gemini Health APP')
input = st.text_input('Input Prompt:',key='input')
uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image.", use_container_width=True)


submit=st.button("Tell me the total calories")

input_prompt="""
You are an expert in nutritionist where you need to see the food items from the image
               and calculate the total calories, also provide the details of every food items with calories intake
               is below format

               1. Item 1 - no of calories
               2. Item 2 - no of calories
               ----
               ----
               

"""

## If submit button is clicked

if submit:
    image_data=input_image_setup(uploaded_image)
    response=get_gemini_response(input_prompt,image_data)
    st.subheader("The Response is")
    st.write(response)
