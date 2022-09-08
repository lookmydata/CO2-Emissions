import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
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
data_produccion = BadEnergies(dfst).get_data('produccion')
data_cons.dropna(axis='index',inplace=True)
data_cons.insert(1,'pais',dfst.pais)
data_produccion.insert(1,'pais',dfst.pais)
data_cons.drop(columns='pais_iso',inplace=True)
data_produccion.drop(columns='pais_iso',inplace=True)
data_cons.rename(columns={'pais':'pais_iso'},inplace=True)
data_produccion.rename(columns={'pais':'pais_iso'},inplace=True)


#LAYOUT#
kpis=st.columns(4,gap='medium')
grafs=st.columns(3,gap='small')

#LIST#
aa=listcol(df19.pais)
data_cons=data_cons[data_cons.pais_iso.isin(aa)]
dfst=dfst[dfst.pais.isin(aa)]
paises=aa

#SIDEBAR#
st.sidebar.markdown('### Se están mostrando resultados de:')
selecpais=st.sidebar.selectbox(' ',options=paises)

dfkpi=df19
dfkpi=dfkpi[dfkpi.pais==selecpais]
var2=str(dfkpi.pais.values)
var3=int(dfkpi.anio.values)
st.sidebar.metric(f'PBI {var2} AÑO {var3}',dfkpi.pbi)

st.sidebar.image('src/app/utils/images/label_plot.jpeg',use_column_width=True)    


#KPIs#
with kpis[0]:  
    var=round(float(dfkpi.cumplimiento.values-45),2)
    var1=round(float(dfkpi.cumplimiento.values),2)
    st.metric("EMISIONES CO2 -45% A 2030", f'{var1}%',f'{var}%')

with kpis[1]:
    carb=round(float(dfkpi.cpm_carbon.values)-95,2)
    carb1=round(float(dfkpi.cpm_carbon.values),2)
    st.metric('REDUCCION CARBÓN -95% A 2030', f'{carb1}%',f'{carb}%')

with kpis[2]:
    cpm_gas=round(float(dfkpi.cpm_gas.values)-45,2)
    cpm_gas1=round(float(dfkpi.cpm_gas.values),2)
    st.metric('REDUCCION GAS -45% A 2050',f'{cpm_gas1}%',f'{cpm_gas}%')

with kpis[3]:
    cpm_pet=round(float(dfkpi.cpm_petroleo.values)-60,2)
    cpm_pet1=round(float(dfkpi.cpm_petroleo.values),2)
    st.metric('REDUCCION PETRÓLEO -60% A 2050',f'{cpm_pet1}%',f'{cpm_pet}%')
    
    


#GRAFS#
df_top=dfst[dfst.pais==selecpais]
with grafs[0]:
    fig = px.line(df_top,x='anio',y='pct_chg_co2',color='pais')
    fig.update_layout(  
            width=500,
            title="Porcentaje de cambio en emisiones de CO2",
            showlegend=False
            ,margin=dict(l=0, b=0, r=300, t=30, pad=0)
            )
    fig.update_yaxes(title='% cambio')
    fig.update_xaxes(title='año')
    st.plotly_chart(fig)

data_pct_cons = data_cons.get_pct_change(2010, 2019,None)
data_pct_cons=data_pct_cons[data_pct_cons.pais_iso==selecpais]
with grafs[1]:
    fig1 = pct_plot(data_pct_cons) 
    fig1.update_layout(
        title='Cambio porcentual consumo de energia'
        ,width=500
        ,showlegend=False
        ,margin=dict(l=0, b=0, r=300, t=30, pad=0)    )
    fig1.update_xaxes(title='pais')
    fig1.update_yaxes(title='cambio porcentual')
               
    st.plotly_chart(fig1)

data_pct_produccion = data_produccion.get_pct_change(2010, 2019,None)
data_pct_produccion = data_pct_produccion[data_pct_produccion.pais_iso==selecpais]
with grafs[2]:
    fig3 = pct_plot(data_pct_produccion)
    fig3.update_layout(
        title='Cambio porcentual produccion de energia'
        ,width=500
        ,showlegend=False
        ,margin=dict(l=0, b=0, r=300, t=30, pad=0)    )
    fig3.update_xaxes(title='pais')
    fig3.update_yaxes(title='cambio porcentual')
    st.plotly_chart(fig3)

