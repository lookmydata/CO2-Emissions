import streamlit as st

from utils.kickoff_text import *


def doc() -> None:
    canvas = st.empty()
    with canvas.container():
        st.markdown(DOC)


def run() -> None:
    page = st.empty()
    with page.container():
        doc()


if __name__ == '__main__':
    st.set_page_config(layout='centered', page_title='paper')
    run()
