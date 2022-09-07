import streamlit as st
from PIL import Image
import base64

st.set_page_config(layout='wide')

@st.cache
def load_image(path):
    with open(path, 'rb') as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    return encoded

def background_image_style(path):
    encoded = load_image(path)
    style = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
    }}
    </style>
    '''
    return style

image_path = 'src/app/utils/images/INFORME_Presentación_Look_My_Data_week_3.jpg'

st.write(background_image_style(image_path), unsafe_allow_html=True)




# image=Image.open('utils/INFORME_Presentación_Look_My_Data_week_3.jpg')
# st.image(image)