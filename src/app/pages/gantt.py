import pandas as pd
import streamlit as st
import plotly.express as px


def gantt():
    color_sequence = ['#0d523a', '#159669', '#3ac998', '#63bfa0', '#333333']
    dg = pd.DataFrame([
        dict(Tarea="Planteo Proyecto", Start='2022-08-16', Finish='2022-08-17', Stage="0"),
        dict(Tarea="Búsqueda y definición de datasets", Start='2022-08-17', Finish='2022-08-19', Stage="1"),
        dict(Tarea="Limpieza y normalizacion de datos", Start='2022-08-18', Finish='2022-08-25', Stage="1"),
        dict(Tarea="Data Lakehouse", Start='2022-08-19', Finish='2022-08-23', Stage="1"),
        dict(Tarea="Analisis", Start='2022-08-25', Finish='2022-09-02', Stage="2"),
        dict(Tarea="Modelos ML", Start='2022-09-02', Finish='2022-09-06', Stage="3"),
        dict(Tarea="Dashboard Streamlit", Start='2022-09-06', Finish='2022-09-08', Stage="4"),
        dict(Tarea="Reporte y conclusiones", Start='2022-09-06', Finish='2022-09-08', Stage="4"),
        ])

    fig = px.timeline(
            dg, 
            x_start="Start", 
            x_end="Finish", 
            y="Tarea",
            color="Stage", 
            color_discrete_sequence=color_sequence[::-1]
            )
    fig.update_yaxes(autorange="reversed")
    return fig


page = st.empty()

with page.container():
    st.header("Diagrama de gantt - Planeacion del proyecto")
    st.plotly_chart(gantt())
