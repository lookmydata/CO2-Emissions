import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

@st.cache
def read(csv):
    return pd.read_csv(csv)

<<<<<<< HEAD
df_pbi=read('src/app/utils/dfpbi.csv')
col=st.columns(1,gap='small')
=======


df19=read('src/app/utils/df19.csv')
df_pbi=read('src/app/utils/dfpbi.csv')

con1=st.container()
col=st.columns(2,gap='medium')
>>>>>>> 14a8e76 (streamlit)
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

<<<<<<< HEAD

    st.plotly_chart(fig)
=======
    st.plotly_chart(fig,use_container_width=True)
    st.write(df19)
>>>>>>> 14a8e76 (streamlit)
