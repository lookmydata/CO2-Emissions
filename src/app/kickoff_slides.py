import streamlit as st

from utils.kickoff_text import *


page = st.empty()
d1 = st.empty()


def intro() -> None:
    canvas = st.empty()
    with canvas.container(): 
        st.header("Propuesta Emisiones CO2")
        st.markdown("> Estudio realizado por LookMyData")

        # MEJORAR
        # st.subheader("Emisiones de CO2 vs Medio ambiente")
        # st.write(INTRO)


def goal_fst():
    canvas = st.empty()
    with canvas.container():
        st.subheader(GOAL1_HEADER)
        st.write(GOAL1)


def run():
    with page.container():
        intro()
        goal_fst()


if __name__ == '__main__':
    run()
