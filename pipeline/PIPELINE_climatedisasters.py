# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python 3.9.1 64-bit
#     language: python
#     name: python3
# ---

import pandas as pd

df=pd.read_csv('../datasets/desastres_naturales/Climate-related_Disasters_Frequency_normalizado.csv',sep=';')
print(df)

# +
col=['Unnamed: 0','objectid','iso2','code','unidad','fuente']

df.drop(columns=col,inplace=True)
# +
cols=['pais','pais_iso','indicador']

df1=pd.melt(df,id_vars=cols,var_name='anio',value_name='frecuencia')

#df1.to_csv('../datasets/desastres_naturales/Climate-related_Disasters_Frequency_normalizado.csv',sep=';',index=False)
