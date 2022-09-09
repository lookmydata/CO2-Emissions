import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


@st.cache
def read(csv):
    return pd.read_csv(csv)

def listcol(dfcol):
    dfcol=dfcol.unique()
    return dfcol.tolist()
#DATA#
df_energia=read('src/app/utils/df_energia.csv')
piechart=read('src/app/utils/pie.csv')

paislis=listcol(df_energia.pais)
#SIDEBAR#
multpais=st.sidebar.multiselect(' ',paislis)

#LAYOUT#
cols1=st.container()
cols=st.columns(2,gap='large')


with cols[0]:
    df=df_energia.set_index('pais')
    df=df.loc[multpais]
    if len(multpais)==0:
        df_energia=df_energia.head(15)
        fig1 = make_subplots()
        fig1.add_trace(go.Bar(x=df_energia['pais'],y=df_energia['energia_cons'],name='Consumo'))
        fig1.add_trace(go.Bar(x=df_energia['pais'],y=df_energia['energia_produccion'],base='stack',name='Produccion',opacity=0.6))
        fig1.add_trace(go.Scatter(x=df_energia['pais'],y=df_energia['net_energy'],name='Neto'))
        fig1.update_layout(go.Layout(
            barmode='overlay'
        ))
    else:
        fig1 = make_subplots()
        fig1.add_trace(go.Bar(x=multpais,y=df['energia_cons'],name='Consumo'))
        fig1.add_trace(go.Bar(x=multpais,y=df['energia_produccion'],base='stack',name='Produccion',opacity=0.6))
        fig1.add_trace(go.Scatter(x=multpais,y=df['net_energy'],name='Neto'))
        fig1.update_layout(go.Layout(
            barmode='overlay'
        ))
    fig1.update_layout( title='Consumo vs produccion en paises productores',
                        barmode='stack',
                        width=500,
                        margin=dict(l=0, b=0, r=0, t=30, pad=0))
    st.plotly_chart(fig1)                            

with cols[1]:
    piechart=piechart.head(6)
    fig = px.pie(piechart,values='CO2_emission',names=piechart.Country)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(title='Contribucion por pais en emisiones CO2',
                        showlegend=False,
                        width=300,
                        margin=dict(l=0, b=0, r=0, t=30, pad=0))
    st.plotly_chart(fig)

with cols1:
    st.image('src/app/utils/images/unknown.png')
