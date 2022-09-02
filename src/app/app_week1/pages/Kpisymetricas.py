import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide", page_title="KPI’s y métricas")

page = st.empty()

with page.container():
    st.markdown(
        "<h1 style='text-align: center; color: #0d523a;'>KPI’s y métricas</h1>",
        unsafe_allow_html=True,
    )
    var = '<p style="font-family:sans-serif; color:#0d523a; font-size: 20px;"> En base a los análisis a realizar, proponemos los siguientes indicadores:</li>'
    st.markdown(var, unsafe_allow_html=True)

    var1 = '<li style="font-family:sans-serif; color:#0d523a; font-size: 15px;"> Ranking de países según participación de energías limpias en la matriz energética</li>'
    st.markdown(var1, unsafe_allow_html=True)

    var2 = '<li style="font-family:sans-serif; color:#0d523a; font-size: 15px;"> Evolución histórica de generación de energía y emisión de CO2  en top 10 países emisores de CO2</li>'
    st.markdown(var2, unsafe_allow_html=True)

    var3 = '<li style="font-family:sans-serif; color:#0d523a; font-size: 15px;"> Evolución del índice de calidad de aire (AQI) en relación al nivel de emisión de CO2  en los 10 países de mayor emisión</li>'
    st.markdown(var3, unsafe_allow_html=True)

    var4 = '<li style="font-family:sans-serif; color:#0d523a; font-size: 15px;">m3 CO2 / GWh generado</ul></li>'
    st.markdown(var4, unsafe_allow_html=True)

    var5 = '<li style="font-family:sans-serif; color:#0d523a; font-size: 15px;"> Ranking países según m3 CO2 / 1M USDPBI</li>'
    st.markdown(var5, unsafe_allow_html=True)

    var6 = '<li style="font-family:sans-serif; color:#0d523a; font-size: 15px;"> Casos de cáncer de pulmón por m3 de CO2  en países top 10 según emisiones</li>'
    st.markdown(var6, unsafe_allow_html=True)

    var7 = '<li style="font-family:sans-serif; color:#0d523a; font-size: 15px;"> Frecuencia de desastres naturales / m3 CO2</li>'
    st.markdown(var7, unsafe_allow_html=True)
