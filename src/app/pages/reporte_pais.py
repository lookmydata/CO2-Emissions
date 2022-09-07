import pandas as pd
import streamlit as st
import plotly.express as px
from utils.bad_energies import BadEnergies
from utils.bad_energies import pct_plot

st.set_page_config(layout='wide')
@st.cache
def readcsv(csv):
    return pd.read_csv(csv)

def listcol(dfcol):
    dfcol=dfcol.unique()
    return dfcol.tolist()

#GET DATA#
df19=readcsv('src/app/utils/df19.csv')
dfst=readcsv('src/app/utils/df_streamlit.csv')

data_cons = BadEnergies(dfst).get_data('cons')
data_cons.dropna(axis='index',inplace=True)
data_produccion = BadEnergies(dfst).get_data('produccion')

data_cons.insert(1,'pais',dfst.pais)
data_cons.drop(columns='pais_iso',inplace=True)
data_cons.rename(columns={'pais':'pais_iso'},inplace=True)
data_produccion.insert(1,'pais',dfst.pais)
data_produccion.drop(columns='pais_iso',inplace=True)
data_produccion.rename(columns={'pais':'pais_iso'},inplace=True)


aa=listcol(data_cons.pais_iso)
dfst=dfst.loc[dfst.pais.isin(aa)]
df19=df19.loc[df19.pais.isin(aa)]

#LAYOUT#
kpis=st.columns(4,gap='medium')
grafs=st.columns(3,gap='large')

#LIST#
paises=aa

#SIDEBAR#
st.sidebar.markdown('## Se están mostrando resultados de:')
selecpais=st.sidebar.selectbox('seleccionar país',options=paises)
st.sidebar.image('src/app/utils/images/label_plot.jpeg',use_column_width=True)    
    
df_top=dfst[dfst.pais==selecpais]
df_top['pct_chg_co2']=df_top.pct_chg_co2.round(2)
with grafs[0]:
    fig = px.line(df_top,x='anio',y='pct_chg_co2',color='pais')
    fig.update_layout(  
            width=500,
            title="Porcentaje de cambio en emisiones de CO2",
            showlegend=False
            ,margin=dict(l=0, b=0, r=300, t=30, pad=0)    )
    st.plotly_chart(fig)


data_pct_cons = data_cons.get_pct_change(2010, 2019,None)
data_pct_cons=data_pct_cons[data_pct_cons.pais_iso==selecpais]
with grafs[1]:
    fig1 = pct_plot(data_pct_cons) 
    fig1.update_layout(
        title='Cambio porcentual en el consumo de energias'
        ,width=500
        ,showlegend=False
        ,margin=dict(l=0, b=0, r=300, t=30, pad=0)    )
               
    st.plotly_chart(fig1)

data_pct_produccion = data_produccion.get_pct_change(2010, 2019,None)
data_pct_produccion = data_pct_produccion[data_pct_produccion.pais_iso==selecpais]
with grafs[2]:
    fig3 = pct_plot(data_pct_produccion)
    fig3.update_layout(
        title='Cambio porcentual en la produccion de energias'
        ,width=500
        ,showlegend=False
        ,margin=dict(l=0, b=0, r=300, t=30, pad=0)    )
    st.plotly_chart(fig3)


df=df19.copy()
df=df[df.pais==selecpais]
with kpis[0]:  
    var=df.cumplimiento.values-45
    var1=df.cumplimiento.values
    st.metric("EMISIONES CO2 -45% A 2030", f'{round(float(var1),2)}%',f'{round(float(var),2)}%')

with kpis[1]:
    if type(df.cpm_carbon.values)==str:
        carb=df.cpm_carbon.values
        carb1=df.cpm_carbon.values
    elif type(df.cpm_carbon.values)==float:
        carb=round(float(df.cpm_carbon.values)-95,2)
        carb1=round(float(df.cpm_carbon.values),2)
        
    st.metric('REDUCCION CARBÓN -95% A 2050', f'{carb1}%',f'{carb}%')

with kpis[2]:
    if type(df.cpm_gas.values)==str:
        cpm_gas=df.cpm_gas.values
        cpm_gas1=df.cpm_gas.values
    elif type(df.cpm_gas.values)==float:
        cpm_gas=round(float(df.cpm_gas.values)-45,2)
        cpm_gas1=round(float(df.cpm_gas.values),2)
    st.metric('REDUCCION GAS -45% A 2050',f'{cpm_gas1}%',f'{cpm_gas}%')

with kpis[3]:
    if type(df.cpm_petroleo.values)==str:
        cpm_pet=df.cpm_petroleo.values
        cpm_pet1=df.cpm_petroleo.values
    elif type(df.cpm_petroleo.values)==float:
        cpm_pet=round(float(df.cpm_petroleo.values)-60,2)
        cpm_pet1=round(float(df.cpm_petroleo.values),2)
    st.metric('REDUCCION PETRÓLEO -60% A 2050',f'{cpm_pet1}%',f'{cpm_pet}%')
