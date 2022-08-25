import pandas as pd
import streamlit as st
import plotly.express as px

from utils import kill_top_margin


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

    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0)
    )

    fig.update_yaxes(title='', autorange="reversed")
    return fig


st.set_page_config(
    layout="wide",
    page_title="Gantt"
)

kill_top_margin()

st.markdown(
    "<br/><br/><h1 style='text-align: center; color: #0d523a;'>Diagrama de gantt - Planificacion del proyecto</h1><br/>", 
    unsafe_allow_html=True
)

_, gantt_chart, _ = st.columns((1, 20, 3))

with gantt_chart:
    st.plotly_chart(gantt(), use_container_width=True)

    ###GANTT SEMANA 2###
    
# color_sequence = ['#0d523a', '#159669', '#3ac998', '#63bfa0']#, '#333333']
# dg2 = pd.DataFrame([
#     dict(Tarea="Data Lakehouse", Start='2022-08-22', Finish='2022-08-25', Semana="2"),
#     dict(Tarea="Limpieza y normalizacion de datos", Start='2022-08-22', Finish='2022-08-23', Semana="2"),
    
#     dict(Tarea="Analisis", Start='2022-08-29', Finish='2022-08-31', Semana="3"),
#     dict(Tarea="Modelos ML", Start='2022-08-29', Finish='2022-09-01', Semana="3"),
#     dict(Tarea="API", Start='2022-08-31', Finish='2022-09-07', Semana="3"),

#     dict(Tarea="Dashboard Streamlit", Start='2022-08-31', Finish='2022-09-07', Semana="4"), 
#     dict(Tarea="Reporte y conclusiones", Start='2022-09-05', Finish='2022-09-07', Semana="4"),
#     dict(Tarea="Demos", Start='2022-09-06', Finish='2022-09-08', Semana="4")
# ])

# fig = px.timeline(
#         dg, 
#         x_start="Start", 
#         x_end="Finish", 
#         y="Tarea",
#         color="Semana", 
#         color_discrete_sequence=color_sequence[::-1],
#         width=1420, height=830
# )
#------------------#
# fig.update_layout(
#     margin=dict(l=0, r=0, t=0, b=0),
#     font=dict(size=24)
# )

# fig.update_yaxes(autorange="reversed")
# fig.show()

# color_sequence = ['#0d523a', '#159669', '#3ac998', '#63bfa0', '#333333']
# dg = pd.DataFrame([
#     dict(Tarea="Planteo Proyecto", Start='2022-08-16', Finish='2022-08-17', Semana="1"),
#     dict(Tarea="Búsqueda y definición de datasets", Start='2022-08-17', Finish='2022-08-19', Semana="1"),
#     dict(Tarea="Limpieza y normalizacion de datos", Start='2022-08-18', Finish='2022-08-25', Semana="2"),
#     dict(Tarea="Data Lakehouse", Start='2022-08-19', Finish='2022-08-23', Semana="2")
# ])

# fig = px.timeline(
#         dg, 
#         x_start="Start", 
#         x_end="Finish", 
#         y="Tarea",
#         color="Semana", 
#         color_discrete_sequence=color_sequence[::-1],
#         width=1420, height=830
# )

# fig.update_layout(
#     margin=dict(l=0, r=0, t=0, b=0),
#     font=dict(size=24)
# )

# fig.update_yaxes(title='', autorange="reversed")
# fig.show()