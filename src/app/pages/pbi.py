import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

@st.cache
def read(csv):
    return pd.read_csv(csv)

df_pbi=read('src/app/utils/dfpbi.csv')
col=st.columns(1,gap='small')
cont=st.container()

with col[0]:
    paises=df_pbi.pais.to_list()
    metric=st.selectbox('Seleccione un País',paises)
    df=df_pbi[df_pbi.pais==metric]
    
    var=df.cumplimiento.values-45
    var1=df.cumplimiento.values
    st.metric("EMISIONES CO2 -45% A 2030", f'{float(var1)}%',f'{round(float(var),2)}%')


with cont:
    title = f"PBI / cumplimiento de -45% CO2 entre TOP5 emision y TOP5 paises cumplimiento de meta (2019)"


    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Bar(x=df_pbi['pais'],y=df_pbi['pbi'],name='PBI',marker=dict(color=px.colors.sequential.Emrld[2])))
    fig.add_trace(go.Scatter(x=df_pbi['pais'],y=df_pbi['cumplimiento'],name='Cumplimiento',mode='markers', marker_color=df_pbi['cumplimiento'],),secondary_y=True)
    fig.update_layout( title=title,
                         height=300,
                         width=600,
                         margin={'l': 10, 'r': 20, 't': 30, 'b': 10},
                        xaxis=dict(automargin= True,
                                    tickangle= 45,
                                    title=dict(
                                    # text="Month",
                                    standoff= 20))
                        ,yaxis=dict(automargin= True,
                                tickangle= 0,
                                title=dict(
                                # text= "Temprature",
                                standoff= 40)),
                        legend=dict(
                          yanchor="top",
                          y=0.99,
                          xanchor="left",
                          x=1),
                        barmode='stack')


    st.plotly_chart(fig)