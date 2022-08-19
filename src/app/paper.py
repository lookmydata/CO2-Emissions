import streamlit as st

from utils.kickoff_text import *


def doc() -> None:
    canvas = st.empty()
    with canvas.container():
        st.markdown(DOC)


def gantt() -> None:
    canvas = st.empty()
    with canvas.container():
        st.markdown(GANTT_HEADER)


def run() -> None:
    page = st.empty()
    with page.container():
        doc()
        gantt()


if __name__ == '__main__':
    run()
