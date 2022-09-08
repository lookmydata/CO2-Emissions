from audioop import mul
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

@st.cache
def read(csv):
    return pd.read_csv(csv)


st.set_page_config(layout="wide")

cols=st.columns(2,gap='large')
emisionCO2=st.container()
energia=st.columns(1)
cont=st.container()
cont1=st.container()


#GET DATA
dftop=read("src/app/utils/top5.csv")
años=dftop.anio.unique()
años=años.tolist()

df_energia=read('src/app/utils/df_energia.csv')
paises=df_energia.pais.unique()
paises=paises.tolist()


# energia chart
with cols[1]:
    multi_pais=st.sidebar.multiselect(
        'Se mostraran resultados de los siguientes paises:',
        paises)
    df=df_energia.set_index('pais')
    df=df.loc[multi_pais]
    if len(multi_pais)==0:
        fig1 = make_subplots()
        fig1.add_trace(go.Bar(x=df_energia['pais'],y=df_energia['energia_cons'],name='Consumo'))
        fig1.add_trace(go.Bar(x=df_energia['pais'],y=df_energia['energia_produccion'],base='stack',name='Produccion',opacity=0.6))
        fig1.add_trace(go.Scatter(x=df_energia['pais'],y=df_energia['net_energy'],name='Neto'))
        fig1.update_layout(go.Layout(
            barmode='overlay'
        ))
        fig1.update_layout( 
            title='Consumo vs produccion en top paises productores energia',
            barmode='stack')
    else:
        fig1 = make_subplots()
        fig1.add_trace(go.Bar(x=multi_pais,y=df['energia_cons'],name='Consumo'))
        fig1.add_trace(go.Bar(x=multi_pais,y=df['energia_produccion'],base='stack',name='Produccion',opacity=0.6))
        fig1.add_trace(go.Scatter(x=multi_pais,y=df['net_energy'],name='Neto'))
        fig1.update_layout(go.Layout(
            barmode='overlay'
        ))
        fig1.update_layout( title='Consumo vs produccion en top paises productores energia',
                            barmode='stack')

# emisiones chart
with cols[0]:
    # st.markdown("## Filtros")        
    start,end=st.sidebar.select_slider('Seleccione un rango de años',
                        options=años,
                        value=(min(años),max(años)))
    # st.write(f'Resultados entre los años {start} y {end}:')
    paises =['United States', 'China', 'Russia', 'Saudi Arabia', 'Canada']
    df_top=dftop[(dftop.pais.isin(paises))&(dftop.anio>=start)&(dftop.anio<=end)]
    selecdf=dftop.set_index('pais')
    selecdf=selecdf.loc[multi_pais]

    if len(multi_pais)==0:
        fig = px.line(df_top,x='anio',y='pct_chg_co2',color='pais')
        fig.update_layout(  
            title="Porcentaje de cambio en emisiones de CO2, TOP5 paises emisores",
                                )                        
    else:
        fig = px.line(selecdf,x='anio',y='pct_chg_co2',color=selecdf.index)
        fig.update_layout(  
            title="Porcentaje de cambio en emisiones de CO2",
                                )                        


#LAYOUT(CONTENT)
emision_column,energia_column=st.columns(2,gap='large')
energia_column.plotly_chart(fig1,use_container_width=True)
emision_column.plotly_chart(fig,use_container_width=True)



# Sidebar(layout)
# cat_selected = st.sidebar.selectbox('Categorical Variables', vars_cat)
# cont_selected = st.sidebar.selectbox('Continuous Variables', vars_cont)
# cont_multi_selected = st.sidebar.multiselect('Correlation Matrix', vars_cont,
#                                              default=vars_cont)
