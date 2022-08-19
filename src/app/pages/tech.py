import streamlit as st


st.set_page_config(layout="centered", page_title="Stack tecnologico")

text, image = st.columns((10, 10))

with text:
    st.markdown("""
### Stack tecnologico

- Data lakehouse (Databricks, Airflow)
- ETL (Python, Spark)
- Analytics (Plotly, Streamlit)
- Paper (Latex)
""")

with image:
    st.image("./utils/images/tech.png")
