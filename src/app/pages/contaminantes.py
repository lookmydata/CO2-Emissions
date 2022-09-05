from utils.bad_energies import BadEnergies
from utils.bad_energies import pct_plot
import streamlit as st
import pandas as pd

@st.cache
def read(csv):
    return pd.read_parquet(csv)

# LAYOUT #
st.set_page_config(layout='wide')
cols=st.columns(1,gap='large')
cont=st.columns(2,gap='large')
pct=st.columns(2,gap='large')

# GET DATA #
data=read('datasets/energy_consumption/owid-energy-consumption-source_normalizado.parquet')

# CONSUMO #
data_cons = BadEnergies(data).get_data('cons')
data_cons.dropna(inplace=True)
carbon_cons_fig, carbon_top_iso = data_cons.plot_and_top('carbon')
gas_cons_fig, gas_top_iso = data_cons.plot_and_top('gas')
petroleo_cons_fig, petroleo_top_iso = data_cons.plot_and_top('petroleo')

paises_cons=data_cons.pais_iso.unique()
paises_cons=paises_cons.tolist()
with cols[0]:
    multi_pais=st.sidebar.multiselect(
    'Se mostraran resultados de consumo los siguientes paises:',
    paises_cons)#,help='Si la lista está vacia mostrará un top 10 paises que mas consumen energias contaminantes.')

multi_dfcons=data_cons.set_index('pais_iso')
multi_dfcons=multi_dfcons.loc[multi_pais]
with cont[0]:
    if len(multi_pais)==0:
        fig, cons_table = data_cons.fig_and_table()
    else:    
        fig, cons_table = multi_dfcons.reset_index().fig_and_table()
    fig.update_layout(
        title='Consumo de energias contaminantes por pais'
                       )

    st.plotly_chart(fig,use_container_width=True)


data_pct_cons = data_cons.get_pct_change(2010, 2019)
df1=multi_dfcons.reset_index().get_pct_change(2010, 2019)
with pct[0]:
    if len(multi_pais)==0:
        fig1 = pct_plot(data_pct_cons) 
    else:
       fig1 = pct_plot(df1)

    fig1.update_layout(
        title='Cambio porcentual desde 2010 en el consumo de energias contaminantes'
                       )
    st.plotly_chart(fig1,use_container_width=True)


# PRODUCCION #
data_produccion = BadEnergies(data).get_data('produccion')
carbon_produccion_fig, carbon_top_iso = data_produccion.plot_and_top('carbon')
gas_produccion_fig, gas_top_iso = data_produccion.plot_and_top('gas')
petroleo_produccion_fig, petroleo_top_iso = data_produccion.plot_and_top('petroleo')


# with cols[1]:
#     multi_pais=st.multiselect(
#     'Se mostraran resultados de producción los siguientes paises:',
#     paises_cons)#,help='Si la lista está vacia mostrará un top 10 paises que mas consumen energias contaminantes.')


multi_dfprod=data_cons.set_index('pais_iso')
multi_dfprod=multi_dfprod.loc[multi_pais]
with cont[1]:
    if len(multi_pais)==0:
        fig2, produccion_table = data_produccion.fig_and_table()
    else:
        fig2, produccion_table = multi_dfprod.reset_index().fig_and_table()
    fig2.update_layout(
                        title='Produccion de energias contaminantes por pais'
                       ) #   x=0.90)
    st.plotly_chart(fig2,use_container_width=True)


data_pct_produccion = data_produccion.get_pct_change(2010, 2019)
df2=multi_dfprod.reset_index().get_pct_change(2010, 2019)
with pct[1]:
    if len(multi_pais)==0:
        fig3 = pct_plot(data_pct_produccion)
    else:
        fig3 = pct_plot(df2)
    fig3.update_layout(
        title='Cambio porcentual desde 2010 en la produccion de energias contaminante'
            )

    st.plotly_chart(fig3,use_container_width=True)


# fig = pct_plot(data_pct_produccion)
# fig.update_layout(
#     title='Cambio porcentual en la produccion de energias contaminantes por pais desde 2010')
