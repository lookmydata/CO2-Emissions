import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

@st.cache
def read(csv):
    return pd.read_csv(csv,sep=';')

def listcol(dfcol):
    dfcol=dfcol.unique()
    return dfcol.tolist()

df=read('datasets/desastres_naturales/Climate-related_Disasters_Frequency_normalizado.csv')

cont=st.container()
col=st.container()  #(2,gap='medium')
col1=st.container()

paises=listcol(df.pais_iso)
indicadores=listcol(df.indicador)
t=indicadores[5]
indicadores.remove(t)
indicadores.insert(0,t)


with cont:
    selecpais = st.sidebar.multiselect('seleccionar pais',paises)
    year = st.sidebar.slider('Select year',min(df.anio),max(df.anio))
    ind = st.sidebar.selectbox('seleccionar tipo de desastre',indicadores)

    df2=df[(df.pais_iso.isin(selecpais))&(df['anio']==year)&(df.indicador==ind)]
    df1=df[(df['anio']==year)&(df.indicador==ind)]
    if len(selecpais)==0:
        fig = px.choropleth(df1, locations="pais_iso",
                            color='frecuencia',
                            hover_name="pais",
                            hover_data=['indicador'],
                            range_color=(min(df1.frecuencia),max(df1.frecuencia)),
                            color_continuous_scale=px.colors.sequential.Reds)
    else:
        fig = px.choropleth(df2, locations="pais_iso",
                            color='frecuencia',
                            hover_name="pais",
                            hover_data=['indicador'],
                            range_color=(min(df2.frecuencia),max(df2.frecuencia)),
                            color_continuous_scale=px.colors.sequential.Reds)
                            
    st.plotly_chart(fig, use_container_width=True)





# df_drought=df.loc[(df.pais_iso==selecpais)&(df.indicador=='Drought')]
# df_ET=df[(df.pais_iso==selecpais)&(df.indicador=='Extreme Temperature')]
# df_flood=df[(df.pais_iso==selecpais)&(df.indicador=='Flood')]
# df_LS=df[(df.pais_iso==selecpais)&(df.indicador=='Landslide')]
# df_storm=df[(df.pais_iso==selecpais)&(df.indicador=='Storm')]
# df_WF=df[(df.pais_iso==selecpais)&(df.indicador=='Wildfire')]

# with col:   #[0]
#     fig=make_subplots()
#     fig.add_trace(go.Scatter(x=df_drought['anio'],y=df_drought['frecuencia'],name='Sequ??as'))
#     fig.add_trace(go.Scatter(x=df_ET['anio'],y=df_ET['frecuencia'],name='Altas temperaturas'))
#     fig.add_trace(go.Scatter(x=df_flood['anio'],y=df_flood['frecuencia'],name='Inundaciones'))
#     fig.add_trace(go.Scatter(x=df_LS['anio'],y=df_LS['frecuencia'],name='Landslide'))
#     fig.add_trace(go.Scatter(x=df_storm['anio'],y=df_storm['frecuencia'],name='Tormentas'))
#     fig.add_trace(go.Scatter(x=df_WF['anio'],y=df_WF['frecuencia'],name='Incendios forestales'))

#     st.plotly_chart(fig,use_container_width=True)

