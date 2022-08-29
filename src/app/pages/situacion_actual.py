import streamlit as st

from utils import kill_top_margin


st.set_page_config(layout="wide", page_title="Situacion actual")

kill_top_margin()

st.markdown(
    "<br/><br/><h1 style='text-align: center; color: #0d523a;'>Situacion actual</h1><br/>",
    unsafe_allow_html=True,
)

_, image, _ = st.columns((3, 10, 3))

with image:
    st.image(
        "./utils/images/atmospheric-CO2.png",
        caption="CO2 en la atmosfera - 1000 años atras",
    )
