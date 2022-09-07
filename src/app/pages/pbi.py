import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

@st.cache
def read(csv):
    return pd.read_csv(csv)



df19=read('src/app/utils/df19.csv')
df_pbi=read('src/app/utils/dfpbi.csv')

con1=st.container()
col=st.columns(2,gap='medium')
cont=st.container()


paises=df19.pais.to_list()
with con1:
    metric=st.sidebar.selectbox('Seleccione un País',paises)
df=df19[df19.pais==metric] 
var=df.cumplimiento.values-45
var1=df.cumplimiento.values
with col[0]:    
    st.metric("EMISIONES CO2 -45% A 2030", f'{round(float(var1),2)}%',f'{round(float(var),2)}%')

with col[1]:
    st.metric("PBI 2019",df.pbi)

with cont:
    title = f"PBI / cumplimiento de -45% CO2 entre TOP5 emision y TOP5 paises cumplimiento de meta (2019)"

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Bar(x=df_pbi['pais'],y=df_pbi['pbi'],name='PBI',marker=dict(color=px.colors.sequential.Emrld[2])))
    fig.add_trace(go.Scatter(x=df_pbi['pais'],y=df_pbi['cumplimiento'],name='Cumplimiento',mode='markers', marker_color=df_pbi['cumplimiento'],),secondary_y=True)
    fig.update_layout( 
        title=title,
        barmode='stack' )

    st.plotly_chart(fig,use_container_width=True)
    st.write(df19)