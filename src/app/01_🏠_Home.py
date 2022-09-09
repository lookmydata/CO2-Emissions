import streamlit as st

st.set_page_config(layout='wide')
cont=st.container()

with cont:
    st.title('Look my CO2')
    st.markdown('''
    ### Brindamos información sobre las emisiones de dióxido de carbono, el consumo y producción de energía y otras problemáticas relacionadas.
    > Propuesta de análisis por __LookMyData__
    ''')

# @st.cache
# def load_image(path):
#     with open(path, 'rb') as f:
#         data = f.read()
#     encoded = base64.b64encode(data).decode()
#     return encoded

# def background_image_style(path):
#     encoded = load_image(path)
#     style = f'''
#     <style>
#     .stApp {{
#         background-image: url("data:image/png;base64,{encoded}");
#         background-size: cover;
#     }}
#     </style>
#     '''
#     return style

# image_path = 'src/app/utils/images/INFORME_Presentación_Look_My_Data_week_3.jpg'

# st.write(background_image_style(image_path), unsafe_allow_html=True)